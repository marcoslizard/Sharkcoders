import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)

app = QApplication(sys.argv)

janela = QMainWindow()
janela.setWindowTitle('Calculadora Antiga')
janela.setGeometry(300, 300, 600, 400)

# ---- Widget central ----
widget_central = QWidget()
janela.setCentralWidget(widget_central)





# ---- Layout ----
layout = QVBoxLayout()

input_field = QLineEdit()
label = QLabel("")

layout.addWidget(input_field)

input_field2 = QLineEdit()
label = QLabel("")

layout.addWidget(input_field2)

layout.addWidget(QPushButton("Somar"))
layout.addWidget(QPushButton("Subtrair"))
layout.addWidget(QPushButton("Dividir"))
layout.addWidget(QPushButton("Multiplicar"))
layout.addWidget(QLabel(""))


layout.addWidget(label)

# Aplicando layout ao widget central
widget_central.setLayout(layout)

janela.show()
sys.exit(app.exec_())

