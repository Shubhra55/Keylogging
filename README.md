# 🖥️ Python Keylogger

A lightweight, cross-platform keylogger built using Python's `pynput` module. It records keystrokes, including key combinations and special keys, and writes them to a log file. A standalone `.exe` version is also provided for Windows systems.

---

## ⚠️ DISCLAIMER

> 🚨 This software is for **educational and ethical use only**.
>
> **Unauthorized use is illegal.** Always obtain **explicit permission** before deploying this on any system. Misuse of this software can lead to criminal prosecution under cybercrime laws.

---

## 📦 Features

- ✅ Logs all keyboard input (including Ctrl + keys)
- ✅ Detects key combinations like `Ctrl + Shift + Esc`
- ✅ `Esc` key immediately stops the logger
- ✅ Saves to `key_log.txt`
- ✅ Hides console window on Windows
- ✅ `.exe` version included for silent use

---

## 🔧 Installation (Python Version)

**Requirements**:
- Python 3.6+
- `pynput` module

```bash
pip install pynput
python keylogger.py
````

---

## 💻 Usage (.EXE Version)

1. Download the prebuilt `keylogger.exe`
2. Double-click to run silently in the background
3. To stop: press the `Esc` key
4. Logs will be saved to `key_log.txt` in the same folder

---

## ⚠️ Antivirus Note

* Some antivirus software may detect the `.exe` as suspicious.
* This is expected for programs that monitor keystrokes.
* You may need to whitelist the executable or run it in a VM for testing.

---

## 🗃️ Log Output

* File: `key_log.txt`
* Location: Same directory as script/exe
* Format: Timestamped log of each key pressed

---

## 🧱 Building Your Own `.exe`

You can build your own executable using `pyinstaller`:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile keylogger.py
```

* The `.exe` will be in the `dist/` folder.
* Use `--noconsole` to keep it hidden.

---

## 🧠 Potential Add-Ons

* 🔒 Encrypt log files
* 🖱️ Add mouse movement/click logging
* 📧 Send logs via email
* ⚙️ Auto-start on boot

---

## 🛑 Legal Use Warning

This software must **not** be used for spying or malicious activities. You are solely responsible for how you use this tool. Use it only in:

* Educational labs
* Cybersecurity testing
* Penetration testing (with written consent)

```

Creator : Shubhra Safi
