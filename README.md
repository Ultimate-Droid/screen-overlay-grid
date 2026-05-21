# Screen Overlay Grid

A lightweight Windows desktop application that displays a customizable grid or crosshair overlay on top of all applications (including fullscreen games and apps). Perfect for UI designers and developers who need pixel-perfect alignment references.

## Features

✨ **Core Features:**
- **Always-on-Top Overlay** - Works with fullscreen apps and games
- **Customizable Lines** - Place horizontal and/or vertical lines anywhere on screen
- **Draggable Lines** - Click and drag lines to reposition them in real-time
- **Lock/Unlock** - Prevent accidental line movement
- **Color Customization** - Change line colors for better visibility
- **System Tray Control** - Minimize to tray and control from system tray menu
- **Persistent Settings** - All line positions and colors are saved automatically

## Installation

### Prerequisites
- Windows 10/11
- Python 3.8+

### Setup

1. Clone or download the project to a directory:
   ```bash
   cd path\to\screen-overlay-grid
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

The overlay will appear on your screen and the system tray icon will show up in your taskbar.

## Usage

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + L` | Toggle lock (prevents line movement) |
| `Ctrl + C` | Clear all lines |
| `ESC` | Hide overlay temporarily |

### Mouse Controls

- **Click and Drag** - Click near any line and drag to reposition it
- **Hover** - Cursor changes to indicate draggable lines

### System Tray Menu

Right-click the system tray icon (lime green grid icon) for:

- **Show/Hide** - Toggle overlay visibility
- **Add Horizontal Line** - Add a horizontal line at screen center
- **Add Vertical Line** - Add a vertical line at screen center
- **Clear All Lines** - Remove all lines
- **Lock/Unlock** - Toggle lock state
- **Change Colors** - Change color of all lines
- **About** - View help information
- **Quit** - Exit the application

## Settings & Configuration

All settings are automatically saved to:
```
C:\Users\{YourUsername}\.screen_overlay_grid\config.json
```

Configuration includes:
- Line positions (x, y coordinates)
- Line properties (color, thickness, orientation)
- Lock state
- Grid mode and visibility

You can manually edit this file if needed, though the app manages it automatically.

## File Structure

```
screen-overlay-grid/
├── main.py                 # Application entry point
├── overlay_window.py       # Main overlay window (Tkinter)
├── lines.py               # Line data model and line management
├── tray.py                # System tray integration
├── config.py              # Configuration management and persistence
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## How It Works

1. **Overlay Window** - Uses Tkinter with transparent background and always-on-top behavior
2. **Line Management** - Lines are stored as data objects with position, orientation, color, and thickness
3. **Persistence** - Configuration is saved to JSON in user's home directory
4. **System Tray** - Integration via pystray for easy access and control
5. **Redraw Loop** - Efficient ~60 FPS canvas redraw for smooth rendering

## Troubleshooting

**Overlay not showing on top of fullscreen apps?**
- This is a limitation of some fullscreen exclusive mode games. The overlay works with fullscreen windowed apps.

**Lines disappearing after restart?**
- Check if the config file exists at `C:\Users\{YourUsername}\.screen_overlay_grid\config.json`
- If corrupted, delete it and the app will create a fresh config

**Tray icon not appearing?**
- Try restarting the application
- Check Windows system tray settings

**Can't interact with overlay?**
- Make sure you're not in "locked" mode (toggle via Ctrl+L or tray menu)

## Tips & Tricks

- Use different colors for different line purposes (e.g., red for margins, green for alignment)
- Lock lines when you're satisfied with placement to avoid accidental movement
- Clear lines and start fresh if you save a design, then open a new project
- Adjust line thickness for better visibility at different zoom levels
- Use horizontal and vertical lines together for perfect alignment grids

## Future Enhancements

Potential features for future versions:
- Save/load multiple grid presets
- Grid spacing and snapping options
- Line labeling and annotation
- Opacity control for better transparency
- Keyboard shortcuts customization
- Multiple color presets
- Grid dimension inputs (for exact spacing)

## License

This project is open source and available for personal and commercial use.

## Support

For issues or feature requests, please refer to the troubleshooting section or check the config file for format reference.

---

**Happy designing! 🎨**
