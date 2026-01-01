import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableView,
                             QVBoxLayout, QWidget, QHeaderView)
from PyQt6.QtCore import Qt, QVariant, QAbstractTableModel, QModelIndex


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)
        self.headers, self.rows = self.load_csv_data("countries.csv")
        self.create_tabs()

    def load_csv_data(self, filename):
        """Загрузка данных из CSV файла"""
        headers = []
        rows = []
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                headers = next(reader)
                rows = list(reader)
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            headers = ["Country", "Region", "Capital", "Official languages",
                       "Area, km 2", "Population, ppl.",
                       "Population density, ppl./km2", "International phone code"]
            rows = [
                ["Russia", "Europe/Asia", "Moscow", "Russian", "17098242", "146780720", "8.4", "+7"],
                ["Germany", "Europe", "Berlin", "German", "357022", "83149300", "232", "+49"],
                ["France", "Europe", "Paris", "French", "551695", "67390000", "122", "+33"]
            ]

        return headers, rows

    def create_tabs(self):
        """Создание вкладок для каждой характеристики"""
        country_index = self.headers.index("Country") if "Country" in self.headers else 0
        for col_index, header in enumerate(self.headers):
            if header == "Country":
                continue
            tab_headers = ["Country", header]
            tab_rows = []

            for row in self.rows:
                country_name = row[country_index] if country_index < len(row) else ""
                col_value = row[col_index] if col_index < len(row) else ""
                tab_rows.append([country_name, col_value])
            model = CsvTableModel(tab_headers, tab_rows)
            table = QTableView()
            table.setModel(model)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tab_widget.addTab(table, header)


# Класс модели
class CsvTableModel(QAbstractTableModel):
    def __init__(self, headers=None, rows=None, parent=None):
        super().__init__(parent)
        self._headers = headers or []
        self._rows = rows or []

    def rowCount(self, parent=None):
        return len(self._rows)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return str(self._rows[index.row()][index.column()])
        return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Horizontal and 0 <= section < len(self._headers):
            return self._headers[section]
        return str(section + 1)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled
        return (Qt.ItemFlag.ItemIsSelectable |
                Qt.ItemFlag.ItemIsEnabled |
                Qt.ItemFlag.ItemIsEditable)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self._rows[index.row()][index.column()] = str(value)
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def insertRows(self, row, count, parent=None):
        self.beginInsertRows(parent or QModelIndex(), row, row + count - 1)
        for _ in range(count):
            self._rows.insert(row, [""] * len(self._headers))
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=None):
        self.beginRemoveRows(parent or QModelIndex(), row, row + count - 1)
        for _ in range(count):
            self._rows.pop(row)
        self.endRemoveRows()
        return True


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()