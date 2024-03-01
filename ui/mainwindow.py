from PySide6.QtWidgets import QMainWindow, QToolBar, QSplitter, QStatusBar, QLabel
from PySide6.QtGui import QAction, QIcon, QPixmap
from views.initial_view import InitialView
from views.culture_view import CultureView
from controllers.culture_controller import CultureController  # Import CultureController
from models.culture import Culture
from ui.main_menu import MainMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mission Field Notes")

        # Set the window icon
        self.setWindowIcon(QIcon('assets/images/mfn_logo_icon_white.svg'))


        # Create a Culture instance
        culture_model = Culture("Default Name")

        # Create a CultureController instance and store it in an attribute
        self.controller = CultureController(culture_model)

        # Create a CultureView instance and store it in an attribute
        self.culture_view = CultureView(self.controller)

        # Import the main menu
        self.setMenuBar(MainMenu(self))

        # Set up the main menu icons
        tool_bar = QToolBar()
        main_menu_icon = QAction("Main Menu Icon", self)
        tool_bar.addAction(main_menu_icon)
        self.addToolBar(tool_bar)

        # Set the CultureView instance as the central widget
        self.setCentralWidget(self.culture_view)
        # self.setCentralWidget(InitialView())  

        # Call the method to setup the status bar
        self.setupStatusBar()

    def open_notes_split_view(self):
        print("Open Notes Split View")
        # Check the type of the current central widget
        if isinstance(self.centralWidget(), CultureView):
            # If the current central widget is a CultureView, call the open_notes_split_view method
            self.centralWidget().open_notes_split_view()
        else:
            # If the current central widget is not a CultureView, create a new instance of CultureView and set it as the central widget
            culture_view = CultureView(self.controller)
            self.setCentralWidget(culture_view)
            culture_view.open_notes_split_view()

    def open_culture_view(self):
        print("Open Culture View")
        # Check the type of the current central widget
        if isinstance(self.centralWidget(), CultureView):
            # If the current central widget is a CultureView, call the open_culture_view method
            self.centralWidget().open_culture_view()
        else:
            # If the current central widget is not a CultureView, create a new instance of CultureView and set it as the central widget
            culture_view = CultureView(self.controller)
            self.setCentralWidget(culture_view)
            culture_view.open_culture_view()

    def setupStatusBar(self):
        # Create a QStatusBar
        self.status_bar = QStatusBar()

        # Set the QStatusBar as the status bar of the main window
        self.setStatusBar(self.status_bar)

        # Create a QLabel to hold the image
        self.image_label = QLabel()

        # Create a QPixmap from the image file
        pixmap = QPixmap("assets/images/mfn_logo_white.svg")

        # Scale the QPixmap
        pixmap = pixmap.scaledToHeight(30)

        # Set the QPixmap to the QLabel
        self.image_label.setPixmap(pixmap)

        # Add the QLabel to the QStatusBar
        self.status_bar.addWidget(self.image_label)

        # Set an initial message
        self.status_bar.showMessage("Ready")