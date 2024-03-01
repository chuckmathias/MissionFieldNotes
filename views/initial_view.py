from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QListView
from PySide6.QtCore import Qt

class InitialView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        open_button = QPushButton("Open")
        new_button = QPushButton("Create New")

        recent_files_label = QLabel("Recent Files:")
        recent_files_list = QListView()  # You'll need to set up a model for this

        layout.addWidget(open_button, alignment=Qt.AlignCenter)
        layout.addWidget(new_button, alignment=Qt.AlignCenter)
        layout.addWidget(recent_files_label)
        layout.addWidget(recent_files_list)

        self.setLayout(layout)