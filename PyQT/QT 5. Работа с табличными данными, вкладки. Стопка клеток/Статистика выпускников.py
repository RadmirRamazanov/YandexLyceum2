import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableWidget,
                             QVBoxLayout, QWidget, QHeaderView, QPushButton,
                             QFileDialog, QMessageBox, QTableWidgetItem)
from PyQt6.QtCore import Qt, pyqtSignal


class SortTableWidget(QTableWidget):
    headerClicked = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        header = self.horizontalHeader()
        header.setSectionsClickable(True)
        header.sectionClicked.connect(self.onHeaderClicked)

        self.sort_order = {}

    def onHeaderClicked(self, logicalIndex):
        self.headerClicked.emit(logicalIndex)

        if logicalIndex not in self.sort_order:
            self.sort_order[logicalIndex] = Qt.SortOrder.AscendingOrder
        else:
            self.sort_order[logicalIndex] = (
                Qt.SortOrder.DescendingOrder
                if self.sort_order[logicalIndex] == Qt.SortOrder.AscendingOrder
                else Qt.SortOrder.AscendingOrder
            )

        self.sortItems(logicalIndex, self.sort_order[logicalIndex])

        self.updateHeaderIndicator(logicalIndex)

    def updateHeaderIndicator(self, sortedColumn):
        header = self.horizontalHeader()

        for i in range(header.count()):
            item = self.horizontalHeaderItem(i)
            if item:
                text = item.text()
                if text.endswith(" ▲") or text.endswith(" ▼"):
                    text = text[:-2]
                item.setText(text)

        if sortedColumn in self.sort_order:
            item = self.horizontalHeaderItem(sortedColumn)
            if item:
                arrow = " ▲" if self.sort_order[sortedColumn] == Qt.SortOrder.AscendingOrder else " ▼"
                current_text = item.text()
                if current_text.endswith(" ▲") or current_text.endswith(" ▼"):
                    current_text = current_text[:-2]
                item.setText(current_text + arrow)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика выпускников")
        self.setGeometry(100, 100, 1000, 600)

        self.headers = []
        self.rows = []

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Кнопка открытия файла
        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        # Вкладки
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        # Создаём пустые вкладки
        self.create_empty_tabs()

    def create_empty_tabs(self):
        """Создание пустых вкладок при запуске"""
        # Вкладка "Данные"
        data_widget = QWidget()
        data_layout = QVBoxLayout(data_widget)
        self.data_table = SortTableWidget()
        self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        data_layout.addWidget(self.data_table)
        self.tab_widget.addTab(data_widget, "Данные")

        # Вкладка "Численность выпускников"
        count_widget = QWidget()
        count_layout = QVBoxLayout(count_widget)
        self.count_table = SortTableWidget()
        self.count_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        count_layout.addWidget(self.count_table)
        self.tab_widget.addTab(count_widget, "Численность выпускников")

        # Вкладка "Соответствует"
        match_widget = QWidget()
        match_layout = QVBoxLayout(match_widget)
        self.match_table = SortTableWidget()
        self.match_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        match_layout.addWidget(self.match_table)
        self.tab_widget.addTab(match_widget, "Соответствует")

        # Вкладка "Не соответствует"
        no_match_widget = QWidget()
        no_match_layout = QVBoxLayout(no_match_widget)
        self.no_match_table = SortTableWidget()
        self.no_match_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        no_match_layout.addWidget(self.no_match_table)
        self.tab_widget.addTab(no_match_widget, "Не соответствует")

        self.data_table.headerClicked.connect(lambda idx: self.onTableHeaderClicked(self.data_table, idx))
        self.count_table.headerClicked.connect(lambda idx: self.onTableHeaderClicked(self.count_table, idx))
        self.match_table.headerClicked.connect(lambda idx: self.onTableHeaderClicked(self.match_table, idx))
        self.no_match_table.headerClicked.connect(lambda idx: self.onTableHeaderClicked(self.no_match_table, idx))

    def onTableHeaderClicked(self, table, column_index):
        pass

    def open_file(self):
        """Открытие файла"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите CSV файл", "", "CSV Files (*.csv);;All Files (*)"
        )

        if file_path:
            try:
                self.load_csv_data(file_path)
                self.update_tables()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def load_csv_data(self, filename):
        """Загрузка данных из CSV файла"""
        self.headers = []
        self.rows = []

        with open(filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            self.headers = next(csvreader)
            self.rows = list(csvreader)

    def update_tables(self):
        """Обновление всех таблиц"""
        self.update_data_table()
        self.update_count_table()
        self.update_match_table()
        self.update_no_match_table()

        tables = [self.data_table, self.count_table, self.match_table, self.no_match_table]
        for table in tables:
            if hasattr(table, 'sort_order'):
                table.sort_order = {}

    def update_data_table(self):
        """Обновление таблицы со всеми данными self.data_table"""
        self.data_table.setRowCount(len(self.rows))
        self.data_table.setColumnCount(len(self.headers))
        self.data_table.setHorizontalHeaderLabels(self.headers)

        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(cell)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                if j > 0:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.data_table.setItem(i, j, item)

    def update_count_table(self):
        """Таблица с численностью выпускников self.count_table"""
        self.count_table.setRowCount(len(self.rows))
        self.count_table.setColumnCount(2)
        self.count_table.setHorizontalHeaderLabels(["Специальность", "Численность выпускников, тыс. чел."])

        for i, row in enumerate(self.rows):
            if len(row) >= 2:
                item1 = QTableWidgetItem(row[0])
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.count_table.setItem(i, 0, item1)

                item2 = QTableWidgetItem(row[1])
                item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item2.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.count_table.setItem(i, 1, item2)

    def update_match_table(self):
        """Таблица с соответствием специальности self.match_table"""
        self.match_table.setRowCount(len(self.rows))
        self.match_table.setColumnCount(3)
        self.match_table.setHorizontalHeaderLabels([
            "Специальность",
            "Соответствует, тыс. чел.",
            "Соответствует, %"
        ])

        for i, row in enumerate(self.rows):
            if len(row) >= 5:
                item1 = QTableWidgetItem(row[0])
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.match_table.setItem(i, 0, item1)

                item2 = QTableWidgetItem(row[2])
                item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item2.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.match_table.setItem(i, 1, item2)

                item3 = QTableWidgetItem(row[4])
                item3.setFlags(item3.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item3.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.match_table.setItem(i, 2, item3)

    def update_no_match_table(self):
        """Таблица с несоответствием специальности self.no_match_table"""
        self.no_match_table.setRowCount(len(self.rows))
        self.no_match_table.setColumnCount(3)
        self.no_match_table.setHorizontalHeaderLabels([
            "Специальность",
            "Не соответствует, тыс. чел.",
            "Не соответствует, %"
        ])

        for i, row in enumerate(self.rows):
            if len(row) >= 6:
                item1 = QTableWidgetItem(row[0])
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.no_match_table.setItem(i, 0, item1)

                item2 = QTableWidgetItem(row[3])
                item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item2.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.no_match_table.setItem(i, 1, item2)

                item3 = QTableWidgetItem(row[5])
                item3.setFlags(item3.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item3.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.no_match_table.setItem(i, 2, item3)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()