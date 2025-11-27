import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from addEditCoffeeForm import Ui_MainWindow1
from mainui import Ui_MainWindow


class Redactor(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("../data/coffee.sqlite")
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roats_level", "type",
                                                    "taste_description", "price", "package_volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.upd)

    def add(self):
        name = self.lineEdit.text()
        roats_level = self.lineEdit_3.text()
        typee = self.lineEdit_5.text()
        taste_description = self.lineEdit_2.text()
        price = self.lineEdit_4.text()
        package_volume = self.lineEdit_6.text()
        self.con.cursor().execute(
            """INSERT INTO coffee(name, roast_level, type, taste_description, price, package_volume) 
            VALUES (?, ?, ?, ?, ?, ?)""", (name, roats_level, typee, taste_description, price, package_volume)
        )
        self.con.commit()
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roats_level", "type",
                                                    "taste_description", "price", "package_volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def upd(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        name = self.tableWidget.item(rows[0], 1).text()
        roats_level = self.tableWidget.item(rows[0], 2).text()
        typee = self.tableWidget.item(rows[0], 3).text()
        taste_description = self.tableWidget.item(rows[0], 4).text()
        price = self.tableWidget.item(rows[0], 5).text()
        package_volume = self.tableWidget.item(rows[0], 6).text()
        self.con.cursor().execute(
            """UPDATE coffee SET name = ?, roast_level = ?, type = ?, taste_description = ?, price = ?, 
            package_volume = ? WHERE id = ?""",
            (name, roats_level, typee, taste_description, price, package_volume, rows[0] + 1)
        )
        self.con.commit()
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roats_level", "type",
                                                    "taste_description", "price", "package_volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("../data/coffee.sqlite")
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roats_level", "type",
                                                    "taste_description", "price", "package_volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.pushButton.clicked.connect(self.open_second_window)
        self.pushButton_2.clicked.connect(self.aaaaaaaaaaa)

    def aaaaaaaaaaa(self):
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roats_level", "type",
                                                    "taste_description", "price", "package_volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def open_second_window(self):
        self.second_window = Redactor()
        self.second_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())