# MouseMover - Sleep Prevention Tool

A powerful program that moves your mouse every 5 seconds and **prevents your computer from going to sleep** using multiple system-level methods.

## 🖥️ **For Windows Users**

1. **Run `MouseMover-Windows.exe`**
2. A GUI window will open showing the activity log
3. Your mouse will move automatically every 5 seconds
4. **Click "Stop" or close the window** to exit

## 🍎 **For Mac Users**

1. **Install Python** (if not already installed):
   - Download from [python.org](https://python.org) or use `brew install python3`

2. **Install dependencies**:
   ```bash
   pip3 install pyautogui
   ```

3. **Run the program**:
   ```bash
   python3 mouse_mover.py
   ```

4. A GUI window will open - **click "Stop" or close the window** to exit

### Alternative for Mac: Build Your Own Executable
```bash
chmod +x build_mac.sh
./build_mac.sh
```
Then run the created `MouseMover-Mac` file.

## 🎯 **What It Does**

- **🖱️ Moves your mouse** to random positions every 5 seconds
- **🔒 Prevents sleep mode** using Windows system APIs
- **💤 Keeps computer awake** even during long periods of inactivity
- **🖥️ Prevents screen savers** from activating
- **📊 Shows real-time activity log** in a beautiful GUI window
- **🎯 Safe positioning** (avoids screen edges)
- **🧪 Multiple fallback methods** ensure maximum effectiveness

## ❓ **Need Help?**

- Make sure you have Python 3.6+ installed
- On Mac, you might need to allow the app in Security & Privacy settings
- The program is completely safe and only moves your mouse cursor

---
*Created with ❤️ - Enjoy keeping your computer awake!* 