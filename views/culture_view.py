from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QSplitter
from views.culture_view_personal_journal import CultureViewPersonalJournal
from views.culture_view_field_notes import CultureViewFieldNotes
from views.culture_view_field_journal import CultureViewFieldJournal
from views.culture_view_contact_journal import CultureViewContactJournal

class CultureView(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        # Create the tab widget
        self.tab_widget = QTabWidget()

        # Create the CultureViewFieldNotes and CultureViewFieldJournal widgets
        self.field_notes = CultureViewFieldNotes(controller)
        self.field_journal = CultureViewFieldJournal(controller)

        # Add the widgets to the tab widget
        self.tab_widget.addTab(self.field_notes, "Field Notes")
        self.tab_widget.addTab(self.field_journal, "Field Journal")
        self.tab_widget.addTab(CultureViewPersonalJournal(controller), "Personal Journal")
        self.tab_widget.addTab(CultureViewContactJournal(controller), "Contact Journal")

        # Set icons for the tabs
        self.tab_widget.setTabIcon(0, QIcon("assets/icons/notes_white.svg"))
        self.tab_widget.setTabIcon(1, QIcon("assets/icons/journal_white.svg"))
        self.tab_widget.setTabIcon(2, QIcon("assets/icons/personal_white.svg"))
        self.tab_widget.setTabIcon(3, QIcon("assets/icons/contact_white.svg"))

        # Add the tab widget to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def open_notes_split_view(self):
        print("Open Notes Split View")
        # Remove the current central widget
        self.parent().setCentralWidget(None)

        # Create the split view
        split_view = QSplitter(Qt.Horizontal, self.parent())
        split_view.addWidget(CultureViewFieldNotes(self.controller, in_split_view=True))
        split_view.addWidget(CultureViewFieldJournal(self.controller, in_split_view=True))

        # Set the initial sizes of the widgets
        split_view.setSizes([100, 100])

        # Set the split view as the central widget
        self.parent().setCentralWidget(split_view)

    def open_culture_view(self):
        print("Open Culture View")
        # Remove the current central widget
        self.parent().setCentralWidget(None)

        # Create a new instance of CultureView and set it as the central widget
        culture_view = CultureView(self.controller)
        self.parent().setCentralWidget(culture_view)