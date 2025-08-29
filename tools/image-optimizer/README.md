# Phantom Image Optimizer

Standalone image optimization tool for Phantom Documentation Kit. This tool is completely independent from the main project structure and can be used to optimize images in any directory.

## Features

- Recursive directory scanning - processes all subdirectories
- Parallel processing - utilizes all CPU cores
- Multiple format support: JPEG, PNG, WebP, GIF, AVIF
- Smart optimization with configurable quality settings
- Detailed text-based reporting with size reduction details
- Error tolerance - continues processing even if some files fail
- Dry-run mode for testing
- Metadata stripping
- Skip already optimized images
- Output directory support with preserved structure

## Installation

```bash
cd tools/image-optimizer
npm install
```

## Usage

### Basic Usage

```bash
node tools/image-optimizer/optimize.js ./path/to/images
```

### Advanced Options

```bash
# Set custom quality
node tools/image-optimizer/optimize.js ./images --quality 90

# Dry run - see what would be optimized without making changes
node tools/image-optimizer/optimize.js ./images --dry-run

# Process specific formats only
node tools/image-optimizer/optimize.js ./images --formats jpeg,png

# Verbose output
node tools/image-optimizer/optimize.js ./images --verbose

# Custom concurrency
node tools/image-optimizer/optimize.js ./images --concurrency 4

# Keep metadata
node tools/image-optimizer/optimize.js ./images --no-strip-metadata

# Skip images with less than 10% reduction potential
node tools/image-optimizer/optimize.js ./images --skip-threshold 10

# Save optimized images to a different directory (preserves directory structure)
node tools/image-optimizer/optimize.js ./images --output ./optimized-images

# Combine multiple options
node tools/image-optimizer/optimize.js ./images -o ./output -q 85 -f jpeg,png --dry-run
```

## Options

- `-V, --version` - Output the version number
- `-q, --quality <number>` - JPEG/WebP quality (0-100, default: 85)
- `-f, --formats <formats>` - Comma-separated list of formats to process (jpeg,png,webp,gif,avif)
- `-c, --concurrency <number>` - Number of images to process in parallel (default: CPU core count)
- `-o, --output <directory>` - Output directory for optimized images (preserves originals and directory structure)
- `--dry-run` - Show what would be optimized without making changes
- `-v, --verbose` - Show detailed output
- `-s, --silent` - Suppress all output except errors
- `--no-strip-metadata` - Keep image metadata (default: strip metadata)
- `--skip-threshold <percent>` - Skip if reduction is less than this percentage (default: 5%)
- `-h, --help` - Display help for command

## Output Format

The tool provides detailed text-based reporting:

```
Image Optimization Report
================================================================

Scanned Directory: ./testing/data/pets_dataset
Output Directory: ./testing/outputs/output_basic
Date: 2025-01-04 18:30:45

Summary:
----------------------------------------------------------------
Total Images Found: 100
Successfully Optimized: 100
Skipped (already optimized): 0
Failed: 0

Total Size Reduction: 12.5 MB -> 7.3 MB (41.6% reduction)
Processing Time: 4.2 seconds

Detailed Results:
----------------------------------------------------------------
[SUCCESS] beagle_1.jpg
   Original: 125.4 KB -> Optimized: 73.2 KB (41.6% reduction)
   
[SUCCESS] bulldog_2.jpg
   Original: 98.7 KB -> Optimized: 57.5 KB (41.7% reduction)
   
[SUCCESS] persian_cat_3.jpg
   Original: 145.2 KB -> Optimized: 84.8 KB (41.6% reduction)
   
... (97 more files)
```

## Testing

The `testing/` directory contains a comprehensive test suite for validating the image optimizer functionality. The test suite uses the [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/) for testing real-world image optimization scenarios.

**Dataset Citation**: O. M. Parkhi, A. Vedaldi, A. Zisserman, C. V. Jawahar, "Cats and Dogs", IEEE Conference on Computer Vision and Pattern Recognition, 2012

### Directory Structure

```
testing/
├── data/                      # Test datasets (created during test runs)
│   ├── pets_dataset/         # Main test dataset (100 images)
│   ├── mini_dataset/         # Small dataset (15 images in nested dirs)
│   ├── empty/                # Empty directory for edge case testing
│   └── nested/               # Deeply nested directory structure
├── outputs/                   # Test output files (created during test runs)
├── reports/                   # Test reports with timestamps
│   └── TEST_REPORT_YYYYMMDD_HHMMSS.md
└── test_comprehensive.py      # Main test script
```

### Running Tests

```bash
# Run comprehensive test suite
cd testing
python test_comprehensive.py

# Keep test artifacts after completion
python test_comprehensive.py --keep-artifacts
```

### Test Categories

The test suite includes three categories of tests:

1. **Basic Tests**
   - Basic optimization
   - High quality (90%)
   - Low quality (50%)
   - Specific format processing (JPEG only)
   - Output directory functionality

2. **Scenario Tests**
   - High concurrency (16 threads)
   - Silent mode
   - Verbose mode
   - Skip threshold testing
   - Metadata preservation

3. **Edge Case Tests**
   - Empty directory handling
   - Nested directory processing
   - Non-existent directory (error handling)
   - Invalid quality validation (expected failure)
   - Invalid concurrency validation (expected failure)

### Test Features

- **Automatic Dataset Download**: Downloads and caches a real-world image dataset
- **Organized Output**: All test outputs are stored in `outputs/` directory
- **Timestamped Reports**: Test reports are saved as `TEST_REPORT_YYYYMMDD_HHMMSS.md`

### Example Test Report

```markdown
# Phantom Image Optimizer - Comprehensive Test Report

## Test Summary
- **Date**: 2025-08-04 15:25:02
- **Total Tests**: 15
- **Passed**: 13
- **Failed**: 0 (2 are expected validation failures)
- **Success Rate**: 100.0%
- **Total Execution Time**: 45.30s

## Dataset Information
- **Source**: [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
- **Total Images**: 7390
- **Mini Dataset Size**: 15 images
- **Citation**: O. M. Parkhi, A. Vedaldi, A. Zisserman, C. V. Jawahar
  "Cats and Dogs"
  IEEE Conference on Computer Vision and Pattern Recognition, 2012

## Test Results by Category

### 1. Basic Functionality Tests

#### High quality (90) - PASS
- Command: `node optimize.js testing/data/mini_dataset -q 90 -o testing/outputs/output_high_quality`
- Execution Time: 0.29s
- Images: 15 total, 14 optimized, 1 skipped
- Size Reduction: 62.3% reduction

#### Medium quality (75) - PASS
- Command: `node optimize.js testing/data/mini_dataset -q 75 -o testing/outputs/output_medium_quality`
- Execution Time: 0.18s
- Images: 15 total, 15 optimized, 0 skipped
- Size Reduction: 78.9% reduction

### 2. Scenario-Based Tests

#### High concurrency (16 threads) - PASS
- Command: `node optimize.js testing/data/pets_dataset -c 16 -o testing/outputs/output_concurrency`
- Execution Time: 42.68s
- Results: 6578 optimized, 68.2% reduction

### 3. Edge Case Tests

#### Invalid quality (150) - FAIL (Expected)
- Command: `node optimize.js testing/data/mini_dataset -q 150`

#### Invalid concurrency (0) - FAIL (Expected)
- Command: `node optimize.js testing/data/mini_dataset -c 0`
```

## Notes

- This tool modifies images in-place by default (use `--output` to preserve originals)
- Always backup your images before running optimization
- Use dry-run mode to preview changes first
- When using `--output`, the directory structure of the source is preserved
- When using `--output`, skipped files are copied to maintain a complete set
- The tool is completely independent from the main Phantom Documentation Kit