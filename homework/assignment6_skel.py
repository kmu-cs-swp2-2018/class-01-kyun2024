import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    '''
    Hello ScoreDB
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.sortScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # Add LineBox - name, age, score, amount
        self.name_box, self.age_box, self.score_box, self.amount_box = [QLineEdit() for _ in range(4)]


        # Add ComboBox - key
        self.key_combo = QComboBox()
        self.key_combo.addItem("Name")
        self.key_combo.addItem("Age")
        self.key_combo.addItem("Score")

        # Set Attribute - ComboBox


        # Add Buttons - add, delete, find, increase, show
        add_button, del_button, find_button, inc_button, show_button = [QPushButton() for _ in range(5)]
        # Set Attributes - name, clicked(event listener)
        add_button.setText("Add")
        del_button.setText("Del")
        find_button.setText("Find")
        inc_button.setText("Inc")
        show_button.setText("Show")

        add_button.clicked.connect(self.buttonClicked)
        del_button.clicked.connect(self.buttonClicked)
        find_button.clicked.connect(self.buttonClicked)
        inc_button.clicked.connect(self.buttonClicked)
        show_button.clicked.connect(self.buttonClicked)

        # Add hbox - name, age, score
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("Name:"))
        hbox1.addWidget(self.name_box)
        hbox1.addWidget(QLabel("Age:"))
        hbox1.addWidget(self.age_box)
        hbox1.addWidget(QLabel("Score:"))
        hbox1.addWidget(self.score_box)

        # Add hbox - amount, key
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QLabel("Amount:"))
        hbox2.addWidget(self.amount_box)
        hbox2.addWidget(QLabel("Key:"))
        hbox2.addWidget(self.key_combo)

        # Add hbox - Buttons
        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addWidget(add_button)
        hbox3.addWidget(del_button)
        hbox3.addWidget(find_button)
        hbox3.addWidget(inc_button)
        hbox3.addWidget(show_button)

        # Add TextBox
        self.result = QTextEdit()

        # Add vbox - hbox1, hbox2, hbox3, label, result
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(QLabel("Result:"))
        vbox.addWidget(self.result)

        self.setLayout(vbox)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    # show ScoreDB on UI
    def showScoreDB(self):
        stream = ""
        for elem in self.scoredb:
            for key, value in elem.items():
                stream += "{key}:{value}\t\t".format(key=key,value=value)
            stream += '\n'
        self.result.setText(stream)
        pass

    def sortScoreDB(self):
        '''sort ScoreDB by flag'''
        key = self.key_combo.currentText()
        self.scoredb.sort(key=lambda x: x[key])

    def buttonClicked(self):
        '''

        '''
        sender = self.sender()
        if sender.text() == "Add":
            self.AddElement()
        elif sender.text() == "Del":
            self.DeleteElement()
        elif sender.text() == "Find":
            # 구현 사항 아님
            pass
        elif sender.text() == "Inc":
            self.IncreaseScore()
        elif sender.text() == "Show":
            self.sortScoreDB()
        self.showScoreDB()
        pass

    def getCurrentElement(self):
        elem = {}
        elem["Name"] = self.name_box.text()
        elem["Age"] = int(self.age_box.text())
        elem["Score"] = int(self.score_box.text())
        return elem

    def AddElement(self):
        elem = self.getCurrentElement()
        self.scoredb.append(elem)

    def DeleteElement(self):
        name = self.name_box.text()
        same_names = []
        for elem in self.scoredb:
            if elem.get("Name")==name:
                same_names.append(elem)
        if(len(same_names)>0):
            for elem in same_names:
                self.scoredb.remove(elem)
        else:
            QMessageBox.warning(self,"Warning","Element does not exit")

    def IncreaseScore(self):
        try:
            amount = int(self.amount_box.text())
            name = self.name_box.text()
            for elem in self.scoredb:
                if elem["Name"] == name:
                    elem["Score"] += amount
        except:
            QMessageBox.warning(self,"Warning","Wrong Value")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    print(ex.scoredb)
    sys.exit(app.exec_())

