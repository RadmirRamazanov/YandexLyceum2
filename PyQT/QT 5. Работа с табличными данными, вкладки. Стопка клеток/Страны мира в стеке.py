import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QTableView,
                             QVBoxLayout, QWidget, QHeaderView,
                             QFileDialog, QComboBox, QHBoxLayout, QLabel)
from PyQt6.QtCore import Qt, QVariant, QModelIndex, QAbstractTableModel
from PyQt6.QtGui import QAction, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Данные о странах")
        self.setGeometry(100, 100, 1000, 600)
        self.headers = []
        self.rows = []
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        self.selection_layout = QHBoxLayout()
        self.selection_label = QLabel("Выберите характеристику:")
        self.page_combo = QComboBox()
        self.page_combo.currentIndexChanged.connect(self.change_page)
        self.selection_layout.addWidget(self.selection_label)
        self.selection_layout.addWidget(self.page_combo)
        self.selection_layout.addStretch()
        self.selection_label.hide()
        self.page_combo.hide()
        self.stack_widget = QStackedWidget()
        main_layout.addLayout(self.selection_layout)
        main_layout.addWidget(self.stack_widget)
        self.create_menu()
        self.init_empty_pages()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        open_action = QAction("Открыть", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def init_empty_pages(self):
        empty_label = QLabel("Откройте файл через меню 'Файл → Открыть'")
        empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_label.setFont(QFont("Arial", 14))
        empty_widget = QWidget()
        layout = QVBoxLayout(empty_widget)
        layout.addWidget(empty_label)
        self.stack_widget.addWidget(empty_widget)
        self.stack_widget.setCurrentIndex(0)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "CSV Files (*.csv)")
        if file_path:
            self.load_csv_data(file_path)

    def load_csv_data(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                self.headers = next(reader)
                self.rows = []
                for row in reader:
                    if row and len(row) >= 8:
                        self.rows.append(row)
            self.create_pages()
        except Exception:
            return

    def create_pages(self):
        while self.stack_widget.count() > 0:
            widget = self.stack_widget.widget(0)
            self.stack_widget.removeWidget(widget)
        self.page_combo.clear()
        self.selection_label.show()
        self.page_combo.show()
        if len(self.headers) < 2:
            return
        characteristic_columns = list(range(1, min(8, len(self.headers))))
        for col_idx in characteristic_columns:
            characteristic_name = self.headers[col_idx]
            self.page_combo.addItem(characteristic_name)
            table_view = QTableView()
            model = CsvTableModel(
                headers=[self.headers[0], characteristic_name],
                rows=[[row[0], row[col_idx]] for row in self.rows]
            )
            table_view.setModel(model)
            table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.stack_widget.addWidget(table_view)
        if self.stack_widget.count() > 0:
            self.stack_widget.setCurrentIndex(0)
            self.page_combo.setCurrentIndex(0)

    def change_page(self, index):
        if 0 <= index < self.stack_widget.count():
            self.stack_widget.setCurrentIndex(index)


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
            return self._rows[index.row()][index.column()]
        return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Horizontal and 0 <= section < len(self._headers):
            return self._headers[section]
        return section + 1

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