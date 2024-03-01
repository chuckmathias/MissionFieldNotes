from PySide6.QtWidgets import QAction
from PySide6.QtGui import QIcon

class MainMenuIcon(QAction):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon('path_to_icon.png'))
        # Set up your icon action here