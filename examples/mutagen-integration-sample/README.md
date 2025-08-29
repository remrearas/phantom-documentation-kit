# Mutagen Integration Sample

Simple test environment for Remote Docker + Mutagen synchronization.

## Prerequisites

### Remote Server Requirements
- Docker must be installed and running on the remote server
- SSH access with key-based authentication
- User must have Docker permissions (or be in the docker group)

### Local Requirements
- Python 3.6+
- Docker Python SDK
- Mutagen (for file synchronization)
- SSH client and key pair

## Setup

1. Copy the sample configuration file:

   ```bash
   cp config.json.sample config.json
   ```

2. Configure your remote server details in `config.json`:

   ```json
   {
     "remote_server": {
       "host": "your-server-ip",
       "user": "your-username",
       "ssh_key": "~/.ssh/your-key",
       "ssh_options": {
         "ConnectTimeout": "5",
         "StrictHostKeyChecking": "no"
       }
     }
   }
   ```

   Replace the following values:
   - `your-server-ip`: Your server's IP address
   - `your-username`: Your SSH username  
   - `~/.ssh/your-key`: Path to your SSH private key

3. Set up SSH key authentication:

   ```bash
   # Generate SSH key if you don't have one
   ssh-keygen -t ed25519 -f ~/.ssh/your-key

   # Copy the public key to your server
   ssh-copy-id -i ~/.ssh/your-key.pub your-username@your-server-ip

   # Test SSH connection
   ssh -i ~/.ssh/your-key your-username@your-server-ip
   ```

4. Install dependencies:

   ```bash
   # Install Docker SDK (if not installed)
   pip install docker

   # Install Mutagen (macOS)
   brew install mutagen-io/mutagen/mutagen

   # Install Mutagen (Linux)
   # Download from: https://github.com/mutagen-io/mutagen/releases
   ```

## Remote Server Setup

Ensure Docker is installed on your remote server:

```bash
# Install Docker on Ubuntu/Debian
curl -fsSL https://get.docker.com | sh

# Add user to docker group (replace 'your-username' with actual username)
sudo usermod -aG docker your-username

# Verify Docker installation
docker --version
docker ps
```

## Usage

```bash
# Run the test
python test_simple_sdk.py
```

The test will:
1. Verify SSH connectivity to the remote server
2. Test Docker connection via SSH
3. Check Mutagen installation
4. Create a test container and establish file synchronization
5. Monitor sync status in real-time

## Files

- `test_simple_sdk.py` - Main test script using Docker SDK
- `config.json` - Configuration file for remote server settings (create from config.json.sample)
- `config.json.sample` - Sample configuration file
- `sync_test/` - Directory for sync testing (created automatically)
- `.gitignore` - Git ignore patterns

## Troubleshooting

### SSH Connection Issues
```bash
# Test SSH connection with verbose output
ssh -v -i ~/.ssh/your-key your-username@your-server-ip

# Check SSH key permissions
chmod 600 ~/.ssh/your-key
```

### Docker Connection Issues
```bash
# Test Docker over SSH
export DOCKER_HOST=ssh://your-username@your-server-ip
docker ps
```

### Mutagen Issues
```bash
# Check Mutagen version
mutagen version

# List active Mutagen sessions
mutagen sync list

# Terminate all Mutagen sessions
mutagen sync terminate --all
```