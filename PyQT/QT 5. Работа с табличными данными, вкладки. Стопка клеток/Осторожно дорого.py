import sys
import csv
import random
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton
)
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtGui import QColor


class Expensive(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle("")
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(10, 10)
        self.tableWidget.setMinimumSize(680, 300)
        with open("price.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            self.rows = list(reader)
            for i in self.rows:
                if self.rows[0] == i:
                    i.append("Количество")
                else:
                    i[2] = "0"
        b = self.rows[0]
        self.rows.pop(0)
        self.rows.sort(key=lambda i: int(i[1]), reverse=True)
        self.rows.insert(0, b)
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
        self.updateButton = QPushButton(self)
        self.updateButton.move(5, 350)
        self.updateButton.setText("Обновить")
        self.updateButton.clicked.connect(self.color_table)
        self.color_table()

    def sum(self):
        total_sum = 0
        for i in range(self.tableWidget.rowCount()):
            total_sum += (int(self.tableWidget.item(i, 1).text()) *
                          int(self.tableWidget.item(i, 2).text()))
        self.total.setText(str(total_sum))

    def color_table(self):
        if self.tableWidget.rowCount() < 5:
            return
        for row in range(5):
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Expensive()
    ex.show()
    sys.exit(app.exec())