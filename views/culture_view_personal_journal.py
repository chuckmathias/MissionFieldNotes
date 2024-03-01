from ui.culture_personal_journal_menu import CulturePersonalJournalMenu
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateTimeEdit, QTextEdit, QComboBox
from PySide6.QtCore import QDateTime
import json

class CultureViewPersonalJournal(QWidget):
     def __init__(self, controller, in_split_view=False):
        super().__init__()

        self.controller = controller
        
        # Create a QVBoxLayout for the QWidget
        layout = QVBoxLayout()

        # Create a QMenuBar
        menu_bar = CulturePersonalJournalMenu(self)

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

        # Add a stretch to the QVBoxLayout
        layout.addStretch(1)

        # Set the QVBoxLayout as the layout for the QWidget
        self.setLayout(layout)