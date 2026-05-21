"""Test suite to verify core functionality."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from lines import LineManager, Line
from config import ConfigManager, LineConfig, AppConfig


def test_line_manager():
    """Test line manager functionality."""
    print("Testing LineManager...")
    
    manager = LineManager()
    
    # Test adding lines
    h_index = manager.add_line(0, 100, True, "#FF0000", 2)
    v_index = manager.add_line(500, 0, False, "#00FF00", 2)
    
    assert len(manager.lines) == 2, "Should have 2 lines"
    assert manager.lines[h_index].is_horizontal, "Line should be horizontal"
    assert not manager.lines[v_index].is_horizontal, "Line should be vertical"
    
    # Test getting lines at point
    line_at_100 = manager.get_line_at_point(300, 100, sensitivity=15)
    assert line_at_100 == h_index, "Should detect horizontal line at y=100"
    
    line_at_500 = manager.get_line_at_point(500, 300, sensitivity=15)
    assert line_at_500 == v_index, "Should detect vertical line at x=500"
    
    # Test filtering
    h_lines = manager.get_horizontal_lines()
    v_lines = manager.get_vertical_lines()
    assert len(h_lines) == 1 and len(v_lines) == 1, "Should filter lines correctly"
    
    # Test dragging
    manager.start_drag(h_index)
    manager.drag_line(300, 150, 1920, 1080)
    assert manager.lines[h_index].y == 150, "Line should move to y=150"
    manager.end_drag()
    
    # Test removal
    manager.remove_line(h_index)
    assert len(manager.lines) == 1, "Should have 1 line after removal"
    
    print("✓ LineManager tests passed!")


def test_config_manager():
    """Test configuration management."""
    print("Testing ConfigManager...")
    
    manager = ConfigManager()
    
    # Test adding lines
    manager.add_line(100, 200, True, "#FF0000", 2)
    manager.add_line(500, 0, False, "#00FF00", 3)
    
    assert len(manager.config.lines) == 2, "Should have 2 lines in config"
    
    # Test updating line
    manager.update_line(0, color="#FFFFFF", thickness=4)
    assert manager.config.lines[0].color == "#FFFFFF", "Color should be updated"
    assert manager.config.lines[0].thickness == 4, "Thickness should be updated"
    
    # Test clearing
    manager.clear_lines()
    assert len(manager.config.lines) == 0, "Should have 0 lines after clear"
    
    # Test persistence (verify config file exists)
    import os
    config_file = manager.config_file
    assert os.path.exists(config_file), "Config file should exist"
    
    print("✓ ConfigManager tests passed!")


def test_line_config():
    """Test line configuration object."""
    print("Testing LineConfig...")
    
    line = LineConfig(
        x=100,
        y=200,
        is_horizontal=True,
        color="#FF0000",
        thickness=3,
        opacity=200
    )
    
    assert line.x == 100, "X should be 100"
    assert line.y == 200, "Y should be 200"
    assert line.is_horizontal, "Should be horizontal"
    assert line.color == "#FF0000", "Color should be red"
    assert line.thickness == 3, "Thickness should be 3"
    assert line.opacity == 200, "Opacity should be 200"
    
    print("✓ LineConfig tests passed!")


def test_app_config():
    """Test app configuration object."""
    print("Testing AppConfig...")
    
    config = AppConfig(
        window_width=1920,
        window_height=1080,
        grid_mode="grid",
        is_locked=False
    )
    
    assert config.window_width == 1920, "Width should be 1920"
    assert config.window_height == 1080, "Height should be 1080"
    assert config.grid_mode == "grid", "Grid mode should be 'grid'"
    assert not config.is_locked, "Should not be locked"
    assert config.lines == [], "Lines should be empty list"
    
    print("✓ AppConfig tests passed!")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*50)
    print("Running Screen Overlay Grid Test Suite")
    print("="*50 + "\n")
    
    try:
        test_line_config()
        test_app_config()
        test_line_manager()
        test_config_manager()
        
        print("\n" + "="*50)
        print("✓ All tests passed successfully!")
        print("="*50 + "\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
