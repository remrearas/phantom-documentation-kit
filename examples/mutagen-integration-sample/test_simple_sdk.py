#!/usr/bin/env python3
"""
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>

TR: Docker SDK ve Mutagen Entegrasyon Test Scripti
==================================================

Phantom Documentation Kit'in mevcut Docker entegrasyonuna, uzak sunucularda da sorunsuz 
çalışabilme yeteneği kazandırmak amacıyla bu gelişmiş test scripti hazırlanmıştır. Local 
Docker kullanımının ötesine geçerek, remote Docker daemon'larla güvenli ve performanslı 
bir şekilde çalışabilmeyi hedefleyen bu yaklaşım, modern DevOps pratiklerine uygun bir 
altyapı sunmaktadır.

Bu entegrasyon testi, mevcut Docker SDK altyapısına dahil edilmeden önce, Mutagen ile 
yapılan kapsamlı manuel testlerin başarıyla tamamlanması sonrasında geliştirilmiştir. 
Otomasyon süreçlerine geçiş için kritik bir ön hazırlık niteliğinde olan bu script, 
uzak sunuculardaki Docker container'ları ile yerel geliştirme ortamı arasında güvenilir 
bir köprü kurmaktadır.

Script'in temel amacı, Docker Python SDK ve Mutagen teknolojilerini entegre ederek, 
uzak Docker container yönetiminde çift yönlü (bidirectional) dosya senkronizasyonunu 
göstermek ve test etmektir. Bu sayede geliştiriciler, uzak sunuculardaki container'larla 
sanki yerel ortamda çalışıyormuş gibi etkileşim kurabilir, dosya değişiklikleri anlık 
olarak senkronize edilir ve geliştirme döngüsü kesintisiz devam eder.

Mimari Genel Bakış:
------------------
1. Uzak Docker Bağlantısı: Uzak Docker daemon erişimi için SSH tabanlı DOCKER_HOST kullanır
2. Konteyner Yönetimi: Container lifecycle işlemleri için Docker Python SDK
3. Dosya Senkronizasyonu: Yüksek performanslı, çift yönlü dosya senkronizasyonu için Mutagen
4. İzleme: Loglama entegrasyonu ile gerçek zamanlı senkronizasyon durumu izleme

Ana Bileşenler:
--------------
- SSH Bağlantısı: Uzak sunucu erişilebilirliğini doğrular
- Docker SDK: Programatik container yönetimi (Docker işlemleri için subprocess kullanmaz)
- Mutagen CLI: Dosya senkronizasyonu (Python SDK mevcut değil, subprocess kullanır)
- İzleme: Senkronizasyon durumu ve simüle edilmiş serve logları için arka plan thread'leri

Test Akışı:
-----------
1. Uzak sunucuya SSH bağlantısını doğrula
2. SSH transport üzerinden Docker SDK bağlantısını test et
3. Mutagen kurulumunu doğrula
4. Docker SDK kullanarak test containerı oluştur
5. Mutagen sync oturumu oluştur
6. Çift yönlü dosya senkronizasyonunu test et
7. Formatlanmış loglama ile senkronizasyon durumunu izle

Ortam Gereksinimleri:
--------------------
- Python: 3.13.3+ (Docker SDK 7.1.0 ile)
- Docker: Uzak sunucuda 27.5.1+
- Mutagen: Yerel makinede 0.18.1+
- SSH: Key tabanlı kimlik doğrulaması yapılandırılmış

Yapılandırma:
------------
config.json dosyası gerektirir:
- remote_server: SSH bağlantı detayları
- docker: Container ve senkronizasyon tercihleri
- SSH seçenekleri: Bağlantı kararlılığı için

==================================================

EN: Docker SDK and Mutagen Integration Test Script
==================================================

This advanced test script has been developed to enhance Phantom Documentation Kit's 
existing Docker integration with the capability to work seamlessly on remote servers. 
By transcending the limitations of local Docker usage and targeting secure, high-performance 
operations with remote Docker daemons, this approach provides an infrastructure aligned 
with modern DevOps practices.

This integration test has been developed following successful completion of comprehensive 
manual tests with Mutagen, before being incorporated into the existing Docker SDK 
infrastructure. As a critical preliminary preparation for transitioning to automation 
processes, this script establishes a reliable bridge between Docker containers on remote 
servers and the local development environment.

The primary purpose of this script is to demonstrate and test bidirectional file 
synchronization in remote Docker container management by integrating Docker Python SDK 
and Mutagen technologies. This enables developers to interact with containers on remote 
servers as if working in a local environment, with file changes synchronized instantly 
and the development cycle continuing uninterrupted.

Architecture Overview:
---------------------
1. Remote Docker Connection: Uses SSH-based DOCKER_HOST for remote Docker daemon access
2. Container Management: Docker Python SDK for container lifecycle operations
3. File Synchronization: Mutagen for high-performance, bidirectional file sync
4. Monitoring: Real-time sync status monitoring with integrated logging

Key Components:
--------------
- SSH Connection: Validates remote server accessibility
- Docker SDK: Programmatic container management (no subprocess for Docker operations)
- Mutagen CLI: File synchronization (no Python SDK available, uses subprocess)
- Monitoring: Background threads for sync status and simulated serve logs

Test Flow:
----------
1. Validate SSH connection to remote server
2. Test Docker SDK connection via SSH transport
3. Verify Mutagen installation
4. Create test container using Docker SDK
5. Establish Mutagen sync session
6. Test bidirectional file synchronization
7. Monitor sync status with formatted logging

Environment Requirements:
------------------------
- Python: 3.13.3+ (with Docker SDK 7.1.0)
- Docker: 27.5.1+ on remote server
- Mutagen: 0.18.1+ on local machine
- SSH: Key-based authentication configured

Configuration:
-------------
Requires config.json with:
- remote_server: SSH connection details
- docker: Container and sync preferences
- SSH options for connection stability

"""

import subprocess
import sys
import os
import time
import json
import shutil
from pathlib import Path
import logging

# Simple logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Load configuration
config_path = Path(__file__).parent / 'config.json'
try:
    with open(config_path) as f:
        config = json.load(f)
except FileNotFoundError:
    logger.error(f"Configuration file not found: {config_path}")
    logger.error("Please create config.json with remote server details")
    sys.exit(1)
except json.JSONDecodeError as json_err:
    logger.error(f"Invalid JSON in config file: {json_err}")
    sys.exit(1)

# Docker SDK check and import
try:
    import docker
    from docker.errors import DockerException, APIError, NotFound
except ImportError:
    docker = None
    DockerException = Exception
    APIError = Exception
    NotFound = Exception
    logger.error("Docker Python package not installed")
    logger.error("Install with: pip install docker")
    sys.exit(1)


def test_ssh():
    """Test SSH connection"""
    remote = config['remote_server']
    host = remote['host']
    user = remote['user']
    ssh_key = os.path.expanduser(remote['ssh_key'])
    
    logger.info(f"Testing SSH connection to {user}@{host}...")
    
    # Build SSH command with options from config
    ssh_cmd = ['ssh', '-i', ssh_key]
    
    # Add SSH options
    for option, value in remote['ssh_options'].items():
        ssh_cmd.extend(['-o', f'{option}={value}'])
    
    ssh_cmd.extend([f'{user}@{host}', 'echo "SSH OK"'])
    
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        logger.info("✓ SSH connection successful")
        return True
    else:
        logger.error(f"✗ SSH connection failed: {result.stderr}")
        return False


def test_docker():
    """Test Docker connection using Docker SDK"""
    logger.info("Testing Docker connection...")
    
    # Set Docker host from config
    remote = config['remote_server']
    os.environ['DOCKER_HOST'] = f'ssh://{remote["user"]}@{remote["host"]}'
    
    try:
        # Create Docker client
        client = docker.from_env()
        
        # Test connection
        version_info = client.version()
        
        logger.info("✓ Docker connection successful")
        logger.info(f"  Server Version: {version_info.get('Version', 'Unknown')}")
        logger.info(f"  API Version: {version_info.get('ApiVersion', 'Unknown')}")
        
        # Close client
        client.close()
        return True
        
    except DockerException as docker_err:
        logger.error(f"✗ Docker connection failed: {docker_err}")
        return False
    except Exception as ex:
        logger.error(f"✗ Unexpected error: {ex}")
        return False


def test_mutagen():
    """Test Mutagen installation"""
    logger.info("Testing Mutagen installation...")
    
    result = subprocess.run(['mutagen', 'version'], capture_output=True, text=True)
    
    if result.returncode == 0:
        logger.info(f"✓ Mutagen installed: {result.stdout.strip()}")
        return True
    else:
        logger.error("✗ Mutagen not found")
        logger.error("  Install with: brew install mutagen-io/mutagen/mutagen")
        return False


def test_mutagen_sync_sdk():
    """Test Mutagen sync with Docker SDK"""
    logger.info("Testing Mutagen sync functionality with Docker SDK...")
    
    docker_config = config.get('docker', {})
    container_name = docker_config.get('container_prefix', 'phantom-mutagen-test')
    sync_test_dir = Path("sync_test")
    session_name = f'{container_name}-sync'
    container = None  # Initialize container variable
    
    # Create Docker client
    try:
        client = docker.from_env()
    except DockerException as docker_err:
        logger.error(f"✗ Failed to create Docker client: {docker_err}")
        return False, None, None
    
    try:
        # Clean up any existing container using Docker SDK
        logger.info("Cleaning up any existing test container...")
        try:
            old_container = client.containers.get(container_name)
            old_container.remove(force=True)
            logger.info("  Removed existing container")
        except NotFound:
            pass
        
        # Clean up any existing Mutagen sessions
        logger.info("Cleaning up any existing Mutagen sessions...")
        subprocess.run(['mutagen', 'sync', 'terminate', '--all'], capture_output=True)
        
        # Create local sync test directory
        logger.info(f"Creating local test directory: {sync_test_dir}")
        sync_test_dir.mkdir(exist_ok=True)
        
        # Create a test file
        test_file = sync_test_dir / "test.txt"
        test_file.write_text("Hello from local host!")
        logger.info(f"  Created {test_file}")
        
        # Start container using Docker SDK
        logger.info(f"Starting container '{container_name}'...")
        try:
            container = client.containers.run(
                image='alpine:latest',
                name=container_name,
                command=f'sh -c "mkdir -p {docker_config.get("sync_directory", "/sync")} && sleep 3600"',
                detach=True,
                remove=False
            )
            logger.info(f"✓ Container '{container_name}' started")
            logger.info(f"  Container ID: {container.short_id}")
            
        except APIError as api_err:
            logger.error(f"✗ Failed to start container: {api_err}")
            return False, None, None
        
        # Create Mutagen sync session (still uses subprocess)
        logger.info("Creating Mutagen sync session...")
        result = subprocess.run(
            ['mutagen', 'sync', 'create',
             '--name', session_name,
             str(sync_test_dir),
             f'docker://{container_name}{docker_config.get("sync_directory", "/sync")}'],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"✗ Failed to create Mutagen session: {result.stderr}")
            # Clean up container
            container.remove(force=True)
            return False, None, None
        
        logger.info("✓ Mutagen sync session created")
        
        # Wait for initial sync
        logger.info("Waiting for initial sync...")
        time.sleep(3)
        
        # Check if file exists in container using Docker SDK
        logger.info("Checking if file synced to container...")
        try:
            sync_dir = docker_config.get('sync_directory', '/sync')
            exec_result = container.exec_run(f'cat {sync_dir}/test.txt')
            
            if exec_result.exit_code == 0 and exec_result.output.decode().strip() == "Hello from local host!":
                logger.info("✓ File successfully synced to container")
            else:
                logger.error(f"✗ File sync failed: {exec_result.output.decode()}")
                return False, container_name, session_name
                
        except APIError as api_err:
            logger.error(f"✗ Failed to exec in container: {api_err}")
            return False, container_name, session_name
        
        # Test reverse sync (container to host) using Docker SDK
        logger.info("Testing reverse sync (container to host)...")
        try:
            exec_result = container.exec_run(
                f'sh -c "echo \\"Hello from container!\\" > {docker_config.get("sync_directory", "/sync")}/container.txt"'
            )
            
            if exec_result.exit_code != 0:
                logger.error(f"✗ Failed to create file in container: {exec_result.output.decode()}")
                return False, container_name, session_name
                
        except APIError as api_err:
            logger.error(f"✗ Failed to exec in container: {api_err}")
            return False, container_name, session_name
        
        # Wait for sync
        time.sleep(3)
        
        container_file = sync_test_dir / "container.txt"
        if container_file.exists():
            content = container_file.read_text().strip()
            if content == "Hello from container!":
                logger.info("✓ File successfully synced from container")
            else:
                logger.error(f"✗ File content mismatch: {content}")
                return False, container_name, session_name
        else:
            logger.error("✗ File not synced from container")
            return False, container_name, session_name
        
        # Show sync status
        logger.info("Mutagen sync status:")
        result = subprocess.run(
            ['mutagen', 'sync', 'list', session_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"  {line}")
        
        # Get container info using Docker SDK
        container.reload()  # Refresh container info
        logger.info(f"Container status: {container.status}")
        logger.info(f"Container IP: {container.attrs['NetworkSettings']['IPAddress'] or 'Bridge network'}")
        
        logger.info("=" * 60)
        logger.info("✓ Mutagen sync test PASSED!")
        logger.info("The container and sync session are running.")
        logger.info(f"Sync directory: {sync_test_dir.absolute()}")
        logger.info("=" * 60)
        
        # Return container object instead of name for SDK usage
        return True, container, session_name
        
    except Exception as sync_err:
        logger.error(f"✗ Mutagen sync test error: {sync_err}")
        # Clean up on error
        subprocess.run(['mutagen', 'sync', 'terminate', '--all'], capture_output=True)
        try:
            if 'container' in locals() and container is not None:
                container.remove(force=True)
        except (DockerException, NameError):
            pass
        return False, None, None
    finally:
        # Close Docker client
        client.close()


def run_mutagen_monitor(session_name, verbose=True):
    """Run Mutagen monitor and display output with logging style"""
    import threading
    
    def monitor_output():
        # Build command with verbose flags
        cmd = ['mutagen', 'sync', 'monitor']
        if verbose:
            cmd.append('-l')  # -l for long/detailed format
        cmd.append(session_name)
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        while True:
            line = process.stdout.readline()
            if not line:
                break
            
            # Format and display monitor output
            line = line.strip()
            if line:
                # Parse regular text output
                if 'Identifier:' in line:
                    logger.info(f"[mutagen.session] {line}")
                elif 'Status:' in line:
                    logger.info(f"[mutagen.status] {line}")
                elif 'Conflicts:' in line and 'None' not in line:
                    logger.warning(f"[mutagen.conflicts] {line}")
                elif 'Problems:' in line and 'None' not in line:
                    logger.error(f"[mutagen.problems] {line}")
                elif 'Scanning' in line or 'scanning' in line:
                    logger.info(f"[mutagen.scan] {line}")
                elif 'Watching' in line or 'watching' in line:
                    logger.info(f"[mutagen.watch] {line}")
                elif 'Transitioning' in line or 'transitioning' in line:
                    logger.info(f"[mutagen.transition] {line}")
                elif 'Staging' in line or 'staging' in line:
                    logger.info(f"[mutagen.stage] {line}")
                elif 'Reconciling' in line or 'reconciling' in line:
                    logger.info(f"[mutagen.reconcile] {line}")
                elif 'Applying' in line or 'applying' in line:
                    logger.info(f"[mutagen.apply] {line}")
                elif 'alpha:' in line.lower():
                    logger.debug(f"[mutagen.alpha] {line}")
                elif 'beta:' in line.lower():
                    logger.debug(f"[mutagen.beta] {line}")
                elif 'error' in line.lower():
                    logger.error(f"[mutagen.error] {line}")
                elif 'warning' in line.lower():
                    logger.warning(f"[mutagen.warning] {line}")
                elif 'connected' in line.lower():
                    logger.info(f"[mutagen.connection] {line}")
                elif line.strip():  # Any other non-empty line
                    logger.debug(f"[mutagen] {line}")
        
        # Also capture stderr
        for line in process.stderr:
            if line.strip():
                logger.error(f"[mutagen.stderr] {line.strip()}")
        
        process.wait()
    
    # Run monitor in background thread
    monitor_thread = threading.Thread(target=monitor_output)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    return monitor_thread


def simulate_serve_logs():
    """Simulate serve command periodic logs"""
    import random
    import threading
    
    serve_messages = [
        "[serve] Watching for file changes...",
        "[serve] Processing request: GET /",
        "[serve] Processing request: GET /docs",
        "[serve] Building documentation...",
        "[serve] Documentation build completed",
        "[serve] Hot reload triggered",
        "[serve] Serving on http://0.0.0.0:8000",
        "[serve] File change detected: index.md",
        "[serve] Rebuilding affected pages...",
        "[serve] Cache cleared",
        "[serve] Static assets served",
        "[serve] WebSocket connection established",
        "[serve] Live reload ready"
    ]
    
    def log_serve_output():
        while True:
            # Random interval between 2-8 seconds
            interval = random.uniform(2, 8)
            time.sleep(interval)
            
            # Pick a random message
            message = random.choice(serve_messages)
            logger.info(f"[phantom.serve] {message}")
            
            # Occasionally log multiple related messages
            if random.random() < 0.3:  # 30% chance
                time.sleep(0.5)
                if "request" in message:
                    logger.info("[phantom.serve] Request completed in 23ms")
                elif "build" in message:
                    logger.info("[phantom.serve] Build time: 1.2s")
                elif "change detected" in message:
                    logger.info("[phantom.serve] Reloading browser...")
    
    # Start serve simulation in background thread
    serve_thread = threading.Thread(target=log_serve_output, daemon=True)
    serve_thread.start()
    return serve_thread


def main():
    """Run simple tests with Docker SDK"""
    logger.info("Simple Remote Sync Docker Test with Mutagen")
    logger.info("=" * 50)
    
    tests = [
        ("SSH", test_ssh),
        ("Docker SDK", test_docker),
        ("Mutagen", test_mutagen),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            success = test_func()
            results.append((name, success))
        except Exception as test_err:
            logger.error(f"✗ {name} test error: {test_err}")
            results.append((name, False))
    
    # If all basic tests pass, run sync test
    container = None
    session_name = None
    
    if all(success for _, success in results):
        logger.info("=" * 50)
        logger.info("Running Mutagen sync test with Docker SDK...")
        logger.info("=" * 50)
        
        sync_success, container, session_name = test_mutagen_sync_sdk()
        results.append(("Mutagen Sync", sync_success))
    
    logger.info("=" * 50)
    logger.info("Summary:")
    for name, success in results:
        if isinstance(success, tuple):
            success = success[0]
        status = "✓ PASS" if success else "✗ FAIL"
        logger.info(f"  {name}: {status}")
    logger.info("=" * 50)
    
    all_passed = all(success[0] if isinstance(success, tuple) else success for _, success in results)
    
    # If all tests passed and we have a sync session, run monitor
    if all_passed and session_name and container:
        try:
            logger.info("Starting Mutagen sync monitor...")
            logger.info("Press Ctrl+C to stop")
            
            # Get sync directory path
            sync_test_dir = Path("sync_test").absolute()
            
            # Show instructions
            logger.info("[phantom.test] Sync test environment is running")
            logger.info(f"[phantom.test] Local directory: {sync_test_dir}")
            sync_dir = config.get('docker', {}).get('sync_directory', '/sync')
            logger.info(f"[phantom.test] Container directory: {sync_dir}")
            logger.info(f"[phantom.test] Container ID: {container.short_id}")
            logger.info("[phantom.test] You can add/modify files in the sync_test directory")
            
            # Run monitor
            # monitor_thread = run_mutagen_monitor(session_name)
            run_mutagen_monitor(session_name)
            
            # Start serve simulation
            logger.info("[phantom.test] Starting serve simulation...")
            simulate_serve_logs()
            
            # Keep running until interrupted
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            logger.info("[phantom.test] Shutting down...")
            
            # Cleanup
            logger.info("[phantom.test] Cleaning up resources...")
            
            if session_name:
                subprocess.run(['mutagen', 'sync', 'terminate', session_name], capture_output=True)
                logger.info("[phantom.test] Terminated Mutagen session")
            
            if container:
                try:
                    # Create new client for cleanup
                    client = docker.from_env()
                    container = client.containers.get(container.id)
                    container.remove(force=True)
                    client.close()
                    logger.info("[phantom.test] Removed container")
                except Exception as cleanup_err:
                    logger.warning(f"[phantom.test] Container cleanup warning: {cleanup_err}")
            
            # Clean up local sync_test directory
            sync_test_dir = Path("sync_test")
            if sync_test_dir.exists():
                try:
                    shutil.rmtree(sync_test_dir)
                    logger.info("[phantom.test] Removed local sync_test directory")
                except Exception as dir_cleanup_err:
                    logger.warning(f"[phantom.test] Directory cleanup warning: {dir_cleanup_err}")
            
            logger.info("[phantom.test] Cleanup completed")
            sys.exit(0)
    else:
        # Exit with error code if tests failed
        sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()