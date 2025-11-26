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
    <width>800</width>
    <height>481</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>-1</x>
      <y>39</y>
      <width>801</width>
      <height>351</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <item>
      <widget class="QPlainTextEdit" name="text1"/>
     </item>
     <item>
      <widget class="QPlainTextEdit" name="text2"/>
     </item>
    </layout>
   </widget>
   <widget class="QDoubleSpinBox" name="alert_value">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>801</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="checkBtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>390</y>
      <width>801</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Сравнить</string>
    </property>
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


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.checkBtn.clicked.connect(self.plagiat)

    def plagiat(self):
        text1 = self.text1.toPlainText()
        text2 = self.text2.toPlainText()
        lines1 = text1.split("\n")
        lines2 = text2.split("\n")
        if text1.endswith('\n'):
            lines1 = lines1[:-1]
        if text2.endswith('\n'):
            lines2 = lines2[:-1]
        set1 = set(lines1)
        set2 = set(lines2)
        ans = "{:.2f}".format(len(set1 & set2) / len(set1 | set2) * 100)
        intans = len(set1 & set2) / len(set1 | set2) * 100
        self.statusBar().move(1, 420)
        self.statusBar().showMessage(f"Тексты похожи на {ans}%, плагиат") if intans >= self.alert_value.value() else (
            self.statusBar().showMessage(f"Тексты похожи на {ans}%, не плагиат"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())