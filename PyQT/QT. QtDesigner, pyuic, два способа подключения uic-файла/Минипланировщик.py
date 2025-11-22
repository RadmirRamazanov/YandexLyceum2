import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTimeEdit" name="timeEdit">
    <property name="geometry">
     <rect>
      <x>7</x>
      <y>10</y>
      <width>391</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QCalendarWidget" name="calendarWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>392</width>
      <height>236</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>290</y>
      <width>391</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addEventBtn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>391</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить событие</string>
    </property>
   </widget>
   <widget class="QListWidget" name="eventList">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>10</y>
      <width>361</width>
      <height>341</height>
     </rect>
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


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.addEventBtn.clicked.connect(self.planner)

    def planner(self):
        zadacha = (f"{self.calendarWidget.selectedDate().toString('yyyy-MM-dd')} "
                   f"{self.timeEdit.time().toString()} - {self.lineEdit.text()}")
        self.eventList.addItem(zadacha)
        self.eventList.sortItems(Qt.SortOrder.AscendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())