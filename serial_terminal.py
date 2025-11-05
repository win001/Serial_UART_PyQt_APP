import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSettings
from serial_terminal_ui import Ui_MainWindow

class SerialTerminal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("assets/app_icon.ico"))
        self.setWindowTitle("Serial Terminal")
        self.serial = serial.Serial()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        font = QtGui.QFont("Courier New")
        self.ui.textReceive.setFont(font)

        self.received_log = []
        self.ui.btnSaveLog.clicked.connect(self.save_log)

        # Populate available COM ports
        self.refresh_ports()

        # Connect signals
        self.ui.btnConnect.clicked.connect(self.toggle_connection)
        self.ui.btnSend.clicked.connect(self.send_data)
        self.ui.lineSend.returnPressed.connect(self.send_data)
        self.ui.btnRefresh.clicked.connect(self.refresh_ports)
        self.ui.btnClear.clicked.connect(self.clear_text)

        # Default settings
        # self.ui.comboLineEnding.clear()
        self.ui.comboLineEnding.addItems([
            "CR+LF (\\r\\n)",
            "CR (\\r)",
            "LF (\\n)",
            "None"
        ])
        self.ui.comboLineEnding.setCurrentText("CR+LF (\r\n)")


        # Default baud rates
        # self.ui.comboBaud.clear()
        self.ui.comboBaud.addItems(["9600", "19200", "38400", "57600", "115200"])
        self.ui.comboBaud.setCurrentText("9600")

        self.settings = QSettings("MyCompany", "SerialTerminal")
        self.load_settings()


    def refresh_ports(self):
        ports = serial.tools.list_ports.comports()
        self.ui.comboPort.clear()
        for port in ports:
            self.ui.comboPort.addItem(port.device)

    def toggle_connection(self):
        if self.serial.is_open:
            self.serial.close()
            self.ui.btnConnect.setText("Connect")
        else:
            # port = self.ui.comboPort.currentText()
            try:
                baud = int(self.ui.comboBaud.currentText())
                if baud < 110 or baud > 230400:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Invalid Baudrate",
                        "Baud rate must be between 110 and 230400."
                    )
                    return
            except ValueError:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Invalid Baudrate",
                    f"'{baud_text}' is not a valid number."
                )
                return

            try:
                self.serial.port = self.ui.comboPort.currentText()
                self.serial.baudrate = baud
                self.serial.open()
                self.ui.btnConnect.setText("Disconnect")
                self.timer.start(100)
            except serial.SerialException as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def send_data(self):
        if not self.serial.is_open:
            QtWidgets.QMessageBox.warning(self, "Connection Error", "Serial port is not open.")
            return

        data = self.ui.lineSend.text()
        line_ending = ""
        ending_option = self.ui.comboLineEnding.currentText()

        # Determine line ending
        if "CR+LF" in ending_option:
            line_ending = "\r\n"
        elif "CR" in ending_option:
            line_ending = "\r"
        elif "LF" in ending_option:
            line_ending = "\n"

        # Send in HEX mode
        if self.ui.checkHexSend.isChecked():
            try:
                # Convert hex string to bytes
                bytes_data = bytes.fromhex(data)

                # Add line ending bytes (if any)
                bytes_data += line_ending.encode()
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Hex Error", "Invalid hex string.")
                return
            tx_text = ' '.join(f'{b:02X}' for b in bytes_data)
        else:
            # String mode with selected line ending
            full_text = data + line_ending
            bytes_data = full_text.encode()
            tx_text = full_text

        # Send over serial
        self.serial.write(bytes_data)

        # Log the transmission
        if self.ui.checkTimestampClear.isChecked():
            timestamp = QtCore.QDateTime.currentDateTime().toString("[hh:mm:ss] ")
        else:
            timestamp = ""
        self.ui.textReceive.setTextColor(QtGui.QColor("blue"))
        self.ui.textReceive.append(f"{timestamp} TX: {tx_text}")
        self.ui.textReceive.moveCursor(QtGui.QTextCursor.End)
        self.ui.textReceive.setTextColor(QtGui.QColor("black"))
        self.received_log.append(f"{timestamp} TX: {tx_text}")


    def read_data(self):
        if self.serial.is_open and self.serial.in_waiting:
            try:
                data = self.serial.read(self.serial.in_waiting)
                if self.ui.checkHexDisplay.isChecked():
                    text = ' '.join(f'{b:02X}' for b in data)
                else:
                    text = data.decode(errors='ignore')

                if self.ui.checkTimestampClear.isChecked():
                    timestamp = QtCore.QDateTime.currentDateTime().toString("[hh:mm:ss] ")
                else:
                    timestamp = ""
                log_line = f"{timestamp} RX: {text}"
                self.ui.textReceive.setTextColor(QtGui.QColor("green"))  # RX
                self.ui.textReceive.append(log_line)
                self.received_log.append(log_line)

            except serial.SerialException as e:
                QtWidgets.QMessageBox.critical(self, "Serial Error", str(e))
                self.serial.close()
                self.ui.btnConnect.setText("Connect")


    def save_log(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Log", "", "Text Files (*.txt)")
        if path:
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.received_log))
            QtWidgets.QMessageBox.information(self, "Saved", "Log saved successfully.")

    def clear_text(self):
        self.ui.textReceive.clear()
        self.received_log.clear()

    def save_settings(self):
        self.settings.setValue("port", self.ui.comboPort.currentText())
        self.settings.setValue("baud", self.ui.comboBaud.currentText())
        self.settings.setValue("lineEnding", self.ui.comboLineEnding.currentText())
        self.settings.setValue("hexSend", self.ui.checkHexSend.isChecked())
        self.settings.setValue("hexDisplay", self.ui.checkHexDisplay.isChecked())
        self.settings.setValue("windowSize", self.size())
        self.settings.setValue("windowPos", self.pos())

    def load_settings(self):
        self.ui.comboPort.setCurrentText(self.settings.value("port", ""))
        self.ui.comboBaud.setCurrentText(self.settings.value("baud", "9600"))
        self.ui.comboLineEnding.setCurrentText(self.settings.value("lineEnding", "CR+LF (\\r\\n)"))
        self.ui.checkHexSend.setChecked(self.settings.value("hexSend", False, type=bool))
        self.ui.checkHexDisplay.setChecked(self.settings.value("hexDisplay", False, type=bool))

        # Optional: Restore window geometry
        size = self.settings.value("windowSize")
        pos = self.settings.value("windowPos")
        if size and pos:
            self.resize(size)
            self.move(pos)

    def closeEvent(self, event):
        self.save_settings()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SerialTerminal()
    # window.show()
    window.showMaximized()
    sys.exit(app.exec_())
