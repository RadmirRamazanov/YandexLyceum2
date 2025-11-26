import sys
import io
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
    <width>807</width>
    <height>601</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>741</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>60</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>#000</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>p</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h1</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h2</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h3</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h4</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h5</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>h6</string>
     </property>
    </item>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>60</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Вывести</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>60</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Очистить</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="textBrowser">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>741</width>
      <height>401</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>807</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class HeadersInColor(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.text = ""
        self.z = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)
        self.html_text = ""

    def write_text(self):
        a = self.comboBox.currentText()
        self.text += self.lineEdit.text()
        self.html_text += f"""
        <{a}><font color="{self.lineEdit_2.text()}">{self.lineEdit.text()}</font></{a}>
        """
        self.textBrowser.setHtml(self.html_text)

    def clear_text(self):
        self.textBrowser.clear()
        self.html_text = ""
        self.text = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HeadersInColor()
    ex.show()
    sys.exit(app.exec())