"""Main overlay window implementation using Tkinter."""

import tkinter as tk
from tkinter import colorchooser
from typing import Optional
from lines import LineManager, Line
from config import ConfigManager, LineConfig


class OverlayWindow:
    """Main overlay window with transparent background and custom lines."""
    
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.line_manager = LineManager()
        
        # Create root window
        self.root = tk.Tk()
        self.root.attributes('-topmost', True)
        self.root.attributes('-transparentcolor', '#000000')
        self.root.geometry(f"{config_manager.config.window_width}x{config_manager.config.window_height}+0+0")
        self.root.title("Screen Overlay Grid")
        self.root.configure(bg='#000000')
        self.root.overrideredirect(True)
        
        # Create canvas for drawing
        self.canvas = tk.Canvas(
            self.root,
            bg='#000000',
            highlightthickness=0,
            width=config_manager.config.window_width,
            height=config_manager.config.window_height
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Load lines from config
        self._load_lines_from_config()
        
        # Mouse event bindings
        self.canvas.bind('<Button-1>', self._on_mouse_down)
        self.canvas.bind('<B1-Motion>', self._on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self._on_mouse_up)
        self.canvas.bind('<Motion>', self._on_mouse_move)
        self.root.bind('<Escape>', lambda e: self.hide())
        self.root.bind('<Control-l>', lambda e: self.toggle_lock())
        self.root.bind('<Control-c>', lambda e: self.clear_all_lines())
        
        self.dragging = False
        self.current_cursor = None
        self.is_locked = config_manager.config.is_locked
        self.is_visible = False
        
        # Redraw loop
        self._redraw()
    
    def _load_lines_from_config(self):
        """Load lines from configuration."""
        config = self.config_manager.config
        for line_config in config.lines:
            self.line_manager.add_line(
                line_config.x,
                line_config.y,
                line_config.is_horizontal,
                line_config.color,
                line_config.thickness
            )
    
    def _redraw(self):
        """Continuously redraw the canvas."""
        self.canvas.delete('all')
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if width > 1 and height > 1:
            # Draw all lines
            for line in self.line_manager.lines:
                self._draw_line(line, width, height)
        
        # Schedule next redraw
        self.root.after(16, self._redraw)  # ~60 FPS
    
    def _draw_line(self, line: Line, width: int, height: int):
        """Draw a single line on the canvas."""
        # Convert hex color to RGB and handle opacity
        color = line.color
        
        if line.is_horizontal:
            # Draw horizontal line
            self.canvas.create_line(
                0, line.y, width, line.y,
                fill=color,
                width=line.thickness,
                stipple='' if line.opacity == 255 else 'gray50'
            )
        else:
            # Draw vertical line
            self.canvas.create_line(
                line.x, 0, line.x, height,
                fill=color,
                width=line.thickness,
                stipple='' if line.opacity == 255 else 'gray50'
            )
    
    def _on_mouse_down(self, event):
        """Handle mouse button down."""
        if self.is_locked:
            return
        
        line_index = self.line_manager.get_line_at_point(
            event.x, event.y, sensitivity=15
        )
        
        if line_index is not None:
            self.line_manager.start_drag(line_index)
            self.dragging = True
    
    def _on_mouse_drag(self, event):
        """Handle mouse drag."""
        if not self.dragging or self.is_locked:
            return
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        self.line_manager.drag_line(event.x, event.y, width, height)
        self.config_manager.config.lines = self._lines_to_config()
        self.config_manager.save_config(self.config_manager.config)
    
    def _on_mouse_up(self, event):
        """Handle mouse button up."""
        self.line_manager.end_drag()
        self.dragging = False
    
    def _on_mouse_move(self, event):
        """Handle mouse move to change cursor."""
        if self.is_locked:
            self.canvas.config(cursor='arrow')
            return
        
        line_index = self.line_manager.get_line_at_point(
            event.x, event.y, sensitivity=15
        )
        
        if line_index is not None:
            line = self.line_manager.lines[line_index]
            cursor = 'sb_h_double_arrow' if line.is_horizontal else 'sb_v_double_arrow'
            self.canvas.config(cursor=cursor)
        else:
            self.canvas.config(cursor='arrow')
    
    def _lines_to_config(self):
        """Convert line manager lines to config format."""
        return [
            LineConfig(
                x=line.x,
                y=line.y,
                is_horizontal=line.is_horizontal,
                color=line.color,
                thickness=line.thickness,
                opacity=line.opacity
            )
            for line in self.line_manager.lines
        ]
    
    def show(self):
        """Show the overlay window."""
        if not self.is_visible:
            self.root.deiconify()
            self.is_visible = True
    
    def hide(self):
        """Hide the overlay window."""
        if self.is_visible:
            self.root.withdraw()
            self.is_visible = False
    
    def toggle_visibility(self):
        """Toggle visibility."""
        if self.is_visible:
            self.hide()
        else:
            self.show()
    
    def toggle_lock(self):
        """Toggle line locking."""
        self.is_locked = not self.is_locked
        self.config_manager.config.is_locked = self.is_locked
        self.config_manager.save_config(self.config_manager.config)
    
    def add_line(self, x: int, y: int, is_horizontal: bool, 
                 color: str = "#00FF00", thickness: int = 2):
        """Add a new line."""
        self.line_manager.add_line(x, y, is_horizontal, color, thickness)
        self.config_manager.config.lines = self._lines_to_config()
        self.config_manager.save_config(self.config_manager.config)
    
    def clear_all_lines(self):
        """Clear all lines."""
        self.line_manager.clear_lines()
        self.config_manager.clear_lines()
    
    def change_line_color(self, line_index: int):
        """Open color picker for a line."""
        if 0 <= line_index < len(self.line_manager.lines):
            current_color = self.line_manager.lines[line_index].color
            color = colorchooser.askcolor(color=current_color, title="Choose Line Color")
            if color[1]:
                self.line_manager.lines[line_index].color = color[1]
                self.config_manager.config.lines = self._lines_to_config()
                self.config_manager.save_config(self.config_manager.config)
    
    def get_root(self):
        """Get the Tkinter root window."""
        return self.root
    
    def run(self):
        """Start the application main loop."""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Error in mainloop: {e}")
