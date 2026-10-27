from PySide6.QtWidgets import QTableWidgetItem
from datetime import datetime
from PySide6.QtWidgets import(
    QComboBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar de visitantes")
        self.resize(520, 460)
        # Dados temporarios: serão perdidos ao encerrarar o progama.
        self.registros = []
        
        self.titulo = QLabel("Recepção - Registro de Visitantes")
        self.campo_nome = QLineEdit()
        self.campo_nome.setPlaceholderText("Nome completo")
        
        
        self.combo_destino = QComboBox()
        self.combo_destino.addItems([
        "Selecione um setor",
        "Secretaria",
        "Coordenação",
        "laboratório",
        
    ])
        
        
        self.botao_cadastrar =QPushButton('Registrar visita')
        self.botao_limpar = QPushButton("Limpar campos")
        
        
        self.mensagen = QLabel("Preencha os campos e registre a visita.")
        self.lista = QListWidget()
        self.contador = QLabel("Visitas nesta sessão: 0 ")
        
        
        formulario = QFormLayout()
        formulario.addRow("Nome:",self.campo_nome) 
        formulario.addRow("Destino:", self.combo_destino)
        
        layout = QVBoxLayout()
        layout.addWidget(self.titulo)
        layout.addLayout(formulario)
        layout.addWidget(self.botao_cadastrar)
        layout.addWidget(self.botao_limpar)
        layout.addWidget(self.mensagen)
        layout.addWidget(QLabel("Visitantes registrados:"))
        layout.addWidget(self.lista)
        layout.addWidget(self.contador)
        self.setLayout(layout)
        
        #Os eventos da interfave chamam métodos da classe.self.botao_cadastrar.clicked.connect(self.resgistrar)
        
def registrar_visita(self):
    nome = self.campo_nome .texte().strip()
    destino = self.combo_destino.currentText()
    
    if not nome:
        self.mensagem.selfText("Informe o nome do visitante.")
        self.campo_nome.setFocus()
        return  
    
    if self.combo_destino.currentIndex() == 0:
        self.mensagem.setText("Selecione o setor de destino.")
        return
    
    registro = {"nome": nome, "destino": destino}
    self.registros.append(registro)
    self.lista.addItem(f"{nome} {destino}")
    self.contador.setText(
        f"Visitas nesta sessão: {len(self.registros)}"
    )
    
    self.mensagem.setText("Visita registrada com sucesso.")
    self.limpar_campos()
    
    
    def limpar_campos(self):
        self.campo_nome.clear()
        self.combo_destino.setCurrentIndex(0)
        self.campo_nome.setFocus()
        
        
        
    def registrar_saida(self):
        linha = self.tabela.currentRow()
        if linha < 0:
            self.mensagem.setText('Selecione uma visita na tabela.')
            return
        visita_id = int(self.tabela.item(linha, 0).text())
        for visita in self.visitas:
            if visita['id'] == visita_id:
                visita['saida'] = datetime.now().strftime('%H:%M:%S')
                self.crachas_livres.append(visita['cracha'])
                self.mensagem.setText(f"Saída registrada. Crachá {visita['cracha']} devolvido.")
                break
        self.atualizar_tabela()

    def atualizar_tabela(self):
        linhas = [v for v in self.visitas if v['saida'] is None]
        self.tabela.setRowCount(len(linhas))
        for i, v in enumerate(linhas):
            valores = [v['id'], self.visitantes[v['cpf']], v['setor'], v['cracha']]
            for j, valor in enumerate(valores):
                self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))