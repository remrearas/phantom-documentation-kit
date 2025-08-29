/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
const fs = require('fs').promises;
const path = require('path');
const bytes = require('bytes');

class FileUtils {
  static async getFileSize(filePath) {
    const stats = await fs.stat(filePath);
    return stats.size;
  }

  static async getFileSizeFormatted(filePath) {
    const size = await this.getFileSize(filePath);
    return bytes(size);
  }

  static async ensureDirectory(dirPath) {
    try {
      await fs.mkdir(dirPath, { recursive: true });
    } catch (error) {
      if (error.code !== 'EEXIST') {
        throw error;
      }
    }
  }

  static async copyFile(source, destination) {
    await fs.copyFile(source, destination);
  }

  static async readFile(filePath) {
    return await fs.readFile(filePath);
  }

  static async writeFile(filePath, data) {
    await fs.writeFile(filePath, data);
  }

  static async fileExists(filePath) {
    try {
      await fs.access(filePath);
      return true;
    } catch {
      return false;
    }
  }

  static getExtension(filePath) {
    return path.extname(filePath).toLowerCase();
  }

  static getFilename(filePath) {
    return path.basename(filePath);
  }

  static getDirectory(filePath) {
    return path.dirname(filePath);
  }

  static calculateReduction(originalSize, newSize) {
    if (originalSize === 0) return 0;
    return ((originalSize - newSize) / originalSize * 100).toFixed(1);
  }

  static formatReduction(originalSize, newSize) {
    const reduction = this.calculateReduction(originalSize, newSize);
    const originalFormatted = bytes(originalSize);
    const newFormatted = bytes(newSize);
    return `${originalFormatted} -> ${newFormatted} (${reduction}% reduction)`;
  }

  static async isReadable(filePath) {
    try {
      await fs.access(filePath, fs.constants.R_OK);
      return true;
    } catch {
      return false;
    }
  }

  static async isWritable(filePath) {
    try {
      await fs.access(filePath, fs.constants.W_OK);
      return true;
    } catch {
      return false;
    }
  }
}

module.exports = FileUtils;