#!/usr/bin/env node
/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 * 
 * TR: Phantom Image Optimizer CLI (optimize.js)
 * ==============================================
 * 
 * Bu script, Phantom Documentation Kit'in görsel optimizasyon CLI aracıdır. Modern 
 * dokümantasyon projelerinde kullanılan görselleri optimize ederek, performanslı ve 
 * hızlı yüklenen dokümantasyon sayfaları oluşturmayı amaçlar.
 * Bu araç aynı zamanda Phantom Documentation Kit yapısından bağımsızda çalıştırılabilir veya farklı projelerinizde
 * kullanılabilir. Ancak Phantom Documentation Kit ihtiyaçları için geliştirilmiştir ve bu projeyle beraber
 * geliştirilmeye devam edecektir.
 *
 * Önemli Notlar
 * --------------
 * Bu CLI aracı, Sharp kütüphanesinin güçlü optimizasyon yeteneklerini kullanarak 
 * görsellerinizi optimize eder. Mevcut konfigürasyon, çoğu dokümantasyon projesi 
 * için optimal bir denge sağlar, ancak özel ihtiyaçlarınıza göre ayarlanabilir.
 * 
 * Kullanım Örnekleri:
 * 
 * Temel kullanım:
 *   phantom-optimize ./images
 *   - images/ dizinindeki tüm görselleri optimize eder
 *   - Varsayılan kalite ayarları kullanılır
 *   - Orijinal dosyalar üzerine yazılır
 * 
 * Kalite kontrollü optimizasyon:
 *   phantom-optimize ./docs -q 85 --output ./optimized
 *   - %85 kalite ile optimize eder
 *   - Sonuçları optimized/ dizinine kaydeder
 *   - Orijinal dosyalar korunur
 * 
 * Belirli formatlar için:
 *   phantom-optimize ./assets -f jpeg,png --skip-threshold 5
 *   - Sadece JPEG ve PNG dosyalarını işler
 *   - %5'ten az kazanç sağlayacak dosyaları atlar
 * 
 * Dry-run modu:
 *   phantom-optimize ./images --dry-run --verbose
 *   - Hiçbir dosyayı değiştirmez
 *   - Nelerin optimize edileceğini gösterir
 *   - Detaylı çıktı sağlar
 * 
 * CLI Parametreleri:
 *   - -q, --quality: JPEG/WebP kalitesi (0-100, varsayılan: 80)
 *   - -f, --formats: İşlenecek formatlar (varsayılan: jpeg,png,webp,gif,avif)
 *   - -c, --concurrency: Paralel işlem sayısı (varsayılan: CPU sayısı)
 *   - -o, --output: Çıktı dizini (belirtilmezse üzerine yazar)
 *   - --dry-run: Değişiklik yapmadan simülasyon
 *   - -v, --verbose: Detaylı çıktı
 *   - -s, --silent: Sadece hatalar gösterilir
 *   - --no-strip-metadata: EXIF verilerini korur
 *   - --skip-threshold: Minimum kazanç eşiği (%)
 * 
 * Nasıl Çalışır? (Adım Adım)
 * ---------------------------
 * Kullanıcı "phantom-optimize ./images" komutunu çalıştırdığında:
 * 
 *   1. CLI → Argüman kontrolü ve validasyon
 *   2. Dizin kontrolü → Hedef dizinin varlığı doğrulanır
 *   3. Optimizer başlatma → Core optimizer sınıfı oluşturulur
 *   4. Görsel tarama → Desteklenen formatlar bulunur
 *   5. Her görsel için:
 *      - Sharp ile yükleme
 *      - Format-spesifik optimizasyon
 *      - Boyut karşılaştırması
 *      - Kaydetme veya atlama
 *   6. Sonuç → Optimizasyon raporu ve istatistikler
 * 
 * Çalışma Akışı:
 * --------------
 * 
 * 1. CLI → Node.js → Sharp Pipeline:
 *    optimize.js → Commander.js → Optimizer → Sharp
 *    - Commander.js ile CLI argümanları parse edilir
 *    - Optimizer sınıfı konfigürasyonu alır
 *    - Sharp pipeline'ı oluşturulur ve çalıştırılır
 * 
 * 2. Optimizasyon Süreci:
 *    Kaynak Görsel → Sharp Pipeline → Optimize Edilmiş Görsel
 *    - JPEG: mozjpeg encoder, progressive, optimize coding
 *    - PNG: Renk paleti azaltma, kompresyon seviyesi
 *    - WebP: Kalite ve kayıpsız mod desteği
 *    - GIF: Renk azaltma ve optimizasyon
 *    - AVIF: Modern codec ile yüksek sıkıştırma
 * 
 * 3. Dosya Yönetimi:
 *    Tarama → İşleme → Kaydetme/Üzerine Yazma
 *    - Recursive dizin taraması
 *    - Paralel işleme (p-limit ile kontrol)
 *    - Atomik dosya yazma (güvenli)
 * 
 * Ana Özellikler:
 * ---------------
 * - Toplu görsel optimizasyonu
 * - Format korumalı veya çapraz format dönüşümü
 * - Metadata temizleme (EXIF, ICC profilleri)
 * - İlerleme göstergesi ve detaylı raporlama
 * - Dry-run modu ile güvenli test
 * 
 * Entegrasyon Noktaları:
 * ---------------------
 * - package.json: Global kurulum için bin konfigürasyonu
 * - src/core/optimizer.js: Ana optimizasyon motoru
 * - src/core/processor.js: Görsel işleme pipeline'ı
 * - src/utils/: Yardımcı fonksiyonlar (logger, stats)
 * 
 * npm Entegrasyonu:
 * ----------------
 * - npm link: Geliştirme sırasında global kullanım
 * - npm install -g: Production kurulumu
 *
 * ========================================================
 * 
 * EN: Phantom Image Optimizer CLI (optimize.js)
 * ==============================================
 * 
 * This script is the image optimization CLI tool for Phantom Documentation Kit. It aims 
 * to create performant and fast-loading documentation pages by optimizing images used 
 * in modern documentation projects.
 * This tool can also be run independently from the Phantom Documentation Kit structure or used in your other projects.
 * However, it has been developed for Phantom Documentation Kit needs and will continue to be developed
 * alongside this project.
 * 
 * Important Notes
 * ---------------
 * This CLI tool optimizes your images using Sharp library's powerful optimization 
 * capabilities. The current configuration provides an optimal balance for most 
 * documentation projects, but can be adjusted according to your specific needs.
 * 
 * Usage Examples:
 * 
 * Basic usage:
 *   phantom-optimize ./images
 *   - Optimizes all images in images/ directory
 *   - Uses default quality settings
 *   - Overwrites original files
 * 
 * Quality-controlled optimization:
 *   phantom-optimize ./docs -q 85 --output ./optimized
 *   - Optimizes with 85% quality
 *   - Saves results to optimized/ directory
 *   - Preserves original files
 * 
 * For specific formats:
 *   phantom-optimize ./assets -f jpeg,png --skip-threshold 5
 *   - Processes only JPEG and PNG files
 *   - Skips files with less than 5% gain
 * 
 * Dry-run mode:
 *   phantom-optimize ./images --dry-run --verbose
 *   - Doesn't modify any files
 *   - Shows what would be optimized
 *   - Provides detailed output
 * 
 * CLI Parameters:
 *   - -q, --quality: JPEG/WebP quality (0-100, default: 80)
 *   - -f, --formats: Formats to process (default: jpeg,png,webp,gif,avif)
 *   - -c, --concurrency: Parallel processing count (default: CPU count)
 *   - -o, --output: Output directory (overwrites if not specified)
 *   - --dry-run: Simulation without changes
 *   - -v, --verbose: Detailed output
 *   - -s, --silent: Show only errors
 *   - --no-strip-metadata: Keep EXIF data
 *   - --skip-threshold: Minimum gain threshold (%)
 * 
 * How It Works? (Step by Step)
 * -----------------------------
 * When a user runs "phantom-optimize ./images":
 * 
 *   1. CLI → Argument parsing and validation
 *   2. Directory check → Target directory existence verified
 *   3. Optimizer init → Core optimizer class created
 *   4. Image scanning → Supported formats found
 *   5. For each image:
 *      - Load with Sharp
 *      - Format-specific optimization
 *      - Size comparison
 *      - Save or skip
 *   6. Result → Optimization report and statistics
 * 
 * Workflow:
 * ---------
 * 
 * 1. CLI → Node.js → Sharp Pipeline:
 *    optimize.js → Commander.js → Optimizer → Sharp
 *    - CLI arguments parsed with Commander.js
 *    - Optimizer class receives configuration
 *    - Sharp pipeline created and executed
 * 
 * 2. Optimization Process:
 *    Source Image → Sharp Pipeline → Optimized Image
 *    - JPEG: mozjpeg encoder, progressive, optimize coding
 *    - PNG: Color palette reduction, compression level
 *    - WebP: Quality and lossless mode support
 *    - GIF: Color reduction and optimization
 *    - AVIF: High compression with modern codec
 * 
 * 3. File Management:
 *    Scan → Process → Save/Overwrite
 *    - Recursive directory scanning
 *    - Parallel processing (controlled with p-limit)
 *    - Atomic file writing (safe)
 * 
 * Key Features:
 * ------------
 * - Batch image optimization
 * - Format-preserving or cross-format conversion
 * - Metadata stripping (EXIF, ICC profiles)
 * - Progress indicator and detailed reporting
 * - Safe testing with dry-run mode
 * 
 * Integration Points:
 * ------------------
 * - package.json: bin configuration for global installation
 * - src/core/optimizer.js: Main optimization engine
 * - src/core/processor.js: Image processing pipeline
 * - src/utils/: Helper functions (logger, stats)
 * 
 * npm Integration:
 * ---------------
 * - npm link: Global usage during development
 * - npm install -g: Production installation
 *
 */

const { program } = require('commander');
const path = require('path');
const fs = require('fs');
const Optimizer = require('./src/core/optimizer');
const packageJson = require('./package.json');

// Define CLI
program
  .name('phantom-optimize')
  .description(packageJson.description)
  .version(packageJson.version)
  .argument('<directory>', 'Directory to scan for images')
  .option('-q, --quality <number>', 'JPEG/WebP quality (0-100)', parseInt)
  .option('-f, --formats <formats>', 'Comma-separated list of formats to process (jpeg,png,webp,gif,avif)')
  .option('-c, --concurrency <number>', 'Number of images to process in parallel', parseInt)
  .option('-o, --output <directory>', 'Output directory for optimized images (preserves originals)')
  .option('--dry-run', 'Show what would be optimized without making changes')
  .option('-v, --verbose', 'Show detailed output')
  .option('-s, --silent', 'Suppress all output except errors')
  .option('--no-strip-metadata', 'Keep image metadata')
  .option('--skip-threshold <percent>', 'Skip if reduction is less than this percentage', parseFloat)
  .action(async (directory, options) => {
    try {
      // Resolve directory path
      const targetDir = path.resolve(directory);
      
      // Check if directory exists
      if (!fs.existsSync(targetDir)) {
        console.error(`[ERROR] Directory not found: ${targetDir}`);
        process.exit(1);
      }
      
      // Check if it's a directory
      const stats = fs.statSync(targetDir);
      if (!stats.isDirectory()) {
        console.error(`[ERROR] Not a directory: ${targetDir}`);
        process.exit(1);
      }
      
      // Prepare options
      const optimizerOptions = {
        verbose: options.verbose,
        silent: options.silent,
        dryRun: options.dryRun,
        stripMetadata: options.stripMetadata !== false
      };
      
      if (options.quality) {
        if (options.quality < 0 || options.quality > 100) {
          console.error('[ERROR] Quality must be between 0 and 100');
          process.exit(1);
        }
        optimizerOptions.quality = options.quality;
      }
      
      if (options.concurrency !== undefined) {
        if (options.concurrency < 1) {
          console.error('[ERROR] Concurrency must be at least 1');
          process.exit(1);
        }
        optimizerOptions.maxConcurrency = options.concurrency;
      }
      
      if (options.skipThreshold) {
        optimizerOptions.skipThreshold = (100 - options.skipThreshold) / 100;
      }
      
      if (options.formats) {
        optimizerOptions.formats = options.formats.split(',').map(f => f.trim());
      }
      
      if (options.output) {
        const outputDir = path.resolve(options.output);
        
        // In dry-run mode, only validate the output path
        if (options.dryRun) {
          if (fs.existsSync(outputDir)) {
            const outputStats = fs.statSync(outputDir);
            if (!outputStats.isDirectory()) {
              console.error(`[ERROR] Output path exists but is not a directory: ${outputDir}`);
              process.exit(1);
            }
          }
          // Don't create directory in dry-run mode
          if (!options.silent) {
            console.log(`[INFO] Dry-run mode - would save to: ${outputDir}`);
          }
        } else {
          // Create output directory if it doesn't exist (only in non-dry-run mode)
          if (!fs.existsSync(outputDir)) {
            try {
              fs.mkdirSync(outputDir, { recursive: true });
              if (!options.silent) {
                console.log(`[INFO] Created output directory: ${outputDir}`);
              }
            } catch (error) {
              console.error(`[ERROR] Failed to create output directory: ${error.message}`);
              process.exit(1);
            }
          }
          
          // Check if output is a directory
          const outputStats = fs.statSync(outputDir);
          if (!outputStats.isDirectory()) {
            console.error(`[ERROR] Output path is not a directory: ${outputDir}`);
            process.exit(1);
          }
        }
        
        optimizerOptions.outputDir = outputDir;
      }
      
      // Create optimizer instance
      const optimizer = new Optimizer(optimizerOptions);
      
      // Run optimization
      if (!options.silent) {
        console.log(`[INFO] Starting optimization of: ${targetDir}`);
        if (options.dryRun) {
          console.log('[INFO] Running in dry-run mode - no files will be modified');
        }
      }
      
      const results = await optimizer.optimize(targetDir, optimizerOptions);
      
      // Exit with error code if there were failures
      if (results.stats.failed > 0) {
        process.exit(1);
      }
      
      process.exit(0);
      
    } catch (error) {
      console.error(`[ERROR] ${error.message}`);
      if (options.verbose) {
        console.error(error.stack);
      }
      process.exit(1);
    }
  });

// Parse arguments
program.parse();

// Show help if no arguments
if (!process.argv.slice(2).length) {
  program.outputHelp();
}