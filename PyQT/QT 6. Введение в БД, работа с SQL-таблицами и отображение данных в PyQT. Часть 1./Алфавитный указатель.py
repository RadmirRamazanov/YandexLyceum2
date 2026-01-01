import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidget, QPushButton, QHBoxLayout, QTableWidgetItem, \
    QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.connection = sqlite3.connect("films_db.sqlite")
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle("")
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.buttons = []
        self.alph = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        for i in range(33):
            a = QPushButton()
            a.setText(self.alph[i])
            a.setFixedSize(17, 25)
            buttons_layout.addWidget(a)
            self.buttons.append(a)
            a.clicked.connect(self.search)
        layout.addLayout(buttons_layout)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(130, 50)
        self.tableWidget.setMinimumSize(570, 400)
        res = self.connection.cursor().execute("""SELECT * FROM films""").fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Год", "Жанр", "Продолжительность"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def search(self):
        btn = self.sender()
        self.tableWidget.setRowCount(0)
        res = self.connection.cursor().execute(f"""SELECT * FROM films
        WHERE title LIKE '{btn.text()}%'""").fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.statusBar().showMessage(f"Нашлось {str(len(res))} записей") if len(res) > 0 else \
            self.statusBar().showMessage("К сожалению, ничего не нашлось")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())