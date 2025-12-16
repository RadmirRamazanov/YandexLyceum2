import io
import sys
from PIL import Image
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

t = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>416</width>
    <height>440</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QSlider" name="alpha">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>41</width>
      <height>371</height>
     </rect>
    </property>
    <property name="sliderPosition">
     <number>99</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>30</y>
      <width>291</width>
      <height>261</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>416</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class AlphaManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(t)
        uic.loadUi(f, self)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)
        self.alpha.valueChanged.connect(self.update_image)
        self.pixmap = QPixmap('orig.jpg')
        self.image.setPixmap(self.pixmap)

    def update_image(self):
        im = Image.open("orig.jpg")
        im.putalpha(self.alpha.value())
        im.save('new.png')
        self.pixmap = QPixmap('new.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())

