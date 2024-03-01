from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindow
import sys

def main():
    app = QApplication(sys.argv)

    # Load the stylesheet
    with open("ui/styles/stylesheet.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()