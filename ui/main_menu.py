from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction

class MainMenu(QMenuBar):
    def __init__(self, parent=None):  # Add a parent argument
        super().__init__(parent)  # Pass the parent to the superclass constructor

        self.main_window = parent

        # Create the File menu
        file_menu = QMenu("File", self)
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")
        self.addMenu(file_menu)

        # Create the Edit menu
        edit_menu = QMenu("Edit", self)
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        self.addMenu(edit_menu)

        # Create the View menu

        culture_view_action = QAction("Culture View", self)
        culture_view_action.triggered.connect(self.main_window.open_culture_view)

        notes_split_view_action = QAction("Notes Split View", self)
        notes_split_view_action.triggered.connect(self.main_window.open_notes_split_view)


        view_menu = QMenu("View", self)
        view_menu.addAction(culture_view_action)
        view_menu.addAction(notes_split_view_action)

        self.addMenu(view_menu)