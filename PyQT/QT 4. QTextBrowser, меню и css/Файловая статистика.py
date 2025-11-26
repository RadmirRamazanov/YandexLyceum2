import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QTextBrowser, QMainWindow, \
    QLineEdit


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.button = QPushButton(self)
        self.button.setText("Рассчитать")
        self.button.move(300, 15)
        self.button.clicked.connect(self.min_med_max)
        self.filenameEdit = QLineEdit(self)
        self.filenameEdit.move(150, 15)
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.move(10, 60)
        self.textBrowser.setFixedSize(480, 100)

    def min_med_max(self):
        try:
            with open(self.filenameEdit.text(), "r", encoding="utf-8") as f:
                self.textBrowser.setText("")
                lines = f.readlines()
                nums = []
                sum = 0
                for i in lines:
                    i = i.split()
                    for j in i:
                        try:
                            nums.append(int(j))
                            sum += int(j)
                        except ValueError:
                            self.statusBar().showMessage("Файл содержит некорректные данные")
                            return
                if len(nums) == 0:
                    self.statusBar().showMessage("Указанный файл пуст")
                    return
                self.textBrowser.append(f"Максимальное значение = {max(nums)}")
                self.textBrowser.append(f"Минимальное значение = {min(nums)}")
                sred = "{:.2f}".format(sum / len(nums))
                self.textBrowser.append(f"Среднее значение = {sred}")
                with open("out.txt", "w", encoding="utf-8") as out:
                    out.write(f"Максимальное значение = {max(nums)}\n")
                    out.write(f"Минимальное значение = {min(nums)}\n")
                    out.write(f"Среднее значение = {sred}\n")
        except FileNotFoundError:
            self.textBrowser.setText("")
            self.statusBar().showMessage("Указанный файл не существует")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())