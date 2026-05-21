# Installation & Setup Guide

## System Requirements

- **OS:** Windows 10 or Windows 11
- **Python:** 3.8 or higher
- **RAM:** 50MB minimum
- **Screen Resolution:** Any (1920x1080 or higher recommended)

## Installation Methods

### Method 1: Python Source (Recommended for Development)

#### Step 1: Ensure Python is Installed
```bash
python --version
```
Should show Python 3.8 or higher. If not installed, download from [python.org](https://www.python.org/downloads/).

#### Step 2: Install Dependencies
Navigate to the project directory and run:
```bash
pip install -r requirements.txt
```

#### Step 3: Run the Application
```bash
python main.py
```

### Method 2: Standalone Executable (Easiest for End Users)

#### Build Process
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   python build_exe.py
   ```

3. Find the executable in the `dist` folder:
   ```
   dist/ScreenOverlayGrid.exe
   ```

#### Running the Executable
Simply double-click `ScreenOverlayGrid.exe` to run the application. No Python installation needed!

**Optional:** Create a Windows shortcut for easy access:
- Right-click `ScreenOverlayGrid.exe` → Send to → Desktop (create shortcut)

### Method 3: Run from Command Line

```bash
# From project directory
cd path\to\screen-overlay-grid
python main.py
```

Or create a `.bat` file for quick launching:

**run.bat:**
```batch
@echo off
python "%~dp0main.py"
pause
```

Save as `run.bat` in the project folder and double-click to run.

---

## Verifying Installation

Run the test suite to verify everything works:
```bash
python test_app.py
```

You should see:
```
==================================================
✓ All tests passed successfully!
==================================================
```

---

## First Launch Checklist

After running the application:

- [ ] Overlay window appears on screen (green lines)
- [ ] System tray icon visible (lime green grid icon)
- [ ] Right-click tray menu works
- [ ] Can drag lines to move them
- [ ] Lines persist after restart

If any of these don't work, see the Troubleshooting section below.

---

## Configuration Files

After first launch, configuration is stored at:
```
C:\Users\YourUsername\.screen_overlay_grid\config.json
```

This folder contains:
- `config.json` - Your saved lines, colors, and settings

**Backup:**
To backup your setup, copy this entire folder to a safe location.

**Reset:**
To reset to defaults, delete the folder and restart the app.

---

## Uninstallation

### Remove Python Source Installation
Simply delete the project folder. Settings are stored in:
```
C:\Users\YourUsername\.screen_overlay_grid\
```

To completely remove, also delete this folder.

### Remove Standalone Executable
- Delete `ScreenOverlayGrid.exe` and any shortcuts
- Optional: Delete the `.screen_overlay_grid` folder in your user home directory

---

## Troubleshooting Installation Issues

### "Python not found" or "'python' is not recognized"
**Solution:** Python is not in your PATH. Either:
1. Reinstall Python and check "Add Python to PATH"
2. Use full path: `C:\Python311\python.exe main.py` (adjust version number)

### "pip: command not found"
**Solution:** Use Python's pip module directly:
```bash
python -m pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named 'tkinter'"
**Solution:** Tkinter is usually included with Python. If missing, reinstall Python and select "tcl/tk and IDLE" during installation.

### "Failed to build Pillow"
**Solution:** This was already fixed in requirements.txt. Try:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Tray icon doesn't appear or crashes
**Solution:** 
1. Restart the application
2. Check Windows system tray settings
3. Run with administrator privileges

### "DLL load failed" error
**Solution:**
1. Update Windows and Python
2. Reinstall Python and dependencies:
   ```bash
   pip uninstall -r requirements.txt
   pip install -r requirements.txt
   ```

---

## Upgrading or Reinstalling

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Fresh Installation
```bash
# Remove old installation
pip uninstall -r requirements.txt

# Reinstall
pip install -r requirements.txt

# Run
python main.py
```

---

## Getting Help

1. **Check the README.md** for feature documentation
2. **Review QUICKSTART.md** for common tasks
3. **Check Windows Event Viewer** for system errors (Settings → System → Logs)
4. **Try the test suite** to diagnose issues:
   ```bash
   python test_app.py
   ```

---

## Next Steps

- Read **QUICKSTART.md** to learn basic usage
- Read **README.md** for full documentation
- Explore the system tray menu to add your first lines
- Customize colors and positions for your workflow

---

**Enjoy using Screen Overlay Grid! 🎨**
