#!/usr/bin/env python3
"""
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>

TR: Evrensel Terminal Kayıt Aracı (run_with_recording.py)
==========================================

Bu araç, herhangi bir terminal komutunu asciinema ile kaydeden bağımsız bir yardımcıdır.
Kayıtlar recordings/ dizinine kaydedilir (yoksa otomatik oluşturulur).

Kullanım:
--------
python run_with_recording.py python3 serve.py --verbose
python run_with_recording.py npm run build  
python run_with_recording.py ./my-script.sh

Ana Özellikler:
--------------
- Herhangi bir komutu asciinema ile kaydet
- Otomatik dosya adlandırma (komut_tarih_saat.cast)
- Çalışma süresi ve dosya boyutu bilgisi
- Kayıt oynatma ve yükleme komutları

Çıktı Dosyaları:
---------------
- recordings/{komut}_{YYYYMMDD}_{HHMMSS}.cast
- Python komutları için script adı kullanılır
- Örnek: serve_20250131_142530.cast

==========================================
EN: Universal Terminal Recording Tool (run_with_recording.py)
==========================================

This tool is a standalone utility that records any terminal command with asciinema.
Recordings are saved in recordings/ directory (created automatically if doesn't exist).

Usage:
------
python run_with_recording.py python3 serve.py --verbose
python run_with_recording.py npm run build
python run_with_recording.py ./my-script.sh

Key Features:
------------
- Record any command with asciinema
- Automatic file naming (command_date_time.cast)
- Runtime duration and file size info
- Playback and upload commands

Output Files:
------------
- recordings/{command}_{YYYYMMDD}_{HHMMSS}.cast
- For Python commands, uses script name
- Example: serve_20250131_142530.cast

"""

import sys
import subprocess
import datetime
import time
import os
from pathlib import Path


class RecordingWrapper:
    def __init__(self):
        self.recording_file = None
        self.start_time = None
        self.sync_marker = None
        self.command_args = []
        
    def setup_paths(self):
        """Setup recordings directory in current working directory"""
        # Use current working directory instead of script location
        recordings_dir = Path.cwd() / "recordings"
        recordings_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate script name from command
        if self.command_args:
            # Get the base command name for filename
            base_cmd = Path(self.command_args[0]).stem
            # If it's python/python3, use the script name instead
            if base_cmd in ['python', 'python3', 'py'] and len(self.command_args) > 1:
                base_cmd = Path(self.command_args[1]).stem
        else:
            base_cmd = "recording"
            
        script_name = base_cmd.replace('.', '_').replace('/', '_')
        self.recording_file = recordings_dir / f"{script_name}_{timestamp}.cast"
        
        return recordings_dir
    
    def parse_args(self):
        """Parse command line arguments"""
        # Check if we have minimum arguments
        if len(sys.argv) < 2:
            self.show_usage()
            sys.exit(1)
        
        # Look for -m flag
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] == '-m' and i + 1 < len(sys.argv):
                self.sync_marker = sys.argv[i + 1]
                i += 2
            else:
                # Collect remaining args as command
                self.command_args = sys.argv[i:]
                break
        
        if not self.command_args:
            self.show_usage()
            sys.exit(1)

    # noinspection PyMethodMayBeStatic
    def show_usage(self):
        """Show usage information"""
        print("Usage: run_with_recording.py [-m MARKER] <command> [args...]")
        print("Examples:")
        print("  run_with_recording.py python3 serve.py --verbose")
        print("  run_with_recording.py npm run build")
        print("  run_with_recording.py ./my-script.sh")
        print("  run_with_recording.py -m 'SYNC_START' python3 serve.py")
        print("\nOptions:")
        print("  -m MARKER    Add synchronization marker at start of recording")
        print("\nRecordings will be saved to: recordings/")
    
    def run(self):
        """Main execution"""
        # Parse arguments
        self.parse_args()
        
        # Check if asciinema is available
        try:
            subprocess.run(["asciinema", "--version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print("Error: asciinema is not installed or not found in PATH")
            print(f"Details: {e}")
            print("Install with: brew install asciinema (macOS)")
            print("or: pip install asciinema")
            sys.exit(1)
        
        # Setup paths
        recordings_dir = self.setup_paths()
        
        # Build the command to execute
        command_string = ' '.join(self.command_args)
        
        # If sync marker is provided, wrap command to echo it first
        if self.sync_marker:
            # Use bash -c to execute both echo and the actual command
            command_string = f"bash -c 'echo \"{self.sync_marker}\" && {command_string}'"
        
        print("-" * 60)
        print(f"Starting recording: {self.recording_file.name}")
        print(f"Command: {' '.join(self.command_args)}")
        if self.sync_marker:
            print(f"Sync marker: {self.sync_marker}")
        print(f"Working directory: {Path.cwd()}")
        print(f"Recording location: {recordings_dir}")
        print("-" * 60)
        print()
        
        # Record start time
        self.start_time = time.time()
        
        # Set up environment to ensure output is visible
        env = os.environ.copy()
        env['PYTHONUNBUFFERED'] = '1'  # Force unbuffered output for Python
        env['FORCE_COLOR'] = '1'  # Force color output
        
        # Build asciinema command
        asciinema_cmd = [
            "asciinema", "rec",
            "--overwrite",
            "--title", f"Recording: {command_string}",
            "--idle-time-limit", "2",
            "--command", command_string,
            str(self.recording_file)
        ]
        
        try:
            # Run asciinema recording with proper environment
            # Execute in current working directory
            result = subprocess.run(asciinema_cmd, env=env, cwd=Path.cwd())
            
            # Calculate duration
            duration = time.time() - self.start_time
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            
            # Show summary if recording was successful
            if self.recording_file.exists():
                file_size = self.recording_file.stat().st_size / 1024
                
                print()
                print("-" * 60)
                print(f"Recording completed successfully!")
                print(f"File: {self.recording_file.name}")
                print(f"Duration: {minutes:02d}:{seconds:02d}")
                print(f"Size: {file_size:.1f} KB")
                print(f"Location: {self.recording_file}")
                print("-" * 60)
                print(f"Play: asciinema play {self.recording_file}")
                print(f"Upload: asciinema upload {self.recording_file}")
                print("-" * 60)
            
            # Exit with same code as the recorded command
            sys.exit(result.returncode)
            
        except KeyboardInterrupt:
            print("\nRecording interrupted by user")
            if self.recording_file and self.recording_file.exists():
                print(f"Partial recording saved: {self.recording_file}")
            sys.exit(1)
        except Exception as e:
            print(f"\nError during recording: {e}")
            sys.exit(1)


if __name__ == "__main__":
    wrapper = RecordingWrapper()
    wrapper.run()