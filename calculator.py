from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.show()
        self.setStyleSheet("background: #333; font-size: 30px;") #to set the style
        
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()

        self.historyBox = QListWidget()
        self.entryBox = QLineEdit()

        main_layout.addWidget(self.historyBox)
    
      
app = QApplication([])
main = Main()
app.exec_()
