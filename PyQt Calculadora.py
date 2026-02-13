import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox , QAction
)
from PyQt5.QtGui import QKeySequence

app= QApplication(sys.argv)

janela = QMainWindow()
janela.setWindowTitle('Bloco de Notas Simples')
janela.setGeometry(300,300,600,400)

texto_edit= QTextEdit()
janela.setCentralWidget(texto_edit)



def  novo_arquivo():
    texto_edit.clear()
def abrir_arquivo():
    caminho, _ = QFileDialog.getOpenFileName(janela,"Abrir Ficheiro","","Text Files(*.txt);; All Files (*)")
    if caminho:
        try:
            with open(caminho,'r', encoding='utf-8') as f:
                conteudo = f.read()
                texto_edit.setText(conteudo)
        except Exception as e:
            QMessageBox.warning(janela,"Erro",f"Não foi possível abrir o ficheiro:\n{e}")



def guardar_arquivo():
    caminho,_ =QFileDialog.getSave.FileName(janela,"Guardar Ficheiros","","Text Files (*.txt);; All Files (*)")
    if caminho:
        try:
            with open(caminho,'w', encoding='utf-8') as f:
                f.write(texto_edit.toPlainText())
        except Exception as e:
            QMessageBox.warning(janela, "Erro",f"Não foi possível guardar o ficheiro")






menu_arquivo = janela.menuBar().addMenu("Arquivo")

acao_novo = QAction("Novo", janela)
acao_novo.setShortcut(QKeySequence.New)
acao_novo.triggered.connect(novo_arquivo)

acao_abrir = QAction ("Abrir...",janela)
acao_abrir.setShortcut(QKeySequence.Open)
acao_abrir.triggered.connect(abrir_arquivo)

acao_guardar = QAction("Guardar...", janela)
acao_guardar.setShortcut(QKeySequence.Save)
acao_guardar.triggered.connect(guardar_arquivo)



menu_arquivo.addAction(acao_novo)
menu_arquivo.addAction(acao_abrir)
menu_arquivo.addAction(acao_guardar)

janela.show()
sys.exit(app.exec_())