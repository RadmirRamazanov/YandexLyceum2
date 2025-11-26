import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>410</width>
    <height>310</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPlainTextEdit" name="text_edit">
   <property name="geometry">
    <rect>
     <x>160</x>
     <y>30</y>
     <width>231</width>
     <height>251</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="new_button">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>129</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Создать новый</string>
   </property>
  </widget>
  <widget class="QPushButton" name="save_button">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>130</y>
     <width>129</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Сохранить файл</string>
   </property>
  </widget>
  <widget class="QPushButton" name="open_button">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>180</y>
     <width>129</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Открыть файл</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="filename_edit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>129</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.new_button.clicked.connect(self.new_file)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def new_file(self):
        self.text_edit.clear()
        self.filename_edit.clear()

    def save_file(self):
        if self.filename_edit.text() != "":
            with open(self.filename_edit.text(), "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())

    def open_file(self):
        try:
            with open(self.filename_edit.text(), "r", encoding="utf-8") as f:
                lines = f.readlines()
                for i in lines:
                    self.text_edit.appendPlainText(i[:-1]) if i != lines[-1] else \
                        self.text_edit.appendPlainText(i)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())