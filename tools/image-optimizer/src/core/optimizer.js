/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
const os = require('os');
const { default: pLimit } = require('p-limit');
const oraModule = require('ora');
const ora = oraModule.default || oraModule;
const Scanner = require('./scanner');
const Processor = require('./processor');
const Reporter = require('../utils/reporter');
const ErrorHandler = require('../utils/error-handler');
const Logger = require('../utils/logger');
const defaults = require('../config/defaults');

class Optimizer {
  constructor(options = {}) {
    this.options = {
      ...defaults.processingOptions,
      ...options
    };
    
    // Set concurrency to CPU count if not specified
    if (!this.options.maxConcurrency) {
      this.options.maxConcurrency = os.cpus().length;
    }
    
    this.logger = new Logger(options);
    this.errorHandler = new ErrorHandler(this.logger);
    this.scanner = new Scanner(this.logger);
    this.processor = new Processor(this.logger, this.errorHandler);
    this.reporter = new Reporter(this.logger);
    
    this.stats = {
      totalFiles: 0,
      processed: 0,
      succeeded: 0,
      skipped: 0,
      failed: 0,
      totalOriginalSize: 0,
      totalOptimizedSize: 0,
      startTime: null,
      endTime: null
    };
  }

  async optimize(directory, userOptions = {}) {
    const options = { ...this.options, ...userOptions };
    const limit = pLimit(options.maxConcurrency);
    
    this.stats.startTime = Date.now();
    
    try {
      // Scan directory
      const spinner = !options.silent ? ora('Scanning directory...').start() : null;
      const scanOptions = {
        formats: options.formats
      };
      const scanResult = await this.scanner.scan(directory, scanOptions);
      if (spinner) spinner.succeed(`Found ${scanResult.count} images`);
      
      this.stats.totalFiles = scanResult.count;
      this.stats.totalOriginalSize = scanResult.totalSize;
      
      if (scanResult.count === 0) {
        this.logger.warning('No images found to optimize');
        return this.getResults();
      }
      
      // Process images
      const progressSpinner = !options.silent ? ora({
        text: 'Processing images...',
        spinner: 'dots'
      }).start() : null;
      
      const results = await Promise.all(
        scanResult.files.map((file) =>
          limit(async () => {
            const processOptions = {
              ...options,
              scanDirectory: directory
            };
            const result = await this.processor.process(file.path, processOptions);
            
            this.stats.processed++;
            
            // Update stats based on result
            switch (result.status) {
              case 'success':
                this.stats.succeeded++;
                this.stats.totalOptimizedSize += result.newSize;
                break;
              case 'skipped':
                this.stats.skipped++;
                this.stats.totalOptimizedSize += result.originalSize;
                break;
              case 'error':
                this.stats.failed++;
                this.stats.totalOptimizedSize += file.size;
                break;
            }
            
            // Update progress
            if (progressSpinner) {
              const progress = Math.round((this.stats.processed / this.stats.totalFiles) * 100);
              progressSpinner.text = `Processing images... ${progress}% | ${this.stats.processed}/${this.stats.totalFiles} files`;
            }
            
            return result;
          })
        )
      );
      
      if (progressSpinner) progressSpinner.succeed('Processing complete');
      
      this.stats.endTime = Date.now();
      
      // Generate report
      await this.reporter.generateReport({
        directory,
        stats: this.stats,
        results,
        errors: this.errorHandler.getErrorSummary(),
        options
      });
      
      return this.getResults();
      
    } catch (error) {
      this.logger.error(`Optimization failed: ${error.message}`);
      throw error;
    }
  }

  getResults() {
    return {
      stats: this.stats,
      errors: this.errorHandler.getErrors(),
      processingTime: this.stats.endTime - this.stats.startTime
    };
  }

}

module.exports = Optimizer;