import hashlib

import PyInstaller.__main__
import sys
import os

def generate_checksum(filepath):
    """Generate and save an MD5 checksum for the executable."""
    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
    checksum = md5.hexdigest()
    
    checksum_path = filepath + '.md5'
    with open(checksum_path, 'w') as f:
        f.write(f"{checksum}  ScreenOverlayGrid.exe\n")
    
    print(f"  MD5 Checksum: {checksum}")
    print(f"  Checksum file: {checksum_path}")
    return checksum

def build_executable():
    """Build a standalone executable using PyInstaller."""
    
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # PyInstaller arguments
    args = [
        'main.py',
        '--name=ScreenOverlayGrid',
        '--onefile',
        '--windowed',  # No console window
        f'--icon={os.path.join(script_dir, "icon.ico")}',  
        f'--distpath={os.path.join(script_dir, "dist")}',
        f'--workpath={os.path.join(script_dir, "build")}',
        f'--specpath={os.path.join(script_dir, "specs")}',
        f'--version-file={os.path.join(script_dir, "version_info.txt")}',
        '--exclude-module=PIL.IcnsImagePlugin',
    ]
    
    print("Building executable...")
    print(f"PyInstaller arguments: {args}")
    
    PyInstaller.__main__.run(args)
    
    executable_path = os.path.join(script_dir, 'dist', 'ScreenOverlayGrid.exe')
    
    if os.path.exists(executable_path):
        print(f"\n✓ Executable created successfully!")
        print(f"  Location: {executable_path}")
        print(f"\nYou can now run the application by double-clicking the .exe file")
        print(f"or running it from command line: {executable_path}")
        generate_checksum(executable_path)
    else:
        print("\n✗ Failed to create executable")
        sys.exit(1)


if __name__ == '__main__':
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        os.system(f'{sys.executable} -m pip install pyinstaller')
    
    build_executable()
