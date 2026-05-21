"""Main entry point for the Screen Overlay Grid application."""

import sys
import threading
from config import ConfigManager
from overlay_window import OverlayWindow
from tray import TrayMenu


def main():
    """Initialize and run the application."""
    # Load configuration
    config = ConfigManager()
    
    # Create overlay window
    overlay = OverlayWindow(config)
    
    # Show overlay if configured to do so
    if config.config.show_on_startup:
        overlay.show()
    
    # Create tray menu
    tray_menu = TrayMenu(overlay, config)
    
    # Start tray icon in a separate thread
    tray_thread = threading.Thread(target=tray_menu.run, daemon=True)
    tray_thread.start()
    
    # Run the main application loop
    try:
        overlay.run()
    except KeyboardInterrupt:
        print("Shutting down...")
        tray_menu.stop()
        sys.exit(0)


if __name__ == "__main__":
    main()
