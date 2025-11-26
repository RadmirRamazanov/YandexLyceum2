import sys
import csv
from PyQt6.QtWidgets import QApplication, QTextBrowser, QMainWindow, \
    QFileDialog


class ClosestStars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.menu1 = self.menuBar()
        self.menu2 = self.menuBar()
        self.file_menu = self.menu1.addMenu("Файл")
        self.vid_menu = self.menu2.addMenu("Выбор")
        self.open_f = self.file_menu.addAction("Открыть")
        self.open_f.triggered.connect(self.load_file)
        self.save_f = self.file_menu.addAction("Сохранить")
        self.save_f.triggered.connect(self.save_file)
        self.clss = self.vid_menu.addMenu("Спектральный класс")
        self.ss = self.vid_menu.addMenu("Расстояние")
        self.clss.addAction("O").triggered.connect(lambda: self.spread("O"))
        self.clss.addAction("B").triggered.connect(lambda: self.spread("B"))
        self.clss.addAction("A").triggered.connect(lambda: self.spread("A"))
        self.clss.addAction("F").triggered.connect(lambda: self.spread("F"))
        self.clss.addAction("G").triggered.connect(lambda: self.spread("G"))
        self.clss.addAction("K").triggered.connect(lambda: self.spread("K"))
        self.clss.addAction("M").triggered.connect(lambda: self.spread("M"))
        self.ss.addAction("до 10").triggered.connect(lambda: self.spread2(10))
        self.ss.addAction("до 20").triggered.connect(lambda: self.spread2(20))
        self.ss.addAction("до 30").triggered.connect(lambda: self.spread2(30))
        self.ss.addAction("свыше 30").triggered.connect(lambda: self.spread2(31))
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(5, 30)
        self.text_browser.setFixedSize(490, 160)
        self.text = []
        self.html_text = ""

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        with open(fname, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            self.text = list(reader)[1:]

    def save_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        with open(fname, "w", encoding="utf-8") as f:
            f.write(self.text_browser.toPlainText())

    def spread(self, v):
        self.html_text = ""
        self.text_browser.clear()
        self.text.sort()
        self.html_text += f"""<h3>Спектральный класс {v}</h3>"""
        for i in self.text:
            if i[2][0] == v:
                self.text_browser.append(f"{i[0]} {i[1]}")
                self.html_text += f"""<p>{i[0]} {i[1]}</p>"""
        self.text_browser.setHtml(self.html_text)

    def spread2(self, v):
        self.html_text = ""
        self.text_browser.clear()
        self.text.sort()
        if v == 31:
            self.html_text += """<h3>Расстояние свыше 30</h3>"""
        else:
            self.html_text += f"""<h3>Расстояние до {v}</h3>"""
        for i in self.text:
            if v != 31:
                if int(float(i[-1])) <= v:
                    self.html_text += f"""<p>{i[0]} {i[1]}</p>"""
            else:
                if (int(float(i[-1]))) >= 30:
                    self.html_text += f"""<p>{i[0]} {i[1]}</p>"""
        self.text_browser.setHtml(self.html_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ClosestStars()
    ex.show()
    sys.exit(app.exec())