#!/usr/bin/env python3
"""
Mouse Mover - A simple program that moves the mouse cursor every 5 seconds.
Close the window or click Stop to exit the program.
"""

import pyautogui
import time
import threading
import sys
import os
import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Windows-specific imports for sleep prevention
try:
    import ctypes
    from ctypes import wintypes
    import win32api
    import win32con
    import win32gui
    WINDOWS_AVAILABLE = True
except ImportError:
    WINDOWS_AVAILABLE = False

class MouseMover:
    def __init__(self):
        self.running = True
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Disable pyautogui's fail-safe (moving mouse to corner)
        pyautogui.FAILSAFE = False
        
        # Initialize sleep prevention
        self.setup_sleep_prevention()
        
        # Create GUI
        self.setup_gui()
        
        self.log_message("Mouse Mover Started!")
        self.log_message("The mouse will move every 5 seconds.")
        self.log_message("Close this window or click Stop to exit.")
        self.log_message(f"Screen size: {self.screen_width}x{self.screen_height}")
        if WINDOWS_AVAILABLE:
            self.log_message("✅ Windows sleep prevention enabled")
        else:
            self.log_message("⚠️ Windows sleep prevention not available")
        self.log_message("-" * 50)
    
    def setup_sleep_prevention(self):
        """Set up system-level sleep prevention."""
        if WINDOWS_AVAILABLE:
            try:
                # Prevent system from going to sleep
                ES_CONTINUOUS = 0x80000000
                ES_SYSTEM_REQUIRED = 0x00000001
                ES_DISPLAY_REQUIRED = 0x00000002
                
                # Set thread execution state to prevent sleep
                ctypes.windll.kernel32.SetThreadExecutionState(
                    ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
                )
                
                # Get current power scheme - handle gracefully if function not available
                try:
                    self.original_power_state = ctypes.windll.kernel32.GetThreadExecutionState()
                except AttributeError:
                    # Function not available on this Windows version
                    self.original_power_state = None
                    self.log_message("Note: Power state tracking not available on this Windows version")
                
            except Exception as e:
                self.log_message(f"Warning: Could not set sleep prevention: {e}")
                self.original_power_state = None
    
    def restore_power_settings(self):
        """Restore original power settings."""
        if WINDOWS_AVAILABLE and self.original_power_state is not None:
            try:
                # Restore original thread execution state
                ctypes.windll.kernel32.SetThreadExecutionState(self.original_power_state)
                self.log_message("Power settings restored")
            except Exception as e:
                self.log_message(f"Warning: Could not restore power settings: {e}")
        elif WINDOWS_AVAILABLE:
            # Just reset to normal state
            try:
                ES_CONTINUOUS = 0x80000000
                ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
                self.log_message("Power settings reset to normal")
            except Exception as e:
                self.log_message(f"Warning: Could not reset power settings: {e}")
    
    def prevent_sleep_activity(self):
        """Perform activities to prevent sleep mode."""
        try:
            # Method 1: Move mouse to random position
            x = random.randint(50, self.screen_width - 50)
            y = random.randint(50, self.screen_height - 50)
            pyautogui.moveTo(x, y, duration=0.5)
            
            # Method 2: Simulate a tiny mouse movement (more natural)
            pyautogui.moveRel(1, 0, duration=0.1)
            pyautogui.moveRel(-1, 0, duration=0.1)
            
            # Method 3: Simulate a tiny key press (invisible to user)
            pyautogui.press('numlock')  # Toggle numlock (usually invisible)
            pyautogui.press('numlock')  # Toggle back
            
            # Method 4: Windows-specific - simulate input
            if WINDOWS_AVAILABLE:
                try:
                    # Send a mouse event to the system
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 0, 0, 0)
                except:
                    pass
            
            self.log_message(f"Mouse moved to ({x}, {y}) + sleep prevention active")
            
        except Exception as e:
            self.log_message(f"Error in sleep prevention: {e}")
    
    def setup_gui(self):
        """Create the GUI window."""
        self.root = tk.Tk()
        self.root.title("Mouse Mover - Sleep Prevention")
        self.root.geometry("550x450")
        self.root.resizable(True, True)
        
        # Configure the window to handle close button
        self.root.protocol("WM_DELETE_WINDOW", self.stop_program)
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🖱️ Mouse Mover - Sleep Prevention", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="System Status", padding="5")
        status_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        status_frame.columnconfigure(1, weight=1)
        
        # Sleep prevention status
        ttk.Label(status_frame, text="Sleep Prevention:").grid(row=0, column=0, padx=(0, 5), sticky=tk.W)
        if WINDOWS_AVAILABLE:
            self.sleep_status = ttk.Label(status_frame, text="✅ Active", foreground="green", font=("Arial", 10, "bold"))
        else:
            self.sleep_status = ttk.Label(status_frame, text="⚠️ Not Available", foreground="orange", font=("Arial", 10, "bold"))
        self.sleep_status.grid(row=0, column=1, sticky=tk.W)
        
        # Activity status
        ttk.Label(status_frame, text="Activity:").grid(row=1, column=0, padx=(0, 5), sticky=tk.W)
        self.status_label = ttk.Label(status_frame, text="Running", foreground="green", font=("Arial", 10, "bold"))
        self.status_label.grid(row=1, column=1, sticky=tk.W)
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Activity Log", padding="5")
        log_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        # Text widget with scrollbar
        self.log_text = tk.Text(log_frame, height=15, width=70, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0)
        
        # Stop button
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_program)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Clear log button
        clear_button = ttk.Button(button_frame, text="Clear Log", command=self.clear_log)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Test sleep prevention button
        test_button = ttk.Button(button_frame, text="Test Sleep Prevention", command=self.test_sleep_prevention)
        test_button.pack(side=tk.LEFT, padx=5)
    
    def test_sleep_prevention(self):
        """Test the sleep prevention methods."""
        self.log_message("🧪 Testing sleep prevention methods...")
        self.prevent_sleep_activity()
        self.log_message("✅ Sleep prevention test completed")
    
    def log_message(self, message):
        """Add a message to the log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        # Update GUI in thread-safe way
        if hasattr(self, 'root'):
            self.root.after(0, self._update_log, full_message)
        else:
            print(full_message.strip())
    
    def _update_log(self, message):
        """Update the log text widget (called from main thread)."""
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        
        # Limit log size to prevent memory issues
        lines = self.log_text.get("1.0", tk.END).count('\n')
        if lines > 100:
            self.log_text.delete("1.0", "10.0")
    
    def clear_log(self):
        """Clear the log text."""
        self.log_text.delete("1.0", tk.END)
    
    def stop_program(self):
        """Stop the program and close the window."""
        self.running = False
        self.status_label.config(text="Stopped", foreground="red")
        self.sleep_status.config(text="🔄 Restoring...", foreground="orange")
        self.stop_button.config(text="Stopping...", state="disabled")
        self.log_message("Stopping Mouse Mover...")
        self.log_message("Restoring power settings...")
        
        # Restore power settings
        self.restore_power_settings()
        
        self.root.after(1000, self.root.destroy)  # Close window after 1 second
    
    def mouse_mover_thread(self):
        """Run the mouse moving logic in a separate thread."""
        while self.running:
            if self.running:  # Check again in case it changed
                self.prevent_sleep_activity()
            
            # Wait 5 seconds, but check every 0.1 seconds if we should exit
            for _ in range(50):  # 50 * 0.1 = 5 seconds
                if not self.running:
                    break
                time.sleep(0.1)
    
    def run(self):
        """Main program loop."""
        # Start mouse mover in a separate thread
        mover_thread = threading.Thread(target=self.mouse_mover_thread, daemon=True)
        mover_thread.start()
        
        try:
            # Start the GUI main loop
            self.root.mainloop()
        except Exception as e:
            self.log_message(f"Error in GUI: {e}")
        finally:
            self.running = False
            self.restore_power_settings()
            self.log_message("Mouse Mover stopped.")
            self.log_message("Goodbye!")

def main():
    """Main entry point."""
    try:
        mover = MouseMover()
        mover.run()
    except ImportError as e:
        print(f"Error: Missing required dependency - {e}")
        print("Please install required packages:")
        print("pip install pyautogui pywin32")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 