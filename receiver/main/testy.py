import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Хелло Декстер Морган")

        next_statements = [
            'pay 100 pounds',
            'pay 10 pounds(this button must be doesnt work, trust me)',
            'pay 0 pounds(this button seems to be like second too)',
            'pay 1000 pounds'
        ]

        statements = [
            'Yes, I hate niggers',
            'No, I hate niggers',
            'Maybe, I hate niggers',
            'Basically, I hate niggers',
            'Must be, I hate niggers',
            '"leave the blank"'
        ]

        self.widgets = [
            QLabel(),
            QCheckBox(),
            QComboBox(),
            QListWidget(),
            QLabel()
        ]

        self.widgets[0].setPixmap(QPixmap('stef.jpg'))
        self.widgets[0].setScaledContents(True)
        self.widgets[1].stateChanged.connect(self.statement)
        self.widgets[1].setCheckState(Qt.CheckState.PartiallyChecked)
        self.widgets[2].addItems(statements)
        self.widgets[2].currentTextChanged.connect(self.setWindowTitle)
        self.widgets[3].addItems(next_statements)
        self.widgets[3].currentTextChanged.connect(self.guess)
        self.widgets[4].setText('I will guess what you have picked')
        self.widgets[4].setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout = QVBoxLayout()

        for widget in self.widgets:
            layout.addWidget(widget)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.setFixedSize(QSize(1000, 800))

    def statement(self, s):
        if s == 0:
            self.widgets[0].setPixmap(QPixmap('dicaprio.jpg'))
        elif s == 1:
            self.widgets[0].setPixmap(QPixmap('stef.jpg'))
        else:
            self.widgets[0].setPixmap(QPixmap('dexter.jpg'))

    def guess(self, s):
        self.widgets[4].setText(f'I guess you picked to {s}')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
