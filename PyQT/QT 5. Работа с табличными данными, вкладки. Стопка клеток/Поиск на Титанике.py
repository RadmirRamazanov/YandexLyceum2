import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTableWidget, QTableWidgetItem,
    QLineEdit, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont


class TitanicSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = []
        self.load_data()
        self.init_ui()
        self.display_data(self.data)

    def load_data(self):
        try:
            with open('titanic.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.headers = next(reader)
                for row in reader:
                    if len(row) >= 6:
                        self.data.append(row)
        except FileNotFoundError:
            self.headers = ['PassengerID', 'Name', 'PClass', 'Age', 'Sex', 'Survived', 'SexCode']
            self.data = [
                ['1', 'Allen, Miss Elisabeth Walton', '1st', '29', 'female', '1', '1'],
                ['2', 'Allison, Miss Helen Loraine', '1st', '2', 'female', '0', '1'],
                ['3', 'Allison, Mr Hudson Joshua Creighton', '1st', '30', 'male', '0', '0'],
                ['4', 'Allison, Mrs Hudson JC (Bessie Waldo Daniels)', '1st', '25', 'female', '0', '1'],
                ['5', 'Allison, Master Hudson Trevor', '1st', '0.92', 'male', '1', '0'],
                ['6', 'Anderson, Mr Harry', '1st', '47', 'male', '1', '0'],
                ['7', 'Andrews, Miss Kornelia Theodosia', '1st', '63', 'female', '1', '1'],
                ['8', 'Andrews, Mr Thomas, jr', '1st', '39', 'male', '0', '0'],
                ['9', 'Appleton, Mrs Edward Dale (Charlotte Lamson)', '1st', '58', 'female', '1', '1'],
                ['10', 'Artagaveytia, Mr Ramon', '1st', '71', 'male', '0', '0']
            ]

    def init_ui(self):
        self.setGeometry(100, 100, 1000, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        search_layout = QHBoxLayout()
        search_label = QLabel('Поиск по имени:')
        search_label.setFont(QFont('Arial', 10))
        self.searchEdit = QLineEdit()
        self.searchEdit.setPlaceholderText('Введите имя для поиска...')
        self.searchEdit.textChanged.connect(self.on_search_text_changed)
        self.searchEdit.setFont(QFont('Arial', 10))
        self.searchEdit.setMinimumWidth(200)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.searchEdit)
        search_layout.addStretch()
        self.resultTable = QTableWidget()
        self.resultTable.setColumnCount(len(self.headers))
        self.resultTable.setHorizontalHeaderLabels(self.headers)
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        self.resultTable.verticalHeader().setVisible(False)
        self.resultTable.setSortingEnabled(True)
        self.resultTable.setFont(QFont('Arial', 9))
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.resultTable)
        self.info_label = QLabel('Всего записей: 0')
        self.info_label.setFont(QFont('Arial', 10))
        main_layout.addWidget(self.info_label)

    def on_search_text_changed(self, text):
        search_text = text.strip().lower()
        if len(search_text) < 3:
            self.display_data(self.data)
        else:
            filtered_data = []
            for row in self.data:
                if len(row) > 1 and search_text in row[1].lower():
                    filtered_data.append(row)
            self.display_data(filtered_data)

    def display_data(self, data):
        self.resultTable.setRowCount(0)
        self.resultTable.setRowCount(len(data))
        self.resultTable.setUpdatesEnabled(False)
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                if col_idx < len(self.headers):
                    item = QTableWidgetItem(str(cell_data))
                    if len(row_data) > 5:
                        survived = row_data[5]
                        if survived == '1':
                            item.setBackground(QColor('#00FF00'))
                        else:
                            item.setBackground(QColor('#FF0000'))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.resultTable.setItem(row_idx, col_idx, item)
        self.resultTable.setUpdatesEnabled(True)
        survived_count = sum(1 for row in data if len(row) > 5 and row[5] == '1')
        perished_count = sum(1 for row in data if len(row) > 5 and row[5] == '0')
        self.info_label.setText(f'Всего записей: {len(data)} | Выживших: {survived_count} | Погибших: {perished_count}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TitanicSearch()
    window.show()
    sys.exit(app.exec())