from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QScrollArea, QDateTimeEdit, QTextEdit, QFileDialog
from ui.culture_contact_journal_menu import CultureContactJournalMenu
from PySide6.QtGui import QPixmap

class CultureViewContactJournal(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        # Create a QVBoxLayout for the QWidget
        layout = QVBoxLayout()

        # Create an instance of CultureFieldNotesMenu
        menu_bar = CultureContactJournalMenu()

        # Add the QMenuBar to the QVBoxLayout
        layout.addWidget(menu_bar)

        # Create a form layout for the contact details
        form_layout = QFormLayout()

        # Create widgets for the contact details
        self.image_label = QLabel()
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        self.name_edit = QLineEdit()
        self.pronunciation_edit = QLineEdit()
        self.meeting_edit = QTextEdit()
        self.general_info_edit = QTextEdit()
        self.prayer_requests_edit = QTextEdit()
        self.notes_edit = QTextEdit()

        # Add the widgets to the form layout
        form_layout.addRow("Image", self.image_label)
        form_layout.addRow("", self.upload_button)
        form_layout.addRow("Name", self.name_edit)
        form_layout.addRow("Name (Pronunciation)", self.pronunciation_edit)
        form_layout.addRow("Meeting", self.meeting_edit)
        form_layout.addRow("General Info", self.general_info_edit)
        form_layout.addRow("Prayer Requests", self.prayer_requests_edit)
        form_layout.addRow("Notes", self.notes_edit)

        # Create a QWidget and set the form layout as its layout
        form_widget = QWidget()
        form_widget.setLayout(form_layout)

        # Create a QScrollArea and set the form widget as its widget
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(form_widget)

        # Add the scroll area to the QVBoxLayout
        layout.addWidget(scroll_area)

        # Set the QVBoxLayout as the layout for the QWidget
        self.setLayout(layout)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.image_label.setPixmap(QPixmap(file_name))