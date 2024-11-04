import cv2
import numpy as np
import pyautogui
import tkinter as tk
import subprocess

# Path to the template image you want to detect
template_path = "./images/castle.png"
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    print("Template image not found. Check the file path.")
    exit()
w, h = template.shape[::-1]  # Template dimensions

# Connect to the Nox emulator
def adb_connect():
    command = "adb connect 127.0.0.1:62001"
    subprocess.run(command, shell=True)

# Capture the screen of the Nox emulator
def capture_nox_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    return screenshot

# Detect template in the screenshot
def detect_template():
    screen = capture_nox_screen()
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locations = np.where(result >= threshold)
    if locations[0].size > 0:
        return locations[1][0], locations[0][0]  # (x, y) coordinates of the first match
    return None

# Function to send tap command via ADB
def adb_click(x, y):
    command = f"adb shell input tap {x} {y}"
    subprocess.run(command, shell=True)

# Main function to create a Tkinter overlay with a rectangle
def overlay_square():
    adb_connect()
    
    # Initialize Tkinter overlay window
    root = tk.Tk()
    root.attributes("-transparentcolor", "white")
    root.overrideredirect(True)  # Remove window borders
    root.wm_attributes("-topmost", True)  # Keep window on top
    root.config(bg="white")  # Background color for transparency

    # Create a canvas for drawing the overlay
    canvas = tk.Canvas(root, highlightthickness=0, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)  # Allow canvas to fill the window

    def update_overlay():
        # Get the screen size
        screen_width, screen_height = pyautogui.size()
        
        # Resize the Tkinter window to cover the full screen
        root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Clear previous drawings
        canvas.delete("all")

        # Detect template position
        detected_location = detect_template()
        if detected_location:
            x, y = detected_location
            
            # Print detected coordinates for debugging
            # print(f"Detected template at: ({x}, {y})")

            # Draw a rectangle at the detected position
            canvas.create_rectangle(x, y, x + w, y + h, outline="red", width=2)
            
            # Send a click command to ADB
            #adb_click(x, y)
        # Refresh overlay after a delay
        root.after(1, update_overlay)


    # Close the overlay when the user presses 'Esc'
    def close_overlay(event):
        root.quit()

    root.bind('<Escape>', close_overlay)  # Bind the escape key to close the overlay
    update_overlay()  # Initial call to update overlay
    root.mainloop()

# Run the overlay
overlay_square()