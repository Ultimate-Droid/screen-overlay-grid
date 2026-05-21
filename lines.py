"""Line data model and utilities."""

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Line:
    """Represents a single line on the overlay."""
    x: int
    y: int
    is_horizontal: bool
    color: str = "#00FF00"
    thickness: int = 2
    opacity: int = 255
    
    def get_bounds(self, screen_width: int, screen_height: int, sensitivity: int = 10):
        """Get clickable bounds around the line for dragging."""
        if self.is_horizontal:
            return {
                'x1': 0,
                'y1': max(0, self.y - sensitivity),
                'x2': screen_width,
                'y2': min(screen_height, self.y + sensitivity)
            }
        else:
            return {
                'x1': max(0, self.x - sensitivity),
                'y1': 0,
                'x2': min(screen_width, self.x + sensitivity),
                'y2': screen_height
            }
    
    def contains_point(self, px: int, py: int, sensitivity: int = 10) -> bool:
        """Check if a point is near the line."""
        bounds = self.get_bounds(99999, 99999, sensitivity)
        return (bounds['x1'] <= px <= bounds['x2'] and
                bounds['y1'] <= py <= bounds['y2'])
    
    def move_to(self, px: int, py: int, screen_width: int, screen_height: int):
        """Move line to a new position based on point."""
        if self.is_horizontal:
            self.y = max(0, min(screen_height - 1, py))
        else:
            self.x = max(0, min(screen_width - 1, px))


class LineManager:
    """Manages all lines on the overlay."""
    
    def __init__(self):
        self.lines: List[Line] = []
        self.dragging_line_index: Optional[int] = None
    
    def add_line(self, x: int, y: int, is_horizontal: bool, 
                 color: str = "#00FF00", thickness: int = 2) -> int:
        """Add a line and return its index."""
        line = Line(x, y, is_horizontal, color, thickness)
        self.lines.append(line)
        return len(self.lines) - 1
    
    def remove_line(self, index: int):
        """Remove a line by index."""
        if 0 <= index < len(self.lines):
            self.lines.pop(index)
    
    def get_line_at_point(self, px: int, py: int, sensitivity: int = 10) -> Optional[int]:
        """Find line index at a given point, returns None if no line."""
        for i, line in enumerate(self.lines):
            if line.contains_point(px, py, sensitivity):
                return i
        return None
    
    def start_drag(self, line_index: int):
        """Start dragging a line."""
        self.dragging_line_index = line_index
    
    def end_drag(self):
        """End dragging."""
        self.dragging_line_index = None
    
    def drag_line(self, px: int, py: int, screen_width: int, screen_height: int):
        """Drag the currently selected line."""
        if self.dragging_line_index is not None:
            line = self.lines[self.dragging_line_index]
            line.move_to(px, py, screen_width, screen_height)
    
    def clear_lines(self):
        """Remove all lines."""
        self.lines.clear()
        self.dragging_line_index = None
    
    def get_horizontal_lines(self) -> List[Line]:
        """Get all horizontal lines."""
        return [line for line in self.lines if line.is_horizontal]
    
    def get_vertical_lines(self) -> List[Line]:
        """Get all vertical lines."""
        return [line for line in self.lines if not line.is_horizontal]
