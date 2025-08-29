/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
const { glob } = require('glob');
const path = require('path');
const FileUtils = require('../utils/file-utils');
const formats = require('../config/formats');

class Scanner {
  constructor(logger) {
    this.logger = logger;
  }

  async scan(directory, options = {}) {
    const pattern = options.pattern || formats.getExtensionsPattern();
    const fullPattern = path.join(directory, pattern);
    
    
    // Check if logger exists and has verbose method
    if (this.logger && typeof this.logger.verbose === 'function') {
      this.logger.verbose(`Scanning pattern: ${fullPattern}`);
    }
    
    try {
      // Use modern glob with async/await
      const files = await glob(fullPattern, {
        nodir: true,
        dot: false,
        ignore: options.ignore || []
      });
      
      // Filter only image files
      let imageFiles = files.filter(file => formats.isImageFile(file));
      
      // Apply format filter if specified
      if (options.formats && Array.isArray(options.formats)) {
        const allowedExtensions = options.formats.map(f => `.${f.toLowerCase()}`);
        imageFiles = imageFiles.filter(file => {
          const ext = FileUtils.getExtension(file).toLowerCase();
          return allowedExtensions.includes(ext);
        });
      }
      
      // Get file stats
      const fileStats = await Promise.all(
        imageFiles.map(async (file) => {
          try {
            const size = await FileUtils.getFileSize(file);
            return {
              path: file,
              size,
              extension: FileUtils.getExtension(file),
              filename: FileUtils.getFilename(file),
              directory: FileUtils.getDirectory(file)
            };
          } catch (error) {
            if (this.logger && typeof this.logger.warning === 'function') {
              this.logger.warning(`Could not stat file ${file}: ${error.message}`);
            }
            return null;
          }
        })
      );
      
      // Filter out null entries
      const validFiles = fileStats.filter(stat => stat !== null);
      
      
      // Sort by size (largest first)
      validFiles.sort((a, b) => b.size - a.size);
      
      if (this.logger && typeof this.logger.info === 'function') {
        this.logger.info(`Found ${validFiles.length} image files in ${directory}`);
      }

      return {
        directory,
        files: validFiles,
        totalSize: validFiles.reduce((sum, file) => sum + file.size, 0),
        count: validFiles.length
      };
      
    } catch (error) {
      throw error;
    }
  }

}

module.exports = Scanner;