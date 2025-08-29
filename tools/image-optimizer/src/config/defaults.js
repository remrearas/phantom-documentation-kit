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
  optimizationStrategies: {
    'image/jpeg': {
      quality: 85,
      progressive: true,
      mozjpeg: true,
      stripMetadata: true
    },
    'image/png': {
      compressionLevel: 9,
      palette: true,
      stripMetadata: true,
      adaptiveFiltering: true
    },
    'image/webp': {
      quality: 80,
      lossless: false,
      nearLossless: 50,
      smartSubsample: true
    },
    'image/gif': {
      optimizationLevel: 3,
      colors: 256
    },
    'image/avif': {
      quality: 75,
      lossless: false,
      effort: 4
    }
  },
  processingOptions: {
    maxConcurrency: null, // Will be set to CPU count
    skipThreshold: 0.95, // Skip if reduction is less than 5%
    maxFileSize: 100 * 1024 * 1024, // 100MB max file size
    timeout: 60000 // 60 seconds per image
  },
  outputOptions: {
    preserveOriginal: true,
    overwrite: true,
    reportFormat: 'detailed' // 'detailed' or 'summary'
  }
};