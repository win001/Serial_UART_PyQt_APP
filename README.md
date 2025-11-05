# Serial UART Terminal

A cross-platform UART serial terminal GUI application built with Python and PyQt5, similar to Arduino Serial Monitor, with additional features for HEX mode, feature for saving terminal data.

## Features

- **Multiple Display Modes**: ASCII and HEX display/send modes
- **Flexible Line Endings**: Support for CR, LF, CR+LF, or None
- **Timestamped Logs**: Optional timestamps for all received/transmitted data
- **Save Logs**: Export terminal sessions to text files
- **Persistent Settings**: Automatically saves last-used port, baud rate, and preferences
- **Real-time Communication**: 100ms polling for responsive data reception
- **Color-coded Output**: TX (blue) and RX (green) for easy identification
- **Dynamic Baud Rates**: Support for standard and custom baud rates (110-230400)

## Screenshots

*(Add screenshots here)*

## Installation

See [SETUP.md](SETUP.md) for detailed installation instructions.

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Serial_UART_QT_APP
   ```

2. **Run setup script** (Windows):
   ```bash
   setup.bat
   ```

3. **Or manual setup**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python serial_terminal.py
   ```

## Usage

1. **Select COM Port**: Choose your serial device from the dropdown
2. **Set Baud Rate**: Select or enter custom baud rate
3. **Connect**: Click "Connect" to establish connection
4. **Send Data**: Type in the send box and press Enter or click "Send"
5. **Save Logs**: Click "Save" to export your session

## Requirements

- Python 3.6+
- PyQt5 5.15.9
- pyserial 3.5

## Project Structure

```
Serial_UART_QT_APP/
├── assets/                  # Application assets
│   ├── app_icon.ico        # Windows application icon
│   └── app_icon.png        # Cross-platform icon
├── serial_terminal.py       # Main application logic
├── serial_terminal_ui.py    # Auto-generated UI code (from Qt Designer)
├── serial_terminal.ui       # Qt Designer UI file
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # This file
├── SETUP.md                # Detailed setup guide
├── TODO.md                 # Feature roadmap
├── setup.bat               # Windows setup script
└── run.bat                 # Windows launch script
```

## Development

### Modifying the UI

1. Edit `serial_terminal.ui` in Qt Designer
2. Regenerate Python code:
   ```bash
   pyuic5 serial_terminal.ui -o serial_terminal_ui.py
   ```

### Building Executable

*(Coming soon - PyInstaller configuration)*

## Contributing

Contributions are welcome! Please check [TODO.md](TODO.md) for planned features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vineet-kumar-99a332136/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/win001)

## Acknowledgments

- Inspired by Arduino Serial Monitor, Docklight, and PuTTY
- Built with PyQt5 and pyserial
