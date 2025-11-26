import sys
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QLineEdit
)
from PyQt6.QtWidgets import QHeaderView


class InteractiveReceipt(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle("")
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(10, 10)
        self.tableWidget.setMinimumSize(700, 300)
        with open("price.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            self.rows = list(reader)
            for i in self.rows:
                if self.rows[0] == i:
                    i.append("Количество")
                else:
                    i[2] = "0"
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.rows) - 1)
        self.tableWidget.setColumnCount(len(self.rows[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.rows[0])
        for r, row in enumerate(self.rows[1:]):
            for c, val in enumerate(row):
                item = QTableWidgetItem(val)
                if val.isdigit():
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.tableWidget.setItem(r, c, item)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        self.total = QLineEdit(self)
        self.total.move(550, 350)
        self.tableWidget.cellChanged.connect(self.sum)

    def sum(self):
        self.sum = 0
        for i in range(self.tableWidget.rowCount()):
            self.sum += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.total.setText(str(self.sum))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = InteractiveReceipt()
    ex.show()
    sys.exit(app.exec())