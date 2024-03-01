from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateTimeEdit, QTextEdit, QComboBox
from PySide6.QtCore import QDateTime
from ui.culture_field_notes_menu import CultureFieldNotesMenu
import json

class CultureViewFieldNotes(QWidget):
    def __init__(self, controller, in_split_view=False):
        super().__init__()

        self.controller = controller
        
        # Create a QVBoxLayout for the QWidget
        layout = QVBoxLayout()

        # Create a QMenuBar
        menu_bar = CultureFieldNotesMenu(self)

        # Add the QMenuBar to the QVBoxLayout
        layout.addWidget(menu_bar)
        
        # If in split view, add additional content
        if in_split_view:
            # Create a QLabel
            label = QLabel("Field Journal")

            # Add the QLabel to the QVBoxLayout
            layout.addWidget(label)

        # Create a QDateTimeEdit with the current date and time
        datetime_edit = QDateTimeEdit(QDateTime.currentDateTime())
        layout.addWidget(datetime_edit)

        # Create a QTextEdit
        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        # Create a QComboBox
        combo_box = QComboBox()

        # Load the categories or tags from a JSON file
        with open("categories.json") as f:
            categories = json.load(f)

        # Add the categories or tags to the QComboBox
        for category in categories:
            combo_box.addItem(category["name"])

        layout.addWidget(combo_box)

        # Add a stretch to the QVBoxLayout
        layout.addStretch(1)

        # Set the QVBoxLayout as the layout for the QWidget
        self.setLayout(layout)