import sys
from PyQt6.QtWidgets import QApplication, QTextBrowser, QMainWindow, \
    QFileDialog


class Distributor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.menu1 = self.menuBar()
        self.menu2 = self.menuBar()
        self.file_menu = self.menu1.addMenu("Файл")
        self.vid_menu = self.menu2.addMenu("Распределитель")
        self.open_f = self.file_menu.addAction("Открыть")
        self.open_f.triggered.connect(self.load_file)
        self.save_f = self.file_menu.addAction("Сохранить")
        self.save_f.triggered.connect(self.save_file)
        self.txt = self.vid_menu.addAction("TXT")
        self.csv = self.vid_menu.addAction("CSV")
        self.png = self.vid_menu.addAction("PNG")
        self.py = self.vid_menu.addAction("PY")
        self.d = self.vid_menu.addAction("Другие")
        self.txt.triggered.connect(lambda: self.spread("txt"))
        self.csv.triggered.connect(lambda: self.spread("csv"))
        self.png.triggered.connect(lambda: self.spread("png"))
        self.py.triggered.connect(lambda: self.spread("py"))
        self.d.triggered.connect(lambda: self.spread(""))
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(5, 30)
        self.text_browser.setFixedSize(490, 160)
        self.text = []

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        with open(fname, "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.text = lines
            lines.sort()
            for i in lines:
                self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)

    def save_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        with open(fname, "w", encoding="utf-8") as f:
            f.write(self.text_browser.toPlainText())

    def spread(self, vid):
        self.text.sort()
        if vid == "txt":
            self.text_browser.setText("")
            for i in self.text:
                if ".txt" in i.lower():
                    self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)
        elif vid == "csv":
            self.text_browser.setText("")
            for i in self.text:
                if ".csv" in i.lower():
                    self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)
        elif vid == "png":
            self.text_browser.setText("")
            for i in self.text:
                if ".png" in i.lower():
                    self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)
        elif vid == "py":
            self.text_browser.setText("")
            for i in self.text:
                if ".py" in i.lower():
                    self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)
        else:
            self.text_browser.setText("")
            for i in self.text:
                if ".txt" not in i.lower() and ".csv" not in i.lower() and ".png" not in i.lower() and ".py" \
                        not in i.lower():
                    self.text_browser.append(i[:-1]) if "\n" in i else self.text_browser.append(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Distributor()
    ex.show()
    sys.exit(app.exec())