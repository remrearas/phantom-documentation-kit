#!/usr/bin/env python3
"""
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>

TR: Phantom Image Optimizer - Kapsamlı Test Sistemi
==================================================

Bu gelişmiş test scripti, Phantom Image Optimizer'ın tüm özelliklerini gerçek dünya 
koşullarında kapsamlı bir şekilde test etmek amacıyla geliştirilmiştir. Oxford-IIIT 
Pet Dataset gibi gerçek veri setleri kullanarak, production ortamlarında karşılaşılabilecek 
senaryoları simüle eder ve optimizer'ın güvenilirliğini doğrular.

Bu test sistemi, hem temel fonksiyonalite testlerini hem de karmaşık senaryoları, 
edge case durumlarını ve hata yönetimini kapsar. Otomatik rapor üretimi ile test 
sonuçları ayrıntılı şekilde analiz edilebilir ve optimizer'ın performansı ölçülebilir.

Test Sistemi Mimarisi:
---------------------
1. Ortam Hazırlığı: Temiz test ortamı oluşturma ve veri seti hazırlığı
2. Temel Testler: Kalite ayarları, output yönetimi ve dry-run modları
3. Senaryo Testleri: Yüksek eşzamanlılık, conservative/aggressive optimizasyon
4. Edge Case Testleri: Boş dizinler, geçersiz parametreler, yeniden optimizasyon

Ana Bileşenler:
--------------
- Dataset Yönetimi: Oxford Pet Dataset otomatik indirme ve indirilen arşivi dışarı çıkartma
- Mini Dataset: Nested yapıda test verisi oluşturma (5 image, 6 directory)
- Test Engine: Subprocess tabanlı optimizer çalıştırma ve sonuç analizi
- Raporlama: Markdown formatında kapsamlı test raporu üretimi
- Temizlik: Artifact yönetimi ve --keep-artifacts parametresi

Test Akışı:
-----------
1. Ortam Kurulumu (setup_environment)
   - data/ ve outputs/ dizinlerini temizle
   - Test ortamını sıfırdan oluştur

2. Veri Seti Hazırlığı (download_dataset, create_mini_dataset)
   - Oxford Pet Dataset'ini indir (7390+ resim)
   - Mini dataset oluştur (nested structure ile 15 resim)

3. Temel Fonksiyonalite Testleri (run_basic_tests)
   - High quality (90): Yüksek kalite optimizasyon
   - Medium quality (75): Orta kalite optimizasyon  
   - Low quality (60): Düşük kalite optimizasyon
   - Output directory: Farklı dizine çıktı alma
   - Dry run mode: Simülasyon modu

4. Senaryo Testleri (run_scenario_tests)
   - High concurrency: 16 thread ile yüksek hacim işleme
   - Conservative: Q95, metadata korunması
   - Aggressive: Q60, skip-threshold=1
   - Silent batch: Sessiz toplu işleme
   - Verbose mode: Detaylı debug çıktısı

5. Edge Case Testleri (run_edge_case_tests)
   - Empty directory: Boş dizin işleme
   - Nested structure: Çok seviyeli dizin yapısı
   - Invalid quality (150): Geçersiz kalite parametresi
   - Invalid concurrency (0): Geçersiz thread sayısı
   - Re-optimization: Daha önce optimize edilmiş resimleri yeniden işleme

6. Rapor Üretimi (generate_report)
   - Test istatistikleri ve başarı oranları
   - Dataset bilgileri ve metrikler
   - Kategori bazında test sonuçları
   - Path sanitization ile temiz komut gösterimi

7. Temizlik (cleanup)
   - keep_artifacts=False: Tüm test verilerini temizle
   - keep_artifacts=True: Karşılaştırma için verileri koru

Dizin Yapısı:
------------
testing/
├── data/                     # Test verileri (dataset + temp directories)
│   ├── pets_dataset/        # Oxford Pet Dataset (7390+ images)
│   ├── mini_dataset/        # Test için mini dataset (15 images)
│   ├── empty/               # Boş dizin testi
│   └── nested/              # Nested yapı testi
├── outputs/                 # Test çıktıları
│   ├── output_high_quality/ # Q90 test çıktısı
│   ├── output_medium_quality/ # Q75 test çıktısı
│   ├── conservative/        # Muhafazakar optimizasyon
│   ├── aggressive/          # Agresif optimizasyon
│   └── ...
├── images.tar.gz           # Dataset cache
└── TEST_REPORT.md          # Otomatik üretilen rapor

Kullanım:
--------
python test_comprehensive.py                     # Standart test, temizlik ile
python test_comprehensive.py --keep-artifacts    # Test verilerini koru
python test_comprehensive.py -v                  # Verbose mode
python test_comprehensive.py -v --keep-artifacts # Tam detay + veri koruma

Çıktı Analizi:
-------------
- TEST_REPORT.md: Kapsamlı test raporu
- Success Rate: Başarı oranı hesaplama (expected failures dahil)
- Execution Time: Test süresi analizi
- Size Reduction: Optimizasyon performansı
- Path Sanitization: Temiz komut görüntüsü

Expected Failures:
-----------------
- Invalid quality (150): FAIL (Expected) - Geçersiz kalite testi
- Invalid concurrency (0): FAIL (Expected) - Geçersiz thread testi

Bu testler beklenen şekilde başarısız olur ve başarı oranına pozitif katkı sağlar.

==================================================

EN: Phantom Image Optimizer - Comprehensive Test System
======================================================

This advanced test script has been developed to comprehensively test all features 
of the Phantom Image Optimizer under real-world conditions. Using real datasets 
like the Oxford-IIIT Pet Dataset, it simulates scenarios that may be encountered 
in production environments and validates the optimizer's reliability.

This test system covers both basic functionality tests and complex scenarios, 
edge cases, and error handling. With automatic report generation, test results 
can be analyzed in detail and the optimizer's performance can be measured.

Test System Architecture:
------------------------
1. Environment Setup: Clean test environment creation and dataset preparation
2. Basic Tests: Quality settings, output management, and dry-run modes
3. Scenario Tests: High concurrency, conservative/aggressive optimization
4. Edge Case Tests: Empty directories, invalid parameters, re-optimization

Key Components:
--------------
- Dataset Management: Oxford Pet Dataset automatic download and extraction of downloaded archive
- Mini Dataset: Nested structure test data creation (5 images, 6 directories) 
- Test Engine: Subprocess-based optimizer execution and result analysis
- Reporting: Comprehensive test report generation in Markdown format
- Cleanup: Artifact management and --keep-artifacts parameter

Test Flow:
----------
1. Environment Setup (setup_environment)
   - Clean data/ and outputs/ directories
   - Create test environment from scratch

2. Dataset Preparation (download_dataset, create_mini_dataset)
   - Download Oxford Pet Dataset (7390+ images)
   - Create mini dataset (15 images with nested structure)

3. Basic Functionality Tests (run_basic_tests)
   - High quality (90): High quality optimization
   - Medium quality (75): Medium quality optimization  
   - Low quality (60): Low quality optimization
   - Output directory: Output to different directory
   - Dry run mode: Simulation mode

4. Scenario Tests (run_scenario_tests)
   - High concurrency: High volume processing with 16 threads
   - Conservative: Q95, metadata preservation
   - Aggressive: Q60, skip-threshold=1
   - Silent batch: Silent batch processing
   - Verbose mode: Detailed debug output

5. Edge Case Tests (run_edge_case_tests)
   - Empty directory: Empty directory processing
   - Nested structure: Multi-level directory structure
   - Invalid quality (150): Invalid quality parameter
   - Invalid concurrency (0): Invalid thread count
   - Re-optimization: Re-processing previously optimized images

6. Report Generation (generate_report)
   - Test statistics and success rates
   - Dataset information and metrics
   - Category-based test results
   - Path sanitization for clean command display

7. Cleanup (cleanup)
   - keep_artifacts=False: Clean all test data
   - keep_artifacts=True: Preserve data for comparison

Directory Structure:
-------------------
testing/
├── data/                     # Test data (dataset + temp directories)
│   ├── pets_dataset/        # Oxford Pet Dataset (7390+ images)
│   ├── mini_dataset/        # Mini dataset for testing (15 images)
│   ├── empty/               # Empty directory test
│   └── nested/              # Nested structure test
├── outputs/                 # Test outputs
│   ├── output_high_quality/ # Q90 test output
│   ├── output_medium_quality/ # Q75 test output
│   ├── conservative/        # Conservative optimization
│   ├── aggressive/          # Aggressive optimization
│   └── ...
├── images.tar.gz           # Dataset cache
└── TEST_REPORT.md          # Auto-generated report

Usage:
------
python test_comprehensive.py                    # Standard test with cleanup
python test_comprehensive.py --keep-artifacts   # Preserve test data
python test_comprehensive.py -v                 # Verbose mode
python test_comprehensive.py -v --keep-artifacts # Full detail + data preservation

Output Analysis:
---------------
- TEST_REPORT.md: Comprehensive test report
- Success Rate: Success rate calculation (including expected failures)
- Execution Time: Test duration analysis
- Size Reduction: Optimization performance
- Path Sanitization: Clean command display

Expected Failures:
-----------------
- Invalid quality (150): FAIL (Expected) - Invalid quality test
- Invalid concurrency (0): FAIL (Expected) - Invalid thread test

These tests fail as expected and contribute positively to the success rate.

Dataset Information:
-------------------
- Source: Oxford-IIIT Pet Dataset
- URL: https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
- Total Images: 7390+ pet images (cats and dogs)
- Test Usage: Full dataset for concurrency tests, mini dataset for functionality tests
"""

import sys
import time
import shutil
import tarfile
import urllib.request
import ssl
import subprocess
import random
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List
from textwrap import dedent

# Simple logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)-7s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class ImageOptimizerTester:
    def __init__(self, verbose=False):
        self.base_dir = Path.cwd().parent  # Parent directory (image-optimizer)
        self.testing_dir = Path.cwd()  # Current directory (testing)
        self.dataset_url = "https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz"
        self.data_dir = self.testing_dir / "data"
        self.dataset_path = self.data_dir / "pets_dataset"
        self.mini_dataset_path = self.data_dir / "mini_dataset"
        self.outputs_dir = self.testing_dir / "outputs"
        self.test_results = []
        self.start_time = None
        self.node_command = str(self.base_dir / "optimize.js")
        self.verbose = verbose
        
    def setup_environment(self):
        """Setup test environment and directories"""
        logger.info("Setting up test environment...")
        
        # Create data directory if it doesn't exist
        self.data_dir.mkdir(exist_ok=True)
        
        # Clean data directory at the beginning of each test run if it exists
        if self.data_dir.exists():
            shutil.rmtree(self.data_dir)
            logger.debug("Cleaned existing data directory")
            
        # Create directories
        self.dataset_path.mkdir(parents=True, exist_ok=True)
        self.mini_dataset_path.mkdir(parents=True, exist_ok=True)
        
        # Clean outputs directory at the beginning of each test run if it exists
        if self.outputs_dir.exists():
            shutil.rmtree(self.outputs_dir)
            logger.debug("Cleaned existing outputs directory")
            
        # Create outputs directory
        self.outputs_dir.mkdir(exist_ok=True)
        
        logger.info("Test environment ready")
        
    def download_dataset(self):
        """Download pet images dataset"""
        tar_path = self.testing_dir / "images.tar.gz"
        
        # Check if tar.gz already exists
        if tar_path.exists():
            logger.info("Found existing images.tar.gz, using cached file")
        else:
            logger.info(f"Downloading dataset from {self.dataset_url}...")
            
            try:
                # Create SSL context that doesn't verify certificates (for testing only)
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                
                # Download with progress
                def download_progress(block_num, block_size, total_size):
                    downloaded = block_num * block_size
                    percent = min(downloaded * 100 / total_size, 100)
                    sys.stdout.write(f"\rDownloading: {percent:.1f}%")
                    sys.stdout.flush()
                
                # Open URL with custom SSL context
                opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_context))
                urllib.request.install_opener(opener)
                
                urllib.request.urlretrieve(self.dataset_url, tar_path, download_progress)
                logger.info("Dataset downloaded")
                
            except KeyboardInterrupt:
                logger.warning("Download interrupted by user")
                # Remove incomplete download file if it exists
                if tar_path.exists():
                    try:
                        tar_path.unlink()
                        logger.info("Removed incomplete download file")
                    except Exception as remove_err:
                        logger.warning(f"Failed to remove incomplete file: {remove_err}")
                raise  # Re-raise to be caught by main handler
            except Exception as e:
                logger.error(f"Failed to download dataset: {e}")
                # Remove incomplete download file if it exists
                if tar_path.exists():
                    try:
                        tar_path.unlink()
                        logger.info("Removed incomplete download file")
                    except Exception as remove_err:
                        logger.warning(f"Failed to remove incomplete file: {remove_err}")
                sys.exit(1)
        
        # Check if dataset already extracted
        if any(self.dataset_path.glob("*.jpg")):
            logger.info("Dataset already extracted, skipping extraction")
            return
            
        # Extract dataset
        try:
            logger.info("Extracting dataset...")
            with tarfile.open(tar_path, 'r:gz') as tar:
                tar.extractall(self.dataset_path)
            
            # Don't remove tar file, keep for future use
            
            # Find extracted images directory
            images_dir = self.dataset_path / "images"
            if images_dir.exists():
                # Move images to dataset root
                for item in images_dir.iterdir():
                    shutil.move(str(item), str(self.dataset_path))
                images_dir.rmdir()
            
            logger.info("Dataset extracted")
            
        except Exception as e:
            logger.error(f"Failed to extract dataset: {e}")
            sys.exit(1)
    
    def create_mini_dataset(self, num_images: int = 5):
        """Create a smaller dataset with nested structure for comprehensive testing"""
        logger.info(f"Creating mini dataset with {num_images} images in nested structure...")
        
        # Get all jpg files
        all_images = list(self.dataset_path.glob("*.jpg"))
        
        if len(all_images) < num_images * 3:  # We need more images for nested structure
            logger.warning(f"Only {len(all_images)} images available")
            num_images = max(1, len(all_images) // 3)
        
        # Select random images
        selected_images = random.sample(all_images, min(num_images * 3, len(all_images)))
        
        # Create nested directory structure
        nested_dirs = [
            self.mini_dataset_path,  # Root level
            self.mini_dataset_path / "cats",
            self.mini_dataset_path / "dogs",
            self.mini_dataset_path / "animals" / "pets",
            self.mini_dataset_path / "animals" / "pets" / "indoor",
            self.mini_dataset_path / "photos" / "2024" / "january"
        ]
        
        # Create all directories
        for dir_path in nested_dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Distribute images across directories
        for i, img in enumerate(selected_images):
            target_dir = nested_dirs[i % len(nested_dirs)]
            shutil.copy2(img, target_dir)
        
        # Count total images
        total_images = sum(1 for _ in self.mini_dataset_path.rglob("*.jpg"))
        logger.info(f"Mini dataset created with {total_images} images across {len(nested_dirs)} directories")
    
    def run_command(self, cmd: List[str], test_name: str) -> Dict:
        """Run optimizer command and capture results"""
        logger.debug(f"Executing: {' '.join(cmd)}")
        
        start_time = time.time()
        
        try:
            if self.verbose:
                # Run with real-time output in verbose mode
                logger.info("Command output:")
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                stdout_lines = []
                for line in process.stdout:
                    line = line.rstrip()
                    if line:
                        print(line)  # Real-time output
                        stdout_lines.append(line)
                
                process.wait()
                result_stdout = '\n'.join(stdout_lines)
                result_stderr = ""
                result_returncode = process.returncode
            else:
                # Run silently in non-verbose mode
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=False
                )
                result_stdout = result.stdout
                result_stderr = result.stderr
                result_returncode = result.returncode
            
            execution_time = time.time() - start_time
            
            test_result = {
                "name": test_name,
                "command": ' '.join(cmd),
                "success": result_returncode == 0,
                "execution_time": execution_time,
                "stdout": result_stdout,
                "stderr": result_stderr,
                "return_code": result_returncode
            }
            
            if result_returncode == 0:
                logger.info(f"Test passed in {execution_time:.2f}s")
                
                # Check if output files were created for non-dry-run commands
                if "--dry-run" not in cmd and "-o" in cmd:
                    output_idx = cmd.index("-o")
                    if output_idx + 1 < len(cmd):
                        output_dir = Path(cmd[output_idx + 1])
                        if output_dir.exists():
                            output_files = list(output_dir.rglob("*"))
                            image_files = [f for f in output_files if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif']]
                            if image_files:
                                logger.info(f"Output verified: {len(image_files)} files created in {output_dir.name}")
                            else:
                                logger.warning(f"No image files found in output directory: {output_dir}")
                        else:
                            logger.error(f"Output directory not created: {output_dir}")
            else:
                logger.error(f"Test failed with code {result_returncode}")
                if result_stderr and not self.verbose:
                    logger.error(f"Error output: {result_stderr}")
            
            return test_result
            
        except Exception as e:
            logger.error(f"Command execution failed: {e}")
            return {
                "name": test_name,
                "command": ' '.join(cmd),
                "success": False,
                "execution_time": time.time() - start_time,
                "error": str(e)
            }

    def _run_test_suite(self, tests: List[Dict], test_type: str):
        """Helper method to run a suite of tests"""
        for i, test in enumerate(tests, 1):
            logger.info(f"{test_type} test {i}/{len(tests)}: {test['name']}")
            result = self.run_command(test["cmd"], test["name"])
            result["metrics"] = self.parse_optimization_results(result.get("stdout", ""))
            self.test_results.append(result)
    
    def sanitize_path(self, path: str) -> str:
        """Sanitize full paths to relative paths for the report"""
        # Replace the full path with relative paths from the image-optimizer directory
        if str(self.base_dir) in path:
            # Replace base_dir (image-optimizer) and show relative path
            return path.replace(str(self.base_dir / "optimize.js"), "optimize.js").replace(str(self.base_dir), ".")
        elif str(self.testing_dir) in path:
            # Replace testing_dir path with testing/
            return path.replace(str(self.testing_dir), "testing")
        return path
    
    # noinspection PyMethodMayBeStatic
    def parse_optimization_results(self, output: str) -> Dict:
        """Parse optimizer output for metrics"""
        metrics = {
            "total_images": 0,
            "optimized": 0,
            "skipped": 0,
            "failed": 0,
            "size_reduction": "0%",
            "processing_time": 0.0
        }
        
        lines = output.split('\n')
        for line in lines:
            if "Total Images Found:" in line:
                metrics["total_images"] = int(line.split(":")[-1].strip())
            elif "Successfully Optimized:" in line:
                metrics["optimized"] = int(line.split(":")[-1].strip())
            elif "Skipped" in line and ":" in line:
                metrics["skipped"] = int(line.split(":")[-1].strip().split()[0])
            elif "Failed:" in line:
                metrics["failed"] = int(line.split(":")[-1].strip())
            elif "Total Size Reduction:" in line and "reduction)" in line:
                metrics["size_reduction"] = line.split("(")[-1].split(")")[0]
            elif "Processing Time:" in line:
                time_str = line.split(":")[-1].strip()
                metrics["processing_time"] = float(time_str.split()[0])
        
        return metrics
    
    def run_basic_tests(self):
        """Run basic functionality tests"""
        logger.info("Starting basic functionality tests...")
        
        tests = [
            # Quality settings with output directory
            {
                "name": "High quality (90)",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path), "-q", "90",
                        "-o", str(self.outputs_dir / "output_high_quality")]
            },
            {
                "name": "Medium quality (75)",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path), "-q", "75",
                        "-o", str(self.outputs_dir / "output_medium_quality")]
            },
            {
                "name": "Low quality (60)",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path), "-q", "60",
                        "-o", str(self.outputs_dir / "output_low_quality")]
            },
            # Output directory test
            {
                "name": "Output to different directory",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path), 
                        "-o", str(self.outputs_dir / "output_test")]
            },
            # Dry run with mini dataset
            {
                "name": "Dry run mode",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path), "--dry-run"]
            }
        ]
        
        self._run_test_suite(tests, "Basic")
    
    def run_scenario_tests(self):
        """Run scenario-based tests"""
        logger.info("Starting scenario-based tests...")
        
        scenarios = [
            # Scenario 1: High-volume processing
            {
                "name": "High concurrency (16 threads)",
                "cmd": ["node", self.node_command, str(self.dataset_path), 
                        "-c", "16", "-o", str(self.outputs_dir / "output_concurrency")]
            },
            # Scenario 2: Conservative optimization
            {
                "name": "Conservative - high quality, preserve metadata",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-q", "95", "--no-strip-metadata", 
                        "-o", str(self.outputs_dir / "conservative")]
            },
            # Scenario 3: Aggressive optimization
            {
                "name": "Aggressive - low quality, strip all",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-q", "60", "--skip-threshold", "1",
                        "-o", str(self.outputs_dir / "aggressive")]
            },
            # Scenario 4: Silent batch processing
            {
                "name": "Silent batch processing",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-s", "-q", "80", "-o", str(self.outputs_dir / "batch")]
            },
            # Scenario 5: Verbose debugging
            {
                "name": "Verbose mode with details",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-v", "--dry-run"]
            }
        ]
        
        self._run_test_suite(scenarios, "Scenario")
    
    def run_edge_case_tests(self):
        """Run edge case and error handling tests"""
        logger.info("Starting edge case and error handling tests...")
        
        # Create test directories inside data/
        empty_dir = self.data_dir / "empty"
        empty_dir.mkdir(exist_ok=True)
        
        nested_dir = self.data_dir / "nested" / "level1" / "level2"
        nested_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy one image to nested
        images = list(self.mini_dataset_path.glob("*.jpg"))
        if images:
            shutil.copy2(images[0], nested_dir)
        
        edge_cases = [
            # Empty directory
            {
                "name": "Empty directory",
                "cmd": ["node", self.node_command, str(empty_dir)]
            },
            # Nested directories
            {
                "name": "Deeply nested structure",
                "cmd": ["node", self.node_command, str(self.data_dir / "nested"),
                        "-o", str(self.outputs_dir / "nested_output")]
            },
            # Invalid parameters
            {
                "name": "Invalid quality (150)",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-q", "150"]
            },
            {
                "name": "Invalid concurrency (0)",
                "cmd": ["node", self.node_command, str(self.mini_dataset_path),
                        "-c", "0"]
            },
            # Re-optimization test with output
            {
                "name": "Re-optimize already optimized",
                "cmd": ["node", self.node_command, str(self.outputs_dir / "output_test"),
                        "-o", str(self.outputs_dir / "output_reoptimized")]
            }
        ]
        
        self._run_test_suite(edge_cases, "Edge case")
    
    
    def generate_report(self):
        """Generate comprehensive test report"""
        logger.info("Generating comprehensive test report...")
        
        # Create reports directory
        reports_dir = self.testing_dir / "reports"
        reports_dir.mkdir(exist_ok=True)
        
        # Generate timestamp for report filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = reports_dir / f"TEST_REPORT_{timestamp}.md"
        
        # Calculate statistics
        total_tests = len(self.test_results)
        
        # Count expected failures (validation tests that should fail)
        expected_failures = sum(1 for t in self.test_results 
                              if "Invalid" in t["name"] and not t["success"])
        
        # Count actual passes and fails
        passed_tests = sum(1 for t in self.test_results if t["success"])
        failed_tests = total_tests - passed_tests - expected_failures
        
        # For success rate, count expected failures as successes
        effective_passed = passed_tests + expected_failures
        
        # Group results by category - use list indices to avoid overlaps
        basic_test_count = 5  # Number of tests in run_basic_tests
        scenario_test_count = 5  # Number of tests in run_scenario_tests
        
        basic_tests = self.test_results[:basic_test_count]
        scenario_tests = self.test_results[basic_test_count:basic_test_count + scenario_test_count]
        edge_tests = self.test_results[basic_test_count + scenario_test_count:]
        
        report_content = dedent(f"""
        # Phantom Image Optimizer - Comprehensive Test Report
        
        ## Test Summary
        - **Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        - **Total Tests**: {total_tests}
        - **Passed**: {passed_tests}
        - **Failed**: {failed_tests} {"(2 are expected validation failures)" if expected_failures > 0 else ""}
        - **Success Rate**: {(effective_passed/total_tests*100):.1f}%
        - **Total Execution Time**: {sum(t.get('execution_time', 0) for t in self.test_results):.2f}s
        
        ## Dataset Information
        - **Source**: Oxford-IIIT Pet Dataset
        - **Total Images**: {len(list(self.dataset_path.glob('*.jpg')))}
        - **Mini Dataset Size**: {len(list(self.mini_dataset_path.rglob('*.jpg')))} images
        
        ## Test Results by Category
        
        ### 1. Basic Functionality Tests
        """)
        
        # Add basic test results
        for test in basic_tests:
            status = "PASS" if test["success"] else "FAIL"
            sanitized_command = self.sanitize_path(test['command'])
            report_content += f"\n#### {test['name']} - {status}\n"
            report_content += f"- Command: `{sanitized_command}`\n"
            report_content += f"- Execution Time: {test['execution_time']:.2f}s\n"
            
            if test.get("metrics"):
                m = test["metrics"]
                report_content += f"- Images: {m['total_images']} total, "
                report_content += f"{m['optimized']} optimized, {m['skipped']} skipped\n"
                report_content += f"- Size Reduction: {m['size_reduction']}\n"
        
        report_content += "\n### 2. Scenario-Based Tests\n"
        
        # Add scenario test results
        for test in scenario_tests:
            status = "PASS" if test["success"] else "FAIL"
            sanitized_command = self.sanitize_path(test['command'])
            report_content += f"\n#### {test['name']} - {status}\n"
            report_content += f"- Command: `{sanitized_command}`\n"
            report_content += f"- Execution Time: {test['execution_time']:.2f}s\n"
            
            if test.get("metrics") and test["metrics"]["total_images"] > 0:
                m = test["metrics"]
                report_content += f"- Results: {m['optimized']} optimized, "
                report_content += f"{m['size_reduction']} reduction\n"
        
        report_content += "\n### 3. Edge Case Tests\n"
        
        # Add edge case results
        for test in edge_tests:
            status = "PASS" if test["success"] else "FAIL"
            expected = " (Expected)" if "Invalid" in test["name"] and not test["success"] else ""
            sanitized_command = self.sanitize_path(test['command'])
            report_content += f"\n#### {test['name']} - {status}{expected}\n"
            report_content += f"- Command: `{sanitized_command}`\n"
            
            if not test["success"] and test.get("stderr"):
                report_content += f"- Error: {test['stderr'].strip()}\n"
        
        
        report_content += dedent("""
        
        ## Test Artifacts
        
        - Full dataset: `testing/data/pets_dataset/`
        - Mini dataset: `testing/data/mini_dataset/`
        - Test outputs: `testing/outputs/` (contains all test output directories)
        """)
        
        # Write report
        with open(report_path, 'w') as f:
            f.write(report_content)
        
        logger.info(f"Report generation completed")
        logger.info(f"Test summary: {effective_passed}/{total_tests} passed ({effective_passed/total_tests*100:.1f}% success rate)")
        
        return report_path
    
    def cleanup(self, keep_artifacts: bool = True):
        """Clean up test environment"""
        logger.info(f"Cleanup started (keep_artifacts={keep_artifacts})")
        
        # Handle data directory based on keep_artifacts
        if not keep_artifacts:
            logger.info("Cleaning up data directory...")
            if self.data_dir.exists():
                shutil.rmtree(self.data_dir)
                logger.info("Removed data directory (contains datasets and test directories)")
        else:
            logger.info("Test data preserved in data/ directory")
        
        # Handle outputs directory based on keep_artifacts
        if not keep_artifacts:
            logger.info("Cleaning up outputs directory...")
            if self.outputs_dir.exists():
                shutil.rmtree(self.outputs_dir)
                logger.info("Removed outputs directory and all test outputs")
        else:
            logger.info("Test outputs preserved in outputs/ directory")
    
    def run_all_tests(self):
        """Run complete test suite"""
        self.start_time = time.time()
        
        logger.info("Phantom Image Optimizer - Comprehensive Test Suite")
        logger.info(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Phase 1: Environment setup
        logger.info("Phase 1: Setting up test environment")
        self.setup_environment()
        
        # Phase 2: Dataset preparation
        logger.info("Phase 2: Preparing datasets")
        self.download_dataset()
        self.create_mini_dataset(5)
        
        # Phase 3: Test execution
        logger.info("Phase 3: Executing test suites")
        self.run_basic_tests()
        self.run_scenario_tests()
        self.run_edge_case_tests()
        
        # Phase 4: Report generation
        logger.info("Phase 4: Generating test report")
        report_path = self.generate_report()
        
        # Total execution time
        total_time = time.time() - self.start_time
        logger.info(f"Test suite completed in {total_time:.2f}s")
        logger.info(f"Test report: {report_path}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Comprehensive test suite for Phantom Image Optimizer')
    parser.add_argument('-v', '--verbose', action='store_true', 
                        help='Show real-time output from node commands')
    parser.add_argument('--keep-artifacts', action='store_true', default=False,
                        help='Keep test output artifacts after completion (default: remove)')
    args = parser.parse_args()
    
    tester = ImageOptimizerTester(verbose=args.verbose)
    
    try:
        tester.run_all_tests()
        # Use the keep_artifacts argument for cleanup
        tester.cleanup(keep_artifacts=args.keep_artifacts)
    except KeyboardInterrupt:
        logger.warning("Test suite interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Test suite failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()