import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QMenu

import sys
from random import choice

window_titles = [
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Gay | Website',
    'Still Gay | Website',
    'Still Gay | Website',
    'Still Gay | Website',
    'Still Gay | Website',
    'Still Gay | Website',
    'Still Gay | Website',
    'What on earth, this is still Gay | Website!!!!!',
    'What on earth, this is still Gay | Website!!!!!',
    'What on earth, this is still Gay | Website!!!!!',
    'What on earth, this is still Gay | Website!!!!!',
    'This is surprising, but it is still Gay | Website......',
    'This is surprising, but it is still Gay | Website......',
    'Uh I am cumming!'
]


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.show()

        self.W = 600
        self.H = 450
        self.button_is_checked = False
        self.times = 0

        self.setWindowTitle("Gay | Website")

        self.button = QPushButton('Kликабельно')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.windowTitleChanged.connect(self.windo)
        # self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.papa_label = QLabel()

        self.label = QLabel()
        self.snd_label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.snd_label.setText)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.snd_label)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(self.W, self.H))

        self.setCentralWidget(container)

    def contextMenuEvent(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, e):
        e.ignore()
        if e.button() == Qt.MouseButton.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText("окак")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText("mousePressEvent RIGHT")

    def windo(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Uh I am cumming!':
            self.button.setDisabled(True)

    def the_button_was_clicked(self):
        print("Ооооо, пошло дело, пошло!!")
        new_title = choice(window_titles)
        print("Setting title:  %s" % new_title)
        self.setWindowTitle(new_title)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(f'Переключена?: {self.button_is_checked}')

        if checked:
            self.W += 100
            self.H += 100
        else:
            self.W -= 100
            self.H -= 100

        self.setFixedSize(QSize(self.W, self.H))

    # def the_button_was_released(self):
    #     self.button_is_checked = self.button.isChecked()
    #
    #     print(self.button_is_checked)


app = QApplication(sys.argv)

z = MainWindow()
z.show()

app.exec()
