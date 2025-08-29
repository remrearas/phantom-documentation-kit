/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
class ErrorHandler {
  constructor(logger) {
    this.logger = logger;
    this.errors = [];
  }

  handle(error, context = '') {
    const errorInfo = {
      message: error.message,
      context,
      timestamp: new Date().toISOString(),
      stack: error.stack
    };
    
    this.errors.push(errorInfo);
    
    if (context) {
      this.logger.error(`${context}: ${error.message}`);
    } else {
      this.logger.error(error.message);
    }
    
    return errorInfo;
  }

  getErrors() {
    return this.errors;
  }

  getErrorSummary() {
    const summary = {};
    
    this.errors.forEach(error => {
      const key = error.message;
      if (!summary[key]) {
        summary[key] = {
          message: key,
          count: 0,
          contexts: []
        };
      }
      summary[key].count++;
      if (error.context) {
        summary[key].contexts.push(error.context);
      }
    });
    
    return Object.values(summary);
  }

  static categorizeError(error) {
    if (error.code === 'ENOENT') {
      return 'file_not_found';
    } else if (error.code === 'EACCES') {
      return 'permission_denied';
    } else if (error.code === 'EISDIR') {
      return 'is_directory';
    } else if (error.message.includes('Invalid') || error.message.includes('Unsupported')) {
      return 'invalid_format';
    } else if (error.message.includes('timeout')) {
      return 'timeout';
    } else {
      return 'unknown';
    }
  }
}

module.exports = ErrorHandler;