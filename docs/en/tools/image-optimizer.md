---
extra_javascript:
  - assets/javascripts/asciinema-player.js
---

# Phantom Image Optimizer

## :fontawesome-solid-wrench: What Does This Tool Do?

**Phantom Image Optimizer** is the standalone image optimization tool of Phantom Documentation Kit.

### Main Purpose
Developed for optimizing images used in documentation projects. 
Large-sized images cause documentation pages to load slowly. 
This tool significantly reduces file sizes while preserving image quality.

### Powerful Infrastructure

Leverages the industrial power of the **Sharp** library. This provides:

  - Documentation images
  - Website photographs  
  - Images used in blog content
  - E-commerce product images
  - All images requiring optimization in your digital projects

professional-level optimization.

---

## :fontawesome-solid-rocket: Let's Get Started! 

### Step 1: Installation 

#### System Requirements

##### :fontawesome-brands-node-js: Node.js Version
- **Minimum Node.js version: 22.x or higher** required
- To check your Node.js version: `node --version`
- To download the appropriate Node.js version: [https://nodejs.org/en/download](https://nodejs.org/en/download)

##### :fontawesome-brands-apple: macOS System Packages

The following packages must be installed for the Sharp library to work properly:

You can easily install the required packages with Homebrew.
```bash
brew install vips pkg-config
```
```bash
brew install libjpeg libpng webp giflib libtiff
```

##### :fontawesome-brands-linux: Linux System Packages

**For Ubuntu/Debian based systems:**
```bash
sudo apt-get update && sudo apt-get install -y \
    libvips42 libvips-dev \
    libjpeg-dev libpng-dev libwebp-dev \
    libgif-dev libtiff-dev \
    pkg-config build-essential
```

**For RHEL/CentOS/Fedora based systems:**
```bash
sudo yum install -y \
    vips vips-devel \
    libjpeg-turbo-devel libpng-devel libwebp-devel \
    giflib-devel libtiff-devel \
    pkgconfig gcc-c++ make
```

##### :fontawesome-brands-docker: Phantom Documentation Kit Docker Mode

Phantom Documentation Kit includes the necessary tools and Node version to run this tool in the Docker image by default. 
After running `serve` in Docker mode, you can follow the installation steps inside the running container 
to run the tool. 

Note that you need to follow the installation steps for this tool again each time you run `serve`.


#### Package Installation

Open the terminal and navigate to the project directory, then navigate to the Phantom Image Optimizer directory by typing:

```bash
cd tools/image-optimizer
```

Install the required npm packages with the following command:

```bash
npm install
```

If you want to use it globally, apply the following command.

```bash
npm link
```

Then you can run it anywhere directly with the `phantom-optimize` command.

```bash
phantom-optimize ./images
```

### Step 2: Our First Optimization!

#### :fontawesome-solid-star: Simplest Usage

Optimize the images in the 'images' directory with the following command:

```bash
node optimize.js ../../docs/assets/static/images
```

If you wish, you can save the optimized images to a different directory while preserving the originals.
```bash
node optimize.js \
         ../../docs/assets/static/images \
         --output ../../docs/assets/static/optimized_images
```

---

## :fontawesome-solid-lightbulb: Quick Tips 

### If You Say "My Files Are Too Large":
```bash
node optimize.js ./photos --quality 60
```

###  If You Say "I Don't Want to Lose the Originals":
```bash
node optimize.js ./original-photos --output ./optimized
```

###  If You Say "I Want to Test First":
```bash
node optimize.js ./photos --dry-run
```

###  If You Say "Only Optimize JPEGs":
```bash
node optimize.js ./photos --formats jpeg
```

---

## :fontawesome-solid-dice: Practical Experiments

### Speed Test
Process 4 files simultaneously (turbo mode!)
```bash
node optimize.js ./photos --concurrency 4
```

### Detailed Information
Tell me everything!
```bash
node optimize.js ./photos --verbose
```

### Silent Mode
Only show errors, ignore the rest
```bash
node optimize.js ./photos --silent
```

---

## :fontawesome-solid-flask: Our Real Test Results

### How Does Our Test System Work?

**Simple Explanation:** A test script was written that comprehensively tests all features of Phantom Image Optimizer 
under real-world conditions.

### Would You Like to Run the Test Script?
Make sure you are in the `tools/image-optimizer` directory and navigate to the 'testing' folder where the test script is located:
```bash
cd testing
```
There are different ways to run the test script, you can test it by running it as you wish. 
If you want, you can save the results at the end of the tests to compare both the report and the images 
for comparison.

Run the test script:
```bash
python test_comprehensive.py
```
For more detailed error tracking and outputs:
```bash
python test_comprehensive.py --verbose
```
If you want to keep test results for comparison:
```bash
python test_comprehensive.py --keep-artifacts
```

### What Exactly Does the Test Do?

1. **:fontawesome-solid-download: First downloads photos** - 7390 cat-dog photos from Oxford University
2. **:fontawesome-solid-microscope: Performs 15 different tests** - Tests critical situations according to real user usage
3. **:fontawesome-solid-file-lines: Writes report** - Saves results to report file
4. **:fontawesome-solid-broom: Cleans up** - Optionally deletes test files, or keeps them for comparison

###  Why Oxford Pet Dataset?

**Let's be frank:** Real photos were needed for testing. Oxford University's cat-dog photos were chosen because:

-  **Always accessible** - An academic study, link is always accessible
-  **Real photos** - Images selected from real life for an academic study
-  **7390 photos** - Both quick test (15 of them) and large test (all) can be done
-  **Everyone can use** - Open source, free, for scientific purposes

This makes the tests realistic and results can be easily compared!

### Real Test Results

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python test_comprehensive.py --verbose</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Image Optimizer</h3>
        <span class="asciinema-player-info">Test Terminal Recording</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/tests/tools/image-optimizer/test_comprehensive_20250807_092345.cast"
             data-cols="120"
             data-rows="40"
             data-autoplay="false"
             data-loop="false"
             data-speed="1.5"
             data-theme="solarized-dark"
             data-font-size="small">
        </div>
    </div>
</div>

If you want to see the comprehensive and raw outputs of the real test results, you can check the files at the following 
file locations.

- `testing/reports/TEST_REPORT_20250807_092504.md`
- `testing/recordings/test_comprehensive_20250807_092345.cast`

#### High Quality Optimization (Quality 90)

**Command:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 90 \
         --output ./testing/outputs/output_high_quality</span>
</div>

**Real Results:**
```
15 images processed
Processing time: 0.35 seconds
Total size: 1.29MB → 562.3KB (57.3% reduction)

Sample files:
├── scottish_terrier_43.jpg: 172.93KB → 83.38KB (51.8% reduced)
├── shiba_inu_95.jpg: 140.04KB → 55.78KB (60.2% reduced)
├── pomeranian_38.jpg: 133.27KB → 41.2KB (69.1% reduced)
└── Birman_134.jpg: 103.85KB → 34.48KB (66.8% reduced)
```

#### Medium Quality Optimization (Quality 75)

**Command:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 75 \
         --output ./testing/outputs/output_medium_quality</span>
</div>

**Real Results:**
```
15 images processed
Processing time: 0.29 seconds
Total size: 1.29MB → 312.3KB (76.3% reduction)

Sample files:
├── scottish_terrier_43.jpg: 172.93KB → 48.66KB (71.9% reduced)
├── pomeranian_38.jpg: 133.27KB → 18.81KB (85.9% reduced!)
└── Birman_134.jpg: 103.85KB → 15.34KB (85.2% reduced!)
```

#### Aggressive Optimization (Quality 60)

**Command:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 60 \
         --output ./testing/outputs/output_low_quality</span>
</div>

**Real Results:**
```
15 images processed
Processing time: 0.22 seconds
Total size: 1.29MB → 220.17KB (83.3% reduction!)

Sample files:
├── pomeranian_38.jpg: 133.27KB → 12.43KB (90.7% reduced!!)
├── Birman_134.jpg: 103.85KB → 10.22KB (90.2% reduced!!)
└── British_Shorthair_60.jpg: 101.52KB → 14.48KB (85.7% reduced!)
```

---

## :fontawesome-solid-rocket: Practical Usage Table

| What I Want         | Copy Command                               |
|---------------------|--------------------------------------------|
| Simplest Usage      | `node optimize.js ./photos`                |
| High Quality        | `node optimize.js ./photos -q 90`          |
| Fast and Small      | `node optimize.js ./photos -q 60`          |
| Safe Test           | `node optimize.js ./photos --dry-run`      |
| Backup and Optimize | `node optimize.js ./photos -o ./optimized` |
| Only JPEG           | `node optimize.js ./photos -f jpeg`        |
| Turbo Mode          | `node optimize.js ./photos -c 8`           |
| Work Silently       | `node optimize.js ./photos --silent`       |