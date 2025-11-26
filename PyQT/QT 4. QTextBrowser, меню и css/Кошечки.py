import sys
import io
import csv
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>-1</x>
      <y>-1</y>
      <width>801</width>
      <height>571</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLineEdit" name="lineEdit"/>
     </item>
     <item>
      <widget class="QTextBrowser" name="textBrowser"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class CatBreeds(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.lineEdit.textChanged.connect(self.write)
        self.colors = ["Cornsilk", "BlanchedAlmond", "Bisque", "NavajoWhite",
                       "Wheat", "BurlyWood", "Tan"]

    def write(self):
        with open("cat_breeds.csv", "r", encoding="utf-8") as f:
            c = 0
            self.reader = csv.reader(f)
            html_text = ""
            for i in self.reader:
                i = " ".join(i).split(";")
                if self.lineEdit.text().lower() in i[0].lower():
                    html = f"""
                    <p style="background:{self.colors[c % len(self.colors)]}"><b>{i[0]}, </b>{i[1]}, {i[2]}, {i[3]},
                    {i[4]}, {i[5]}</p>
                    """
                    c += 1
                    html_text += html
                self.textBrowser.setHtml(html_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CatBreeds()
    ex.show()
    sys.exit(app.exec())