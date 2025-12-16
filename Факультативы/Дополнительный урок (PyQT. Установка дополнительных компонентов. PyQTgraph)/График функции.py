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
    <width>600</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="PlotWidget" name="graphicsView">
    <property name="geometry">
     <rect>
      <x>25</x>
      <y>21</y>
      <width>551</width>
      <height>271</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>322</x>
      <y>310</y>
      <width>141</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Построить</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>310</y>
      <width>180</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string>y = </string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_from">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>310</y>
      <width>40</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_to">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>310</y>
      <width>40</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string>10</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>600</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header location="global">pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.graphicsView.clear()
        func = self.lineEdit.text()[4:]
        if "^" in func:
            func = func.replace("^", "**")
        fx = int(self.lineEdit_from.text())
        sx = int(self.lineEdit_to.text())
        self.graphicsView.plot([i for i in range(fx, sx + 1)],
                              [eval(func) for x in range(fx, sx + 1)], pen='r')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())