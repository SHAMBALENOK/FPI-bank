import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QDial
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
            QLabel(),
            QSpinBox(),
            QSlider(),
            QLabel(),
            QDial(),
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
        self.widgets[5].setMinimum(-100)
        self.widgets[5].setMaximum(16)
        self.widgets[5].setPrefix("Р")
        self.widgets[5].setSuffix("к")
        self.widgets[5].setSingleStep(2)
        self.widgets[6].setRange(-30, 30)
        self.widgets[6].setSingleStep(2)
        self.widgets[6].setOrientation(Qt.Orientation.Horizontal)
        self.widgets[6].sliderPressed.connect(self.slidePress)
        self.widgets[6].valueChanged.connect(self.value_review)
        self.widgets[6].sliderReleased.connect(self.slideReleased)
        self.widgets[7].setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.widgets[7].setVisible(False)
        self.widgets[8].setRange(-100, 100)
        self.widgets[8].setSingleStep(1)
        self.widgets[8].valueChanged.connect(self.DialChanged)
        self.widgets[9].setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout = QVBoxLayout()

        for widget in self.widgets:
            layout.addWidget(widget)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.setFixedSize(QSize(1000, 800))

    def DialChanged(self, i):
        self.widgets[9].setText(str(i))

    def slidePress(self):
        self.widgets[7].setVisible(True)

    def value_review(self, i):
        self.widgets[7].setText(f' Громкость: {str(i)}')

    def slideReleased(self):
        self.widgets[7].setVisible(False)

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
