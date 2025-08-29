---
extra_javascript:
  - assets/javascripts/asciinema-player.js

---
# Phantom Documentation Kit

This kit was developed to provide an easy and unique documentation experience for the `Phantom Wireguard` software documentation process.
When the industrial power and flexibility of the MkDocs library met our needs, the `Phantom Documentation Kit` was born.
The features and components we needed in the documentation process were developed and gathered under this framework.


## Quick Start

### Prerequisites

#### Python Packages
Install the required Python packages by running the following command in the project directory:

```bash
pip install -r requirements.txt
```

#### Node.js Installation
The `Vendor Builder` and `Image Optimizer` tools in Phantom Documentation Kit require
**Node.js 22 or higher**. For more detailed information about these tools,
you can refer to the [Tools](./tools/index.md) documentation.

- Check your current version: `node --version`
- Download Node.js: [https://nodejs.org/en/download](https://nodejs.org/en/download)

### 1. Development Server (serve.py)

To view and develop your documentation locally:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py</span>
</div>

Open http://localhost:8000 in your browser.

### 2. Building Documentation (build.py)

To generate production-ready static HTML:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py</span>
</div>

The compiled files are created in the `outputs/site/` directory.

## Configuration (config.json)

Edit the `config.json` file to customize project settings:

```json
{
  "paths": {
    "output_dir": "outputs/www",
    "vendor_dir": "overrides/assets/vendor",
    "vendor_builder_dir": "tools/vendor-builder"
  },
  "build": {
    "clean_before_build": true,
    "check_vendor_dependencies": true
  },
  "serve": {
    "port": 8000,
    "host": "localhost",
    "check_vendor_dependencies": true
  },
  "docker": {
    "image_name": "phantom-docs-kit",
    "build_tag": "latest",
    "container_prefix": "phantom-docs"
  },
  "logging": {
    "enabled": true,
    "console_level": "INFO",
    "file_level": "DEBUG",
    "log_directory": "logs",
    "max_file_size": "10MB",
    "backup_count": 5,
    "timestamp_format": "%Y-%m-%d %H:%M:%S",
    "log_filename_pattern": "phantom-{mode}-{date}-{time}.log"
  }
}
```

## Advanced Usage

### Running with Docker

Execute the following commands to run easily on Docker.

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py --docker</span>
</div>

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py --docker</span>
</div>

### Running in Remote Environments with Docker

If you want to work in a remote environment with Docker, Mutagen installation is required for file synchronization 
and port forwarding. Mutagen enables you to work in a remote Docker environment as if you were working in your 
local environment.

To install Mutagen on your Mac device, run the following command:

```bash
brew install mutagen-io/mutagen/mutagen
```

After installation is complete, run the following command in Terminal to verify the installation status:

```bash
mutagen version
```

Docker SDK and Mutagen will recognize your remote server through the `DOCKER_HOST` environment variable.

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">DOCKER_HOST=ssh://user@remote-server</span>
</div>

SSH access must be established without any obstacles between your development device and the remote server with Docker installed.

Example steps are below:

If you don't have an SSH key, generate one on your local machine:

```bash
ssh-keygen -t ed25519 -C "phantom-docs"
```

Copy the public key to the remote server:
```bash
ssh-copy-id user@remote-server
```

Test your connection:

```bash
ssh user@remote-server docker info
```

If you've successfully reached this point, define the `DOCKER_HOST` environment variable with
your remote server's information:

```bash
export DOCKER_HOST=ssh://user@remote-server
```

Then ensure you're in the project directory and run the `serve` command:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py --docker</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Documentation Kit</h3>
        <span class="asciinema-player-info">Terminal Recording</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/serve_docker_remote_firstRun.cast"
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

Run the following command for `build`:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py --docker</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Documentation Kit</h3>
        <span class="asciinema-player-info">Terminal Recording</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/build_docker_remote.cast"
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

One important detail to note is that when you build in a remote environment with Docker, the build outputs
are saved in the output directory archived as `phantom-docs-build-docker-remote-{timestamp}.tar.gz`.

### Command Parameters

| Parameter   | Description                      |
|-------------|----------------------------------|
| `--docker`  | Run inside Docker container      |
| `--verbose` | Detailed log output              |
| `--quiet`   | Minimal log output               |

## System Requirements

- Python 3.8+
- Node.js 22+ 
- Docker (optional)

## First Run

When running for the first time, the system automatically:

- Checks for missing dependencies
- Compiles vendor files (JavaScript/CSS)
- Starts the MkDocs server