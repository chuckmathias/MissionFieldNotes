from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMenu

class CulturePersonalJournalMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the File menu
        file_menu = self.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")

        # Create the Edit menu
        edit_menu = self.addMenu("Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        # Create the View menu
        view_menu = self.addMenu("View")

        culture_view_action = QAction("Culture View", self)
        # culture_view_action.triggered.connect(self.main_window.open_culture_view)

        notes_split_view_action = QAction("Notes Split View", self)
        # notes_split_view_action.triggered.connect(self.main_window.open_notes_split_view)

        view_menu.addAction(culture_view_action)
        view_menu.addAction(notes_split_view_action)