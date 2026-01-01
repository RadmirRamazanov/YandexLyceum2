import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton, QLineEdit, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.connection = sqlite3.connect("films_db.sqlite")
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle("")
        self.year = QLineEdit(self)
        self.year.move(0, 25)
        self.title = QLineEdit(self)
        self.title.move(0, 65)
        self.duration = QLineEdit(self)
        self.duration.move(0, 105)
        self.queryButton = QPushButton(self)
        self.queryButton.move(5, 150)
        self.queryButton.setText("Пуск")
        self.queryButton.clicked.connect(self.search)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(150, 10)
        self.tableWidget.setMinimumSize(600, 400)
        res = self.connection.cursor().execute("""SELECT * FROM films""").fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Год", "Жанр", "Продолжительность"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def search(self):
        self.tableWidget.setRowCount(0)
        if self.year.text() != "" and self.title.text() == "" and self.duration.text() == "":
            if self.year.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()}""").fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE year = ?""", (self.year.text(),)).fetchall()
        elif self.year.text() == "" and self.title.text() != "" and self.duration.text() == "":
            if "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE title {self.title.text()}""").fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE title = ?""", (self.title.text(),)).fetchall()
        elif self.year.text() == "" and self.title.text() == "" and self.duration.text() != "":
            if self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE duration {self.duration.text()}""").fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE duration = ?""", (self.duration.text(), )).fetchall()
        elif self.year.text() != "" and self.title.text() != "" and self.duration.text() == "":
            if self.year.text()[0] in "><=!" and "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND title {self.title.text()}""").fetchall()
            elif self.year.text()[0] in "><=1":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND title = ?""", (self.title.text(), )).fetchall()
            elif "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year = ? AND title {self.title.text()}""", (self.year.text(),)).fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE year = ? AND title = ?""", (self.year.text(), self.title.text())).fetchall()
        elif self.year.text() == "" and self.title.text() != "" and self.duration.text() != "":
            if self.duration.text()[0] in "><=!" and "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE duration {self.duration.text()} AND title {self.title.text()}""").fetchall()
            elif self.duration.text()[0] in "><=1":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE duration {self.duration.text()} AND title = ?""", (self.title.text(),)).fetchall()
            elif "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE duration = ? AND title {self.title.text()}""", (self.duration.text(),)).fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE duration = ? AND title = ?""", (self.duration.text(),
                                                                      self.title.text())).fetchall()
        elif self.year.text() != "" and self.title.text() == "" and self.duration.text() != "":
            if self.year.text()[0] in "><=!" and self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND duration {self.duration.text()}""").fetchall()
            elif self.year.text()[0] in "><=1":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND duration = ?""", (self.duration.text(),)).fetchall()
            elif self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year = ? AND duration {self.duration.text()}""", (self.year.text(),)).fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE year = ? AND duration = ?""", (self.year.text(), self.duration.text())).fetchall()
        else:
            if self.year.text()[0] in "><=!" and "LIKE" in self.title.text() and self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND title {self.title.text()} 
                                AND duration {self.duration.text()}""").fetchall()
            elif self.year.text()[0] in "><=!" and "LIKE" in self.title.text():
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND title {self.title.text()} AND 
                                duration = ?""", (self.duration.text(),)).fetchall()
            elif self.year.text()[0] in "><=!" and self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year {self.year.text()} AND title = ? AND 
                                duration {self.duration.text()}""", (self.title.text(),)).fetchall()
            elif "LIKE" in self.title.text() and self.duration.text()[0] in "><=!":
                res = self.connection.cursor().execute(f"""SELECT * FROM films
                                WHERE year = ? AND title '{self.title.text()}' AND 
                                duration {self.duration.text()}""", (self.year.text(),)).fetchall()
            else:
                res = self.connection.cursor().execute("""SELECT * FROM films
                                WHERE year = ? AND title = ? AND duration = ?""", (self.year.text(), self.title.text(),
                                                                                   self.duration.text())).fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())