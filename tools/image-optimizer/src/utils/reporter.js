/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
const bytes = require('bytes');
const FileUtils = require('./file-utils');

class Reporter {
  constructor(logger) {
    this.logger = logger;
  }

  async generateReport(data) {
    const { directory, stats, results, errors, options = {} } = data;
    const processingTime = ((stats.endTime - stats.startTime) / 1000).toFixed(1);
    
    this.logger.newline();
    this.logger.header('Image Optimization Report');
    this.logger.newline();
    
    this.logger.log(`Scanned Directory: ${directory}`);
    this.logger.log(`Date: ${new Date().toISOString().replace('T', ' ').split('.')[0]}`);
    
    this.logger.subheader('Summary');
    this.logger.log(`Total Images Found: ${stats.totalFiles}`);
    
    if (options.dryRun) {
      this.logger.log(`Would Optimize: ${stats.succeeded} images`);
      this.logger.log(`Would Skip: ${stats.skipped} images`);
      if (stats.failed > 0) {
        this.logger.log(`Errors Found: ${stats.failed}`);
      }
      this.logger.newline();
      this.logger.log(`Potential Size Reduction: ${FileUtils.formatReduction(
        stats.totalOriginalSize,
        stats.totalOptimizedSize
      )}`);
    } else {
      this.logger.log(`Successfully Optimized: ${stats.succeeded}`);
      this.logger.log(`Skipped (already optimized): ${stats.skipped}`);
      this.logger.log(`Failed: ${stats.failed}`);
      this.logger.newline();
      this.logger.log(`Total Size Reduction: ${FileUtils.formatReduction(
        stats.totalOriginalSize,
        stats.totalOptimizedSize
      )}`);
    }
    
    this.logger.log(`Processing Time: ${processingTime} seconds`);
    
    // Detailed results - only show if not in dry-run mode or silent mode
    if (results.length > 0 && !options.dryRun && !options.silent) {
      this.logger.subheader('Detailed Results');
      
      // Success results
      const successResults = results.filter(r => r.status === 'success');
      if (successResults.length > 0) {
        successResults.forEach(result => {
          this.logger.success(FileUtils.getFilename(result.filePath));
          this.logger.log(`   Original: ${bytes(result.originalSize)} -> Optimized: ${bytes(result.newSize)} (${result.reduction}% reduction)`);
          if (result.outputPath) {
            this.logger.log(`   Saved to: ${result.outputPath}`);
          }
        });
      }
      
      // Skipped results
      const skippedResults = results.filter(r => r.status === 'skipped');
      if (skippedResults.length > 0) {
        this.logger.newline();
        skippedResults.forEach(result => {
          this.logger.skip(FileUtils.getFilename(result.filePath));
          this.logger.log(`   Reason: ${result.reason}`);
          if (result.outputPath) {
            this.logger.log(`   Copied to: ${result.outputPath}`);
          }
        });
      }
      
      // Error results
      const errorResults = results.filter(r => r.status === 'error');
      if (errorResults.length > 0) {
        this.logger.newline();
        errorResults.forEach(result => {
          this.logger.error(FileUtils.getFilename(result.filePath));
          this.logger.log(`   Error: ${result.error}`);
        });
      }
    }
    
    // Format breakdown - only show if not in dry-run mode
    if (!options.dryRun) {
      const formatBreakdown = this.calculateFormatBreakdown(results);
      if (Object.keys(formatBreakdown).length > 0) {
        this.logger.subheader('Optimization Breakdown by Format');
        
        Object.entries(formatBreakdown).forEach(([format, data]) => {
          const formatName = format.replace('image/', '').toUpperCase();
          this.logger.log(`${formatName}: ${data.count} files, ${FileUtils.formatReduction(
            data.originalSize,
            data.optimizedSize
          )}`);
        });
      }
    }
    
    // Error summary
    if (errors.length > 0) {
      this.logger.subheader('Error Summary');
      this.logger.log(`${stats.failed} files failed optimization:`);
      
      errors.forEach(error => {
        this.logger.log(`   - ${error.message}: ${error.count} occurrence(s)`);
        if (error.contexts.length > 0 && error.contexts.length <= 3) {
          error.contexts.forEach(ctx => {
            this.logger.log(`     - ${FileUtils.getFilename(ctx)}`);
          });
        }
      });
    }
    
    this.logger.newline();
    this.logger.divider();
  }

  calculateFormatBreakdown(results) {
    const breakdown = {};
    
    results.forEach(result => {
      if (result.status === 'success' && result.format) {
        if (!breakdown[result.format]) {
          breakdown[result.format] = {
            count: 0,
            originalSize: 0,
            optimizedSize: 0
          };
        }
        
        breakdown[result.format].count++;
        breakdown[result.format].originalSize += result.originalSize;
        breakdown[result.format].optimizedSize += result.newSize;
      }
    });
    
    return breakdown;
  }

}

module.exports = Reporter;