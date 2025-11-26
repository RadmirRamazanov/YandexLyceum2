import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit, QLineEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.counter = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle('')
        self.checkboxes = []
        self.inputs = []
        self.menu_checkboxes1 = {}
        self.prices = {"Чизбургер": 10, "Гамбургер": 20, "Кока-кола": 15, "Наггетсы": 30}
        self.box1 = QCheckBox(self)
        self.box1.move(10, 5)
        self.box1.setText("Чизбургер")
        self.box2 = QCheckBox(self)
        self.box2.move(10, 30)
        self.box2.setText("Гамбургер")
        self.box3 = QCheckBox(self)
        self.box3.move(10, 55)
        self.box3.setText("Кока-кола")
        self.box4 = QCheckBox(self)
        self.box4.move(10, 80)
        self.box4.setText("Наггетсы")
        self.box1.toggled.connect(self.frsts)
        self.box2.toggled.connect(self.frsts)
        self.box3.toggled.connect(self.frsts)
        self.box4.toggled.connect(self.frsts)
        self.input1 = QLineEdit(self)
        self.input1.move(95, 8)
        self.input1.resize(25, 15)
        self.input1.setText("0")
        self.input2 = QLineEdit(self)
        self.input2.move(95, 33)
        self.input2.resize(25, 15)
        self.input2.setText("0")
        self.input3 = QLineEdit(self)
        self.input3.move(95, 58)
        self.input3.resize(25, 15)
        self.input3.setText("0")
        self.input4 = QLineEdit(self)
        self.input4.move(95, 83)
        self.input4.resize(25, 15)
        self.input4.setText("0")
        self.checkboxes.append(self.box1)
        self.checkboxes.append(self.box2)
        self.checkboxes.append(self.box3)
        self.checkboxes.append(self.box4)
        self.inputs.append(self.input1)
        self.inputs.append(self.input2)
        self.inputs.append(self.input3)
        self.inputs.append(self.input4)
        self.orderButton = QPushButton(self)
        self.orderButton.move(15, 140)
        self.orderButton.setText("Заказать")
        self.orderButton.clicked.connect(self.buy)
        self.order = QPlainTextEdit(self)
        self.order.move(15, 170)

    def frsts(self):
        if self.box1.isChecked():
            if self.input1.text() == "0":
                self.input1.setText("1")
        else:
            self.input1.setText("0")
        if self.box2.isChecked():
            if self.input2.text() == "0":
                self.input2.setText("1")
        else:
            self.input2.setText("0")
        if self.box3.isChecked():
            if self.input3.text() == "0":
                self.input3.setText("1")
        else:
            self.input3.setText("0")
        if self.box4.isChecked():
            if self.input4.text() == "0":
                self.input4.setText("1")
        else:
            self.input4.setText("0")

    def buy(self):
        res = 0
        self.order.clear()
        if self.box1.isChecked():
            if self.box1 not in self.menu_checkboxes1:
                self.menu_checkboxes1[self.box1] = self.input1.text()
        else:
            if self.box1 in self.menu_checkboxes1:
                self.menu_checkboxes1.pop(self.box1)
        if self.box2.isChecked():
            if self.box2 not in self.menu_checkboxes1:
                self.menu_checkboxes1[self.box2] = self.input2.text()
        else:
            if self.box2 in self.menu_checkboxes1:
                self.menu_checkboxes1.pop(self.box2)
        if self.box3.isChecked():
            if self.box3 not in self.menu_checkboxes1:
                self.menu_checkboxes1[self.box3] = self.input3.text()
        else:
            if self.box3 in self.menu_checkboxes1:
                self.menu_checkboxes1.pop(self.box3)
        if self.box4.isChecked():
            if self.box4 not in self.menu_checkboxes1:
                self.menu_checkboxes1[self.box4] = self.input4.text()
        else:
            if self.box4 in self.menu_checkboxes1:
                self.menu_checkboxes1.pop(self.box4)
        self.order.appendPlainText("Ваш заказ")
        self.order.appendPlainText("")
        for i in self.menu_checkboxes1:
            self.order.appendPlainText(f"{i.text()}-----{self.menu_checkboxes1[i]}-----"
                                       f"{self.prices[i.text()] * int(self.menu_checkboxes1[i])}")
            res += self.prices[i.text()] * int(self.menu_checkboxes1[i])
        self.order.appendPlainText("")
        self.order.appendPlainText(f"Итого: {str(res)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())