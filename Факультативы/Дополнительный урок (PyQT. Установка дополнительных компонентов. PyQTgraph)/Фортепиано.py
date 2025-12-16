import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtMultimedia
from PyQt6.QtCore import Qt


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>854</width>
    <height>225</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>90</y>
      <width>795</width>
      <height>81</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="pushButton_8">
       <property name="text">
        <string>До(Q)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_7">
       <property name="text">
        <string>Ре(W)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_6">
       <property name="text">
        <string>Ми(E)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_5">
       <property name="text">
        <string>Фа(R)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_4">
       <property name="text">
        <string>Соль(T)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_3">
       <property name="text">
        <string>Ля(Y)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Си(U)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>До(I)</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>380</x>
      <y>30</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Palatino Linotype</family>
      <pointsize>26</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>NOTI</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>854</width>
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


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.setup_note)
        self.pushButton_2.clicked.connect(self.setup_note)
        self.pushButton_3.clicked.connect(self.setup_note)
        self.pushButton_4.clicked.connect(self.setup_note)
        self.pushButton_5.clicked.connect(self.setup_note)
        self.pushButton_6.clicked.connect(self.setup_note)
        self.pushButton_7.clicked.connect(self.setup_note)
        self.pushButton_8.clicked.connect(self.setup_note)

    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key.Key_Q or ev.key() == Qt.Key.Key_I:
            media = QtCore.QUrl.fromLocalFile("noty-do.mp3")
        elif ev.key() == Qt.Key.Key_W:
            media = QtCore.QUrl.fromLocalFile("re.mp3")
        elif ev.key() == Qt.Key.Key_E:
            media = QtCore.QUrl.fromLocalFile("mi.mp3")
        elif ev.key() == Qt.Key.Key_R:
            media = QtCore.QUrl.fromLocalFile("fa.mp3")
        elif ev.key() == Qt.Key.Key_T:
            media = QtCore.QUrl.fromLocalFile("sol.mp3")
        elif ev.key() == Qt.Key.Key_Y:
            media = QtCore.QUrl.fromLocalFile("lja.mp3")
        elif ev.key() == Qt.Key.Key_U:
            media = QtCore.QUrl.fromLocalFile("si.mp3")
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()

    def setup_note(self):
        sender = self.sender()
        if sender.text() == self.pushButton_8.text() or sender.text() == self.pushButton.text():
            media = QtCore.QUrl.fromLocalFile("noty-do.mp3")
        elif sender.text() == self.pushButton_7.text():
            media = QtCore.QUrl.fromLocalFile("re.mp3")
        elif sender.text() == self.pushButton_6.text():
            media = QtCore.QUrl.fromLocalFile("mi.mp3")
        elif sender.text() == self.pushButton_5.text():
            media = QtCore.QUrl.fromLocalFile("fa.mp3")
        elif sender.text() == self.pushButton_4.text():
            media = QtCore.QUrl.fromLocalFile("sol.mp3")
        elif sender.text() == self.pushButton_3.text():
            media = QtCore.QUrl.fromLocalFile("lja.mp3")
        elif sender.text() == self.pushButton_2.text():
            media = QtCore.QUrl.fromLocalFile("si.mp3")
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Square1()
    window.show()
    sys.exit(app.exec())