from qtpy.QtWidgets import *

# Initialize application
app = QApplication([])

# Create label
label = QLabel('Label shows inner text within window')

def say_hello(event): # Function which is to be called on clicking
    label.setText('Hello, world!') # On label text wiil be written

# Create button
button = QPushButton('Press me!')
button.clicked.connect(say_hello) # link button to function

# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
layout.SetMinimumSize = 200

# Apply layout to widget
widget = QWidget()
widget.setLayout(layout)

widget.show()

app.exec_()
