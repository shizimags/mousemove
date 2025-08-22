# MouseMover

A simple Python program that automatically moves your mouse cursor every 5 seconds to prevent screen savers or keep your system active.

## Features

- 🖱️ Moves mouse cursor to random positions every 5 seconds
- 🖥️ **Easy-to-use GUI window** with Stop button and activity log
- ❌ **Close window or click Stop** to exit the program
- 🖥️ Works on Windows and Mac
- 📦 Available as standalone executables
- 🎯 Smart positioning (avoids screen edges)
- 📊 Real-time activity logging in GUI
- 🎨 Clean, modern interface

## Quick Start

### Option 1: Download Pre-built Zips

#### Windows
1. Download `MouseMover-Share/MouseMover-Windows.zip`
2. Unzip it
3. Double-click `MouseMover-Windows.exe`
4. If SmartScreen warns, click "More info" → "Run anyway"
5. **A GUI window will open** showing the activity log; click "Stop" or close to exit

#### Mac (Apple Silicon)
1. Download `MouseMover-Share/MouseMover-Mac.zip`
2. Unzip it
3. Right-click `MouseMover-Mac.app` → Open → Open (first run)
4. Grant Accessibility permission if prompted: System Settings → Privacy & Security → Accessibility
5. **A GUI window will open** showing the activity log; click "Stop" or close to exit

### Option 2: Run Python Script

1. Install dependencies:
   ```bash
   pip install pyautogui
   ```

2. Run the script:
   ```bash
   python mouse_mover.py
   ```

3. **A GUI window will open** - click "Stop" or close the window to exit

## Building Executables

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name MouseMover-Windows mouse_mover.py
```

### Mac
Run the provided build script:
```bash
chmod +x build_mac.sh
./build_mac.sh
```

Or manually:
```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed --name MouseMover-Mac mouse_mover.py
```

## How It Works

1. **GUI Interface**: Opens a user-friendly window with activity log and controls
2. **Mouse Movement**: The program generates random coordinates within your screen bounds (with 50-pixel margins from edges)
3. **Smooth Motion**: Mouse moves smoothly to new positions over 0.5 seconds
4. **Timing**: Waits exactly 5 seconds between movements
5. **Exit Handling**: Click "Stop" button or close the window to exit cleanly
6. **Activity Log**: Real-time logging of all mouse movements with timestamps
7. **Safety**: Includes error handling and graceful shutdown

## Dependencies

- `pyautogui` - For mouse control
- `tkinter` - For GUI interface (included with Python)
- `pyinstaller` - For creating executables (build only)

## Troubleshooting

### Permission Issues (Mac)
If you get a security warning on Mac:
1. Right-click the executable → "Open"
2. Or go to System Preferences → Security & Privacy → Allow

### Python Not Found
Make sure Python 3.6+ is installed:
- Windows: Download from [python.org](https://python.org)
- Mac: Use `brew install python3` or download from [python.org](https://python.org)

### Dependencies Installation Issues
Try using `pip3` instead of `pip`:
```bash
pip3 install pyautogui
```

## Technical Details

- **Language**: Python 3.6+
- **Architecture**: Cross-platform (Windows, Mac, Linux)
- **GUI Framework**: Tkinter (built into Python)
- **Threading**: Uses background thread for mouse movement
- **Screen Detection**: Automatically detects screen resolution
- **Fail-safe**: Disabled PyAutoGUI's corner fail-safe for uninterrupted operation

## Safety Notes

- The program moves your mouse automatically - be aware of this when running
- **Click "Stop" button or close the window** to exit cleanly
- The program includes error handling for unexpected situations
- Screen edges are avoided (50-pixel margin)
- GUI window shows real-time status and activity log

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues:
1. Make sure all dependencies are installed
2. Check that you have proper permissions
3. Verify Python version compatibility (3.6+)
4. Try running as administrator/sudo if needed 