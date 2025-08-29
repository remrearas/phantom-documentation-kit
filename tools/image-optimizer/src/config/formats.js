/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
module.exports = {
  supportedFormats: {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.webp': 'image/webp',
    '.gif': 'image/gif',
    '.avif': 'image/avif'
  },
  
  getFormatFromExtension(extension) {
    return this.supportedFormats[extension.toLowerCase()] || null;
  },
  
  isImageFile(filename) {
    const ext = filename.substring(filename.lastIndexOf('.')).toLowerCase();
    return this.supportedFormats.hasOwnProperty(ext);
  },
  
  getExtensionsPattern() {
    const extensions = Object.keys(this.supportedFormats);
    // Remove dots from extensions
    const cleanExtensions = extensions.map(ext => ext.replace('.', ''));
    // Create pattern like: **/*.{jpg,jpeg,png,webp,gif,avif}
    return `**/*.{${cleanExtensions.join(',')}}`;
  }
};