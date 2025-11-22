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
    <height>588</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>19</x>
      <y>19</y>
      <width>761</width>
      <height>471</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QTextBrowser" name="textBrowser"/>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit">
       <property name="text">
        <string></string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>500</y>
      <width>761</width>
      <height>41</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Отправить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton1">
       <property name="text">
        <string>Светлая тема</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>807</width>
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

dark_style = """
             QMainWindow {
                            background-color: #2b2b2b; /* Тёмно-серый фон */
                        }
                        QTextBrowser {
                            background-color: #3c3f41; /* Фон чуть светлее */
                            color: #a9b7c6; /* Светло-серый текст */
                            border: 2px solid #555; /* Рамка в 2 пикселя, сплошная, серая */
                            font-size: 14px; /* Размер шрифта */
                            font-family: "Courier New", monospace; /* Хакерский моноширинный шрифт */
                        }
                        QPushButton {
                            background-color: #3c3f41;
                            color: #a9b7c6;
                            border: 1px solid #555;
                            border-radius: 5px;
                            padding: 5px 10px;
                        }
                        QPushButton:hover {
                            border: 2px solid #3498db; /* Синяя рамка */
                            border-radius: 10px;
                        }
                        QPushButton:pressed {
                            border: 2px solid #2980b9; /* Тёмно-синяя рамка */
                            border-radius: 10px;
                        }
"""
light_style = """
              QMainWindow {
                    background-color: white; /* Тёмно-серый фон */
              }
                        QTextBrowser {
                            background-color: white; /* Фон чуть светлее */
                            color: black; /* Светло-серый текст */
                            border: 2px solid #555; /* Рамка в 2 пикселя, сплошная, серая */
                            font-size: 14px; /* Размер шрифта */
                            font-family: "Courier New", monospace; /* Хакерский моноширинный шрифт */
                        }
                        QPushButton {
                            background-color: white;
                            color: black;
                            border: 1px solid #555;
                            border-radius: 5px;
                            padding: 5px 10px;
                        }
                        QPushButton:hover {
                            border: 2px solid #3498db; /* Синяя рамка */
                            border-radius: 10px;
                        }
                        QPushButton:pressed {
                            border: 2px solid #2980b9; /* Тёмно-синяя рамка */
                            border-radius: 10px;
                        }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.c = 0
        self.setStyleSheet(dark_style)
        self.lineEdit.setPlaceholderText("Введите сообщение...")
        self.pushButton.clicked.connect(self.send_message)
        self.pushButton1.clicked.connect(self.change_theme)
        self.lineEdit.returnPressed.connect(self.send_message)
        self.html_text = ""

    def send_message(self):
        self.html_text += f"""<p><b>Message: </b>{self.lineEdit.text()}</p>"""
        self.textBrowser.setHtml(self.html_text)
        self.lineEdit.clear()

    def change_theme(self):
        self.c += 1
        self.setStyleSheet(light_style) if self.c % 2 == 1 else self.setStyleSheet(dark_style)
        self.pushButton1.setText("Тёмная тема") if self.c % 2 == 1 else self.pushButton1.setText("Светлая тема")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())