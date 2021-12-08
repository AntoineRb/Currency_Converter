from PySide2 import QtWidgets
import currency_converter    

class App(QtWidgets.QWidget):
    def __init__(self): 
        super().__init__() 
        self.c = currency_converter.CurrencyConverter() #Importe les devises      
        self.setWindowTitle("Convertisseur de devises")   
        self.setup_ui()
        self.set_default_values()
        self.setup_connection() 
        self.setup_css()
        self.resize(500, 50)
    def setup_ui(self): 
        self.layout_ = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo =QtWidgets.QComboBox() 
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")

        self.layout_.addWidget(self.cbb_devisesFrom)
        self.layout_.addWidget(self.spn_montant)
        self.layout_.addWidget(self.cbb_devisesTo)
        self.layout_.addWidget(self.spn_montantConverti)
        self.layout_.addWidget(self.btn_inverser)

    def set_default_values(self): 
        self.cbb_devisesFrom.addItems(sorted(self.c.currencies))
        self.cbb_devisesTo.addItems(sorted(self.c.currencies))
        self.cbb_devisesFrom.setCurrentText("EUR") 
        self.cbb_devisesTo.setCurrentText("EUR")
        
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100) 
        self.spn_montantConverti.setValue(100)

    def setup_connection(self): 
        
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)
    
    def compute(self): 
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        
        try: 
            resultat = self.c.convert(montant, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion n'a pas fonctionné.")
        else:
            self.spn_montantConverti.setValue(resultat) 
            
    def inverser_devise(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()

    def setup_css(self): 
        self.setStyleSheet("""
        background-color: rgba(30, 30, 30, 0.5);
        color: rgb(240, 240, 240);
        border: none;
        """)

app = QtWidgets.QApplication([]) 
win = App()                      
win.show()                        
app.exec_()                      
