/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
const sharp = require('sharp');
const path = require('path');
const FileUtils = require('../utils/file-utils');
const formats = require('../config/formats');
const defaults = require('../config/defaults');
const ErrorHandler = require('../utils/error-handler');

class Processor {
  constructor(logger, errorHandler) {
    this.logger = logger;
    this.errorHandler = errorHandler;
  }

  async process(filePath, options = {}) {
    try {
      const startTime = Date.now();
      const originalSize = await FileUtils.getFileSize(filePath);
      const extension = FileUtils.getExtension(filePath);
      const format = formats.getFormatFromExtension(extension);
      
      if (!format) {
        return {
          status: 'error',
          filePath,
          error: `Unsupported format: ${extension}`,
          errorType: 'unsupported_format'
        };
      }
      
      // Get optimization strategy
      const strategy = {
        ...defaults.optimizationStrategies[format],
        ...options
      };
      
      // Process image
      const buffer = await this.optimizeImage(filePath, format, strategy);
      
      const newSize = buffer.length;
      const reduction = FileUtils.calculateReduction(originalSize, newSize);
      const processingTime = Date.now() - startTime;
      
      // Skip if reduction is minimal
      const skipThreshold = options.skipThreshold !== undefined ? options.skipThreshold : defaults.processingOptions.skipThreshold;
      const minReduction = (1 - skipThreshold) * 100; // Convert to percentage
      
      if (parseFloat(reduction) < minReduction) {
        // If output directory is specified, copy the original file even if skipped
        if (options.outputDir && !options.dryRun) {
          const scanDir = options.scanDirectory || path.dirname(filePath);
          const relativePath = path.relative(scanDir, filePath);
          const outputPath = path.join(options.outputDir, relativePath);
          
          // Create subdirectories if needed
          const outputSubDir = path.dirname(outputPath);
          if (!await FileUtils.fileExists(outputSubDir)) {
            await FileUtils.ensureDirectory(outputSubDir);
          }
          
          // Copy original file
          await FileUtils.copyFile(filePath, outputPath);
        }
        
        return {
          status: 'skipped',
          reason: 'no significant reduction',
          filePath,
          outputPath: options.outputDir ? path.join(options.outputDir, path.relative(options.scanDirectory || path.dirname(filePath), filePath)) : undefined,
          originalSize,
          newSize,
          reduction,
          processingTime
        };
      }
      
      // Determine output path
      let outputPath = filePath;
      if (options.outputDir) {
        // Calculate relative path from scan directory to file
        const scanDir = options.scanDirectory || path.dirname(filePath);
        const relativePath = path.relative(scanDir, filePath);
        outputPath = path.join(options.outputDir, relativePath);
        
        // Create subdirectories if needed (only if not dry-run)
        if (!options.dryRun) {
          const outputSubDir = path.dirname(outputPath);
          if (!await FileUtils.fileExists(outputSubDir)) {
            await FileUtils.ensureDirectory(outputSubDir);
          }
        }
      }
      
      // Save optimized image
      if (!options.dryRun) {
        await FileUtils.writeFile(outputPath, buffer);
      }
      
      return {
        status: 'success',
        filePath,
        outputPath: outputPath !== filePath ? outputPath : undefined,
        originalSize,
        newSize,
        reduction,
        processingTime,
        format
      };
      
    } catch (error) {
      this.errorHandler.handle(error, filePath);
      return {
        status: 'error',
        filePath,
        error: error.message,
        errorType: ErrorHandler.categorizeError(error)
      };
    }
  }

  async optimizeImage(filePath, format, strategy) {
    let pipeline = sharp(filePath);
    
    // Apply format-specific optimizations
    switch (format) {
      case 'image/jpeg':
        pipeline = pipeline.jpeg({
          quality: strategy.quality,
          progressive: strategy.progressive,
          mozjpeg: strategy.mozjpeg
        });
        break;
        
      case 'image/png':
        pipeline = pipeline.png({
          compressionLevel: strategy.compressionLevel,
          palette: strategy.palette,
          adaptiveFiltering: strategy.adaptiveFiltering
        });
        break;
        
      case 'image/webp':
        pipeline = pipeline.webp({
          quality: strategy.quality,
          lossless: strategy.lossless,
          nearLossless: strategy.nearLossless,
          smartSubsample: strategy.smartSubsample
        });
        break;
        
      case 'image/gif':
        // Sharp doesn't support GIF optimization well
        // Just pass through for now
        return await FileUtils.readFile(filePath);
        
      case 'image/avif':
        pipeline = pipeline.avif({
          quality: strategy.quality,
          lossless: strategy.lossless,
          effort: strategy.effort
        });
        break;
    }
    
    // Strip metadata if requested
    if (strategy.stripMetadata) {
      // Don't include metadata - withMetadata() without args preserves metadata
      // So we skip calling it when we want to strip metadata
    } else {
      // Keep metadata
      pipeline = pipeline.withMetadata();
    }
    
    return await pipeline.toBuffer();
  }

}

module.exports = Processor;