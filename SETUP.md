# UART Serial Terminal - Setup Guide

## Prerequisites
- Python 3.6 or higher installed on your system

## Installation

### 1. Create Virtual Environment

Open a terminal/command prompt in the project directory and run:

**Windows:**
```bash
python -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal prompt indicating the virtual environment is active.

### 3. Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- PyQt5 (5.15.9) - GUI framework
- pyserial (3.5) - Serial communication library

### 4. Run the Application

```bash
python serial_terminal.py
```

## Deactivating Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

### PyQt5 Installation Issues on Linux
If you encounter issues installing PyQt5 on Linux, you may need to install system dependencies:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-pyqt5
```

**Fedora:**
```bash
sudo dnf install python3-qt5
```

### Serial Port Access on Linux
You may need to add your user to the dialout group:
```bash
sudo usermod -a -G dialout $USER
```
(Log out and log back in for changes to take effect)

## Development

### Regenerating UI File
If you modify the `serial_terminal.ui` file in Qt Designer, regenerate the Python UI code:

```bash
pyuic5 serial_terminal.ui -o serial_terminal_ui.py
```

Note: You'll need to install `pyqt5-tools` for this:
```bash
pip install pyqt5-tools
```
