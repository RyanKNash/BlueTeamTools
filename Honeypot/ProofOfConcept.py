import os
import sys
import time
import platform
from tkinter import Tk, messagebox

def defensive_action():
    """
    Build your real countermeasures.
    Ideas:
    - Disable networking
    - Kill processes
    - Alert your server
    """
    print("[!] Defensive action triggered!")
    # Example placeholder
    # os.system("sudo ip link set eth0 down")  # Linux example
    # os.system("netsh interface set interface name=\"Wi-Fi\" admin=disabled")  # Windows example

def pop_up_alert():
    """Show a pop-up window to warn the attacker. For the purpose of testing"""
    root = Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning("Warning!", "Get out of here!")
    root.destroy()

def dummy_app():
    print("Welcome to honeypot v1.0")
    time.sleep(1)
    print("Initializing...")

    # Simulate normal operations
    for i in range(3):
        print(f"Processing task {i + 1}/3...")
        time.sleep(1)

    # Simulated tampering detection
    tampering_detected = True  # Set to False to disable for now

    if tampering_detected:
        print("[!] Tampering detected!")
        pop_up_alert()  # Show pop-up
        defensive_action()  # Call the defensive action placeholder
    else:
        print("All operations normal.")

if __name__ == "__main__":
    try:
        dummy_app()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting...")
        sys.exit(0)
