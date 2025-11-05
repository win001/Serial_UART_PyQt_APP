# Serial UART Terminal - TODO List

## ✅ Completed Features
- [x] Dynamic window and element alignment
- [x] Custom baud rate support
- [x] Enter key sends data from send box
- [x] Dropdown menu for line endings (CR, LF, CR+LF, None)
- [x] Save last-used settings in config file (QSettings)
- [x] HEX send mode
- [x] HEX display mode
- [x] Timestamp support
- [x] Save log to file

## 🔧 Current Priorities
- [ ] Check if hex receive is enabled when non-hex data received (validation/warning)
- [ ] Hex input formatting improvements (auto-spacing, validation)
- [ ] Make executable app for Windows, Mac, and Linux
- [ ] UI Testing
- [ ] Update Notion and add README.md
- [ ] Name the application

## 🚀 Future Enhancements (Inspired by Docklight/Putty/Arduino IDE)

### Core Features
- [ ] **Auto-reconnect** - Automatically reconnect when device unplugs/replugs
- [ ] **Send File** - Send text/binary files over UART
- [ ] **Data Filters** - Filter incoming data by keywords/patterns
- [ ] **Search in Terminal** - Find text in received data (Ctrl+F)
- [ ] **Color Highlighting** - Highlight specific keywords or patterns
- [ ] **Multiple Tabs** - Connect to multiple COM ports simultaneously
- [ ] **Data Statistics** - Show bytes sent/received, data rate, uptime

### Advanced Serial Features
- [ ] **Flow Control** - Hardware (RTS/CTS) and Software (XON/XOFF) flow control
- [ ] **Pin Status Monitor** - Display DTR, RTS, CTS, DSR, DCD, RI status
- [ ] **Parity & Stop Bits** - Configurable parity (None/Even/Odd) and stop bits
- [ ] **Break Signal** - Send break signal to device
- [ ] **Data Bits** - Support for 5, 6, 7, 8 data bits

### Automation & Testing
- [ ] **Quick Send Buttons/Macros** - Predefined commands with keyboard shortcuts
- [ ] **Auto-Response Rules** - Automatically respond when specific data received
- [ ] **Script Support** - Python scripting for automated testing
- [ ] **Send Sequences** - Schedule repeated commands with delays
- [ ] **Protocol Decoder** - Decode common protocols (Modbus, JSON, custom)
- [ ] **Packet Analyzer** - Parse and display structured data packets

### Data Management
- [ ] **Auto-logging** - Automatically save all sessions to timestamped files
- [ ] **Log Rotation** - Limit log file size with auto-rotation
- [ ] **Export Formats** - Export logs as CSV, JSON, HTML
- [ ] **Session Playback** - Replay saved sessions
- [ ] **Data Comparison** - Compare two log files side-by-side

### File Transfer Protocols
- [ ] **XMODEM/YMODEM/ZMODEM** - Binary file transfer protocols
- [ ] **Intel HEX** - Send/receive Intel HEX files for firmware updates
- [ ] **Binary File Support** - Send/receive raw binary files

### UI/UX Improvements
- [ ] **Dark Mode** - Toggle between light/dark themes
- [ ] **Customizable Colors** - User-defined TX/RX colors
- [ ] **Font Customization** - Size, family, and style settings
- [ ] **Toolbar** - Quick access buttons for common actions
- [ ] **Status Bar** - Connection status, baud rate, byte counts
- [ ] **Split View** - Separate TX and RX windows
- [ ] **Profiles/Sessions** - Save and load connection profiles
- [ ] **Keyboard Shortcuts** - Customizable hotkeys

### Network & Advanced Connectivity
- [ ] **TCP/UDP Terminal** - Connect via network sockets
- [ ] **Telnet Client** - Basic Telnet support
- [ ] **SSH Client** - Secure shell connections
- [ ] **Bluetooth Serial** - Connect to Bluetooth SPP devices
- [ ] **USB-to-Serial Bridge** - Enhanced USB device detection

### Developer Tools
- [ ] **Plugin System** - Support for user-created plugins
- [ ] **API/CLI Mode** - Command-line interface for automation
- [ ] **Regex Testing** - Test regex patterns on live data
- [ ] **Data Generator** - Generate test data patterns
- [ ] **Checksum Calculator** - Calculate CRC, checksum for data

## 💡 Unique Features (Not in other apps)
- [ ] **AI Assistant Integration** - Parse logs with AI for debugging
- [ ] **Real-time Data Plotting** - Graph numeric data streams
- [ ] **Voice Commands** - Send commands via speech recognition
- [ ] **Mobile Companion App** - Control via smartphone
- [ ] **Cloud Sync** - Sync settings and macros across devices
- [ ] **Collaborative Mode** - Share terminal session with team members
- [ ] **IoT Dashboard** - Visual widgets for sensor data monitoring

## 🐛 Bug Fixes & Maintenance
- [ ] Error handling for invalid baud rates (partially implemented)
- [ ] Memory optimization for large log files
- [ ] Handle COM port disconnection gracefully
- [ ] Cross-platform testing