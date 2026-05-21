# Quick Start Guide

## 🚀 Getting Started in 2 Minutes

### Step 1: Install Python (if not already installed)
- Download from [python.org](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**

### Step 2: Install Dependencies
Open Command Prompt in this directory and run:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

That's it! The overlay should appear on your screen.

---

## 🎨 Your First Grid

1. **Application starts** - You'll see a lime green grid overlay on your screen
2. **Add lines** - Right-click the system tray icon (lime grid) → "Add Horizontal Line" or "Add Vertical Line"
3. **Move lines** - Click and drag any line to reposition it
4. **Change colors** - Right-click tray → "Change Colors"
5. **Lock them** - Press `Ctrl+L` to prevent accidental movement

---

## 📌 Essential Controls

| Task | How |
|------|-----|
| Move a line | Click and drag it |
| Add more lines | Right-click tray → Add Line |
| Change line color | Right-click tray → Change Colors |
| Lock lines in place | Press `Ctrl+L` or use tray menu |
| Remove all lines | Press `Ctrl+C` or use tray menu |
| Hide overlay temporarily | Press `ESC` |
| Exit app | Right-click tray → Quit |

---

## 💾 Settings Location

Your settings are automatically saved to:
```
C:\Users\YourUsername\.screen_overlay_grid\config.json
```

Everything is saved automatically - positions, colors, lock state, etc.

---

## 🔧 Creating an Executable (Optional)

To create a standalone `.exe` file you can share:

```bash
pip install pyinstaller
python build_exe.py
```

The executable will be in the `dist` folder.

---

## ❓ Common Questions

**Q: Why can't I see the grid on fullscreen games?**
- Fullscreen exclusive mode games don't allow overlays. Use windowed fullscreen instead.

**Q: Where are my settings saved?**
- In `C:\Users\YourUsername\.screen_overlay_grid\config.json`

**Q: Can I customize the grid spacing?**
- Currently, you manually place lines. Use Ctrl+C to clear and start fresh for a new layout.

**Q: How do I uninstall?**
- Simply delete the folder. Your settings in `.screen_overlay_grid` won't be removed (you can delete manually if needed).

---

## 🎯 Pro Tips

- **Use multiple colors** for different purposes (red for margins, green for alignment)
- **Lock after placement** to avoid accidentally moving lines
- **Save different grid setups** by manually organizing config files
- **Works with any resolution** - automatically uses your screen dimensions

---

## Need Help?

Check the full README.md for detailed documentation and troubleshooting!

Happy designing! 🎨
