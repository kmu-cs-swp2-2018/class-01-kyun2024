from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.Qt import QStyle


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("background-color: rgb(255,243,212)")

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(30)
        self.display.setStyleSheet("background-color: white")

        # Digit Buttons
        self.digitButton = [Button(str(x)) for x in range(0, 10)]

        # Add Digit Event
        for i in self.digitButton:
            i.pressed.connect(self.buttonPressed);

        # . and = Buttons
        self.decButton = Button('.')
        self.eqButton = Button('=')

        self.decButton.pressed.connect(self.buttonPressed)
        self.eqButton.pressed.connect(self.buttonPressed)

        # Operator Buttons
        self.mulButton = Button('*')
        self.divButton = Button('/')
        self.addButton = Button('+')
        self.subButton = Button('-')

        self.mulButton.pressed.connect(self.buttonPressed)
        self.divButton.pressed.connect(self.buttonPressed)
        self.addButton.pressed.connect(self.buttonPressed)
        self.subButton.pressed.connect(self.buttonPressed)

        # Parentheses Buttons
        self.lparButton = Button('(')
        self.rparButton = Button(')')

        self.lparButton.pressed.connect(self.buttonPressed)
        self.rparButton.pressed.connect(self.buttonPressed)

        # Clear Button
        self.clearButton = Button('C')
        self.clearButton.pressed.connect(self.buttonPressed)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0],3,0)
        for i in range(1,10):
            numLayout.addWidget(self.digitButton[i],(9-i)//3,(i-1)%3);

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonPressed(self):
        name = self.sender().text();
        if name == "=":
            self.display.setText(str(eval(self.display.text())))
        elif name == "C":
            self.display.setText("0")
        else: self.display.setText(self.display.text()+name if self.display.text() != "0" else name)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

