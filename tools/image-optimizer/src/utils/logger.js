/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
class Logger {
  constructor(options = {}) {
    this.verbose = options.verbose || false;
    this.silent = options.silent || false;
    
    // Try to load chalk, but work without it if needed
    try {
      const chalkModule = require('chalk');
      this.chalk = chalkModule.default || chalkModule;
    } catch {
      // Fallback - no colors
      this.chalk = {
        red: (str) => str,
        yellow: (str) => str,
        blue: (str) => str,
        gray: (str) => str,
        dim: (str) => str
      };
    }
  }

  log(message) {
    if (!this.silent) {
      console.log(message);
    }
  }

  success(message) {
    if (!this.silent) {
      console.log(`[SUCCESS] ${message}`);
    }
  }

  error(message) {
    if (!this.silent) {
      console.error(this.chalk.red(`[ERROR] ${message}`));
    }
  }

  warning(message) {
    if (!this.silent) {
      console.warn(this.chalk.yellow(`[WARNING] ${message}`));
    }
  }

  info(message) {
    if (!this.silent) {
      console.info(this.chalk.blue(`[INFO] ${message}`));
    }
  }

  skip(message) {
    if (!this.silent) {
      console.log(this.chalk.gray(`[SKIPPED] ${message}`));
    }
  }

  verbose(message) {
    if (this.verbose && !this.silent) {
      console.log(this.chalk.dim(`[VERBOSE] ${message}`));
    }
  }

  divider(char = '=', length = 64) {
    if (!this.silent) {
      console.log(char.repeat(length));
    }
  }

  newline() {
    if (!this.silent) {
      console.log();
    }
  }

  header(title) {
    if (!this.silent) {
      this.log(title);
      this.divider();
    }
  }

  subheader(title) {
    if (!this.silent) {
      this.newline();
      this.log(title);
      this.divider('-');
    }
  }
}

module.exports = Logger;