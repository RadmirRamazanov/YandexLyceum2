import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.counter = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle('')
        self.menu_checkboxes = []
        self.menu_checkboxes1 = []
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
        self.menu_checkboxes.append(self.box1)
        self.menu_checkboxes.append(self.box2)
        self.menu_checkboxes.append(self.box3)
        self.menu_checkboxes.append(self.box4)
        self.order_btn = QPushButton(self)
        self.order_btn.move(15, 140)
        self.order_btn.setText("Заказать")
        self.order_btn.clicked.connect(self.buy)
        self.result = QPlainTextEdit(self)
        self.result.move(15, 170)

    def buy(self):
        self.result.clear()
        if self.box1.isChecked():
            if self.box1 not in self.menu_checkboxes1:
                self.menu_checkboxes1.append(self.box1)
        else:
            if self.box1 in self.menu_checkboxes1:
                self.menu_checkboxes1.remove(self.box1)
        if self.box2.isChecked():
            if self.box2 not in self.menu_checkboxes1:
                self.menu_checkboxes1.append(self.box2)
        else:
            if self.box2 in self.menu_checkboxes1:
                self.menu_checkboxes1.remove(self.box2)
        if self.box3.isChecked():
            if self.box3 not in self.menu_checkboxes1:
                self.menu_checkboxes1.append(self.box3)
        else:
            if self.box3 in self.menu_checkboxes1:
                self.menu_checkboxes1.remove(self.box3)
        if self.box4.isChecked():
            if self.box4 not in self.menu_checkboxes1:
                self.menu_checkboxes1.append(self.box4)
        else:
            if self.box4 in self.menu_checkboxes1:
                self.menu_checkboxes1.remove(self.box4)
        self.result.appendPlainText("Ваш заказ:")
        self.result.appendPlainText(" ")
        for i in self.menu_checkboxes1:
            self.result.appendPlainText(i.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())
