import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton, QComboBox, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.connection = sqlite3.connect("films_db.sqlite")
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle("")
        self.parameterSelection = QComboBox(self)
        self.parameterSelection.addItems(["комедия", "драма", "мелодрама", "детектив", "документальный",
                                          "ужасы", "музыка", "фантастика", "анимация", "биография"])
        self.dct_genre = {"комедия": 1,
                          "драма": 2,
                          "мелодрама": 3,
                          "детектив": 4,
                          "документальный": 5,
                          "ужасы": 6,
                          "музыка": 7,
                          "фантастика": 8,
                          "анимация": 9,
                          "биография": 10}
        self.parameterSelection.move(5, 10)
        self.queryButton = QPushButton(self)
        self.queryButton.move(5, 50)
        self.queryButton.setText("Пуск")
        self.queryButton.clicked.connect(self.search)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(130, 10)
        self.tableWidget.setMinimumSize(400, 400)
        res = self.connection.cursor().execute("""SELECT title, genre, year FROM films""").fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Жанр", "Год"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def search(self):
        self.tableWidget.setRowCount(0)
        res = self.connection.cursor().execute(f"""SELECT title, genre, year FROM films
        WHERE genre = '{self.dct_genre[self.parameterSelection.currentText()]}'""").fetchall()
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