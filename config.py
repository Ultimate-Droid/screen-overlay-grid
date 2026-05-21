"""Configuration management and persistence for the overlay app."""

import json
import os
from pathlib import Path
from dataclasses import dataclass, asdict



@dataclass
class LineConfig:
    """Configuration for a single line."""
    x: int
    y: int
    is_horizontal: bool
    color: str = "#00FF00"
    thickness: int = 1
    opacity: int = 255  # 0-255


@dataclass
class AppConfig:
    """Main application configuration."""
    window_width: int = None #Will be set to screen width on load
    window_height: int = None #Will be set to screen height on load
    lines: list = None
    grid_mode: str = "crosshair"  # "grid", "crosshair", "mixed"
    is_locked: bool = False
    show_on_startup: bool = True
    
    def __post_init__(self):
        if self.lines is None:
            self.lines = []


class ConfigManager:
    """Handles loading and saving app configuration."""
    
    def __init__(self):
        self.config_dir = Path.home() / ".screen_overlay_grid"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(exist_ok=True)
        self.config = self._load_config()
        self._apply_screen_resolution()
    
    def _get_screen_resolution(self):
        """Detect the primary display resolution."""
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height
    
    def _apply_screen_resolution(self):
        width, height = self._get_screen_resolution()
        self.config.window_width = width
        self.config.window_height = height
        self.save_config(self.config)

    def _load_config(self) -> AppConfig:
        """Load configuration from file or create default."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    # Convert line dicts back to LineConfig objects
                    lines = [LineConfig(**line) for line in data.get('lines', [])]
                    config = AppConfig(
                        window_width=data.get('window_width', None),
                        window_height=data.get('window_height', None),
                        lines=lines,
                        grid_mode=data.get('grid_mode', 'crosshair'),
                        is_locked=data.get('is_locked', False),
                        show_on_startup=data.get('show_on_startup', True)
                    )
                    return config
            except (json.JSONDecodeError, KeyError, TypeError):
                pass
        
        return AppConfig()
    
    def save_config(self, config: AppConfig):
        """Save configuration to file."""
        self.config = config
        data = {
            'window_width': config.window_width,
            'window_height': config.window_height,
            'lines': [asdict(line) for line in config.lines],
            'grid_mode': config.grid_mode,
            'is_locked': config.is_locked,
            'show_on_startup': config.show_on_startup
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_line(self, x: int, y: int, is_horizontal: bool, 
                 color: str = "#00FF00", thickness: int = 1):
        """Add a line to the configuration."""
        line = LineConfig(x, y, is_horizontal, color, thickness)
        self.config.lines.append(line)
        self.save_config(self.config)
        return line
    
    def remove_line(self, index: int):
        """Remove a line by index."""
        if 0 <= index < len(self.config.lines):
            self.config.lines.pop(index)
            self.save_config(self.config)
    
    def update_line(self, index: int, **kwargs):
        """Update line properties."""
        if 0 <= index < len(self.config.lines):
            line = self.config.lines[index]
            for key, value in kwargs.items():
                if hasattr(line, key):
                    setattr(line, key, value)
            self.save_config(self.config)
    
    def clear_lines(self):
        """Clear all lines."""
        self.config.lines = []
        self.save_config(self.config)
