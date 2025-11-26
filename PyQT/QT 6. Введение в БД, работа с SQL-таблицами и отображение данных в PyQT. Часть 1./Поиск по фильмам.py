import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QComboBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect("films_db.sqlite")
        self.cur = self.con.cursor()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("")
        self.parameterSelection = QComboBox(self)
        self.parameterSelection.addItems(["Год выпуска", "Название", "Продолжительность"])
        self.parameterSelection.move(5, 10)
        self.queryLine = QLineEdit(self)
        self.queryLine.move(155, 10)
        self.queryButton = QPushButton(self)
        self.queryButton.move(295, 10)
        self.queryButton.setText("Поиск")
        self.queryButton.clicked.connect(self.search)
        self.idEdit = QLineEdit(self)
        self.idEdit.move(100, 40)
        self.titleEdit = QLineEdit(self)
        self.titleEdit.move(100, 80)
        self.yearEdit = QLineEdit(self)
        self.yearEdit.move(100, 120)
        self.genreEdit = QLineEdit(self)
        self.genreEdit.move(100, 160)
        self.durationEdit = QLineEdit(self)
        self.durationEdit.move(100, 200)
        self.errorLabel = QLabel(self)
        self.errorLabel.move(5, 240)

    def search(self):
        if self.parameterSelection.currentText() == "Год выпуска":
            if self.queryLine.text() == "":
                self.errorLabel.setText("Неправильный запрос")
                self.idEdit.setText("")
                self.titleEdit.setText("")
                self.yearEdit.setText("")
                self.genreEdit.setText("")
                self.durationEdit.setText("")
            else:
                try:
                    result = self.cur.execute(f"""SELECT * FROM films
                                WHERE year = {int(self.queryLine.text())}""").fetchone()
                    try:
                        if len(result) == 5:
                            self.idEdit.setText(str(result[0]))
                            self.titleEdit.setText(result[1])
                            self.yearEdit.setText(str(result[2]))
                            self.genreEdit.setText(str(result[3]))
                            self.durationEdit.setText(str(result[4]))
                            self.errorLabel.setText("")
                            self.errorLabel.setText("")
                    except TypeError:
                        self.errorLabel.setText("Ничего не найдено")
                        self.idEdit.setText("")
                        self.titleEdit.setText("")
                        self.yearEdit.setText("")
                        self.genreEdit.setText("")
                        self.durationEdit.setText("")
                except ValueError:
                    self.errorLabel.setText("Неправильный запрос")
                    self.idEdit.setText("")
                    self.titleEdit.setText("")
                    self.yearEdit.setText("")
                    self.genreEdit.setText("")
                    self.durationEdit.setText("")
        elif self.parameterSelection.currentText() == "Название":
            if self.queryLine.text() == "":
                self.errorLabel.setText("Неправильный запрос")
                self.idEdit.setText("")
                self.titleEdit.setText("")
                self.yearEdit.setText("")
                self.genreEdit.setText("")
                self.durationEdit.setText("")
            else:
                try:
                    result = self.cur.execute(f"""SELECT * FROM films
                                WHERE title = '{self.queryLine.text()}'""").fetchone()
                    try:
                        if len(result) == 5:
                            self.idEdit.setText(str(result[0]))
                            self.titleEdit.setText(result[1])
                            self.yearEdit.setText(str(result[2]))
                            self.genreEdit.setText(str(result[3]))
                            self.durationEdit.setText(str(result[4]))
                            self.errorLabel.setText("")
                            self.errorLabel.setText("")
                    except TypeError:
                        self.errorLabel.setText("Ничего не найдено")
                        self.idEdit.setText("")
                        self.titleEdit.setText("")
                        self.yearEdit.setText("")
                        self.genreEdit.setText("")
                        self.durationEdit.setText("")
                except ValueError:
                    self.errorLabel.setText("Неправильный запрос")
                    self.idEdit.setText("")
                    self.titleEdit.setText("")
                    self.yearEdit.setText("")
                    self.genreEdit.setText("")
                    self.durationEdit.setText("")
        else:
            if self.queryLine.text() == "":
                self.errorLabel.setText("Неправильный запрос")
                self.idEdit.setText("")
                self.titleEdit.setText("")
                self.yearEdit.setText("")
                self.genreEdit.setText("")
                self.durationEdit.setText("")
            else:
                try:
                    result = self.cur.execute(f"""SELECT * FROM films
                                WHERE duration = {int(self.queryLine.text())}""").fetchone()
                    try:
                        if len(result) == 5:
                            self.idEdit.setText(str(result[0]))
                            self.titleEdit.setText(result[1])
                            self.yearEdit.setText(str(result[2]))
                            self.genreEdit.setText(str(result[3]))
                            self.durationEdit.setText(str(result[4]))
                            self.errorLabel.setText("")
                            self.errorLabel.setText("")
                    except TypeError:
                        self.errorLabel.setText("Ничего не найдено")
                        self.idEdit.setText("")
                        self.titleEdit.setText("")
                        self.yearEdit.setText("")
                        self.genreEdit.setText("")
                        self.durationEdit.setText("")
                except ValueError:
                    self.errorLabel.setText("Неправильный запрос")
                    self.idEdit.setText("")
                    self.titleEdit.setText("")
                    self.yearEdit.setText("")
                    self.genreEdit.setText("")
                    self.durationEdit.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())