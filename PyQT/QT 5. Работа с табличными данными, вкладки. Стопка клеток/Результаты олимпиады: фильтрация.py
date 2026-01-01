from sys import argv, exit
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                             QPushButton, QVBoxLayout, QGridLayout, QTableWidget, QComboBox, QWidget)
from csv import DictReader


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.schools = QComboBox(self.centralwidget)
        self.schools.setObjectName("schools")
        self.gridLayout.addWidget(self.schools, 1, 0, 1, 1)
        self.classes = QComboBox(self.centralwidget)
        self.classes.setObjectName("classes")
        self.gridLayout.addWidget(self.classes, 1, 1, 1, 1)
        self.resultButton = QPushButton()
        self.resultButton.clicked.connect(self.update_table)
        self.resultButton.setText('Узнать результаты')
        self.gridLayout.addWidget(self.resultButton, 1, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Результат олимпиады: фильтрация"))


class OlympResult(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.load_data()
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.retranslateUi(self)
        self.load_filters()
        self.schools.currentIndexChanged.connect(self.on_school_select)

    def load_data(self):
        with open("rez.csv", encoding="UTF-8") as csv_results:
            reader = DictReader(csv_results, delimiter=',', quotechar='"')
            self.result = tuple(row for row in reader)
            for row in self.result:
                row['Фамилия'] = row["user_name"].split(" ")[3]
                row['Результат'] = row['Score']

    def fill_table(self, header, data):
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for el_num, el in enumerate(row_data):
                item = QTableWidgetItem(el)
                self.tableWidget.setItem(row_num, el_num, item)
        self.tableWidget.resizeColumnsToContents()
        for i in range(self.tableWidget.columnCount() - 2):
            self.tableWidget.setColumnWidth(i, 0)

    def load_filters(self, GradesOnly=False):
        if not GradesOnly:
            self.schools.clear()
            schools = []
            for school in map(lambda row: row["login"].split("-")[2], self.result):
                if school not in schools:
                    schools.append(school)
            schools.sort()
            schools.insert(0, 'Все')
            self.schools.addItems(schools)

        self.classes.clear()
        grades = []
        for row in self.result:
            grade = row["login"].split("-")[3]
            sc = row["login"].split("-")[2]
            if grade not in grades:
                if self.schools.currentText() == 'Все':
                    grades.append(grade)
                else:
                    if sc == self.schools.currentText():
                        grades.append(grade)
        grades.sort()
        grades.insert(0, 'Все')
        self.classes.addItems(grades)

    def update_table(self):
        no_schools_filter = self.schools.currentText() == 'Все'
        no_grades_filter = self.classes.currentText() == 'Все'
        matched = []
        grades = []
        for row in self.result:
            login_data = row["login"].split("-")
            lg_school = login_data[2]
            lg_class = login_data[3]
            if (lg_school == self.schools.currentText() or no_schools_filter) and (
                    lg_class == self.classes.currentText() or no_grades_filter):
                row2 = {k: v for k, v in row.items() if k in ['Фамилия', 'Результат']}
                matched.append(row2)
            if not no_schools_filter and no_grades_filter and lg_school == self.schools.currentText():
                if lg_class not in grades:
                    grades.append(lg_class)
        if matched:
            row2 = {k: v for k, v in matched[0].items() if k in ['Фамилия', 'Результат']}
            header = list(row2.keys())
            data = [list(row.values()) for row in matched]
            self.fill_table(header, data)
        if not no_schools_filter and no_grades_filter:
            self.classes.clear()
            grades.sort()
            grades.insert(0, 'Все')
            self.classes.addItems(grades)

    def on_school_select(self):
        self.load_filters(GradesOnly=True)


def main():
    app = QApplication(argv)
    window = OlympResult()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()