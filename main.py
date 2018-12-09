#Some basic libraries import
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

#Telling that it's an application
app = QApplication([])

#Creating a window
window = QWidget()


#Creating a layout
layout= QVBoxLayout()

#Adding buttons to layout
layout.addWidget(QPushButton('Top')) 
layout.addWidget(QPushButton('Bottom'))


#Placing layout in window because window GUI have many layouts :)
window.setLayout(layout)

#Displaying it
window.show()

#It will execute until user closes it
app.exec_()
