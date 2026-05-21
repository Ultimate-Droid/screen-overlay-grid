"""System tray integration and menu."""

import tkinter as tk
from tkinter import simpledialog, colorchooser
from PIL import Image, ImageDraw
import pystray
from io import BytesIO
from overlay_window import OverlayWindow
from config import ConfigManager


class TrayMenu:
    """System tray menu for the overlay application."""
    
    def __init__(self, overlay: OverlayWindow, config: ConfigManager):
        self.overlay = overlay
        self.config = config
        self.icon = None
        self.tray_thread = None
    
    def _create_icon_image(self):
        """Create a simple icon for the system tray."""
        # Create a 64x64 image with a simple grid pattern
        img = Image.new('RGB', (64, 64), color='black')
        draw = ImageDraw.Draw(img)
        
        # Draw grid lines
        for i in range(0, 64, 16):
            draw.line([(0, i), (64, i)], fill='lime', width=1)
            draw.line([(i, 0), (i, 64)], fill='lime', width=1)
        
        return img
    
    def _on_quit(self, icon, item):
        """Quit the application."""
        self.overlay.get_root().quit()
    
    def _on_show_hide(self, icon, item):
        """Toggle overlay visibility."""
        self.overlay.toggle_visibility()
    
    def _on_toggle_lock(self, icon, item):
        """Toggle line locking."""
        self.overlay.toggle_lock()
    
    def _on_add_horizontal_line(self, icon, item):
        """Add a horizontal line at the center."""
        height = self.config.config.window_height
        self.overlay.add_line(0, height // 2, True, "#00FF00", 2)
    
    def _on_add_vertical_line(self, icon, item):
        """Add a vertical line at the center."""
        width = self.config.config.window_width
        self.overlay.add_line(width // 2, 0, False, "#00FF00", 2)
    
    def _on_clear_lines(self, icon, item):
        """Clear all lines."""
        self.overlay.clear_all_lines()
    
    def _on_change_color(self, icon, item):
        """Change color of lines."""
        if self.overlay.line_manager.lines:
            # Show color picker dialog
            root = tk.Tk()
            root.withdraw()
            color = colorchooser.askcolor(color="#00FF00", title="Choose Line Color")
            root.destroy()
            
            if color[1]:
                for line in self.overlay.line_manager.lines:
                    line.color = color[1]
                self.config.config.lines = self.overlay._lines_to_config()
                self.config.save_config(self.config.config)
    
    def _on_about(self, icon, item):
        """Show about dialog."""
        root = tk.Tk()
        root.withdraw()
        from tkinter import messagebox
        messagebox.showinfo(
            "Screen Overlay Grid",
            "They're literally just lines.\n\n"
            "Controls:\n"
            "• Click and drag lines to reposition\n"
            "• Ctrl+L to toggle lock\n"
            "• Ctrl+C to clear all lines\n"
            "• ESC to hide overlay\n"
            "• Use tray menu for more options"
        )
        root.destroy()
    
    def create_menu(self):
        """Create the system tray menu."""
        menu = pystray.Menu(
            pystray.MenuItem(
                'Show/Hide',
                self._on_show_hide,
                default=True
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('Add Horizontal Line', self._on_add_horizontal_line),
            pystray.MenuItem('Add Vertical Line', self._on_add_vertical_line),
            pystray.MenuItem('Clear All Lines', self._on_clear_lines),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(
                'Lock/Unlock',
                self._on_toggle_lock
            ),
            pystray.MenuItem('Change Colors', self._on_change_color),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('About', self._on_about),
            pystray.MenuItem('Quit', self._on_quit),
        )
        return menu
    
    def run(self):
        """Start the system tray icon."""
        menu = self.create_menu()
        icon = pystray.Icon(
            "screen_overlay_grid",
            self._create_icon_image(),
            "Screen Overlay Grid",
            menu
        )
        self.icon = icon
        icon.run()
    
    def stop(self):
        """Stop the system tray icon."""
        if self.icon:
            self.icon.stop()
