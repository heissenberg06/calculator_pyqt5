from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(400, 500)
        self.show()
        self.setStyleSheet("background: #333; font-size: 30px;") #to set the style
        
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()

        self.historyBox = QListWidget()
        self.entryBox = QLineEdit()
        self.entryBox.setStyleSheet("color: white")

        main_layout.addWidget(self.historyBox)
        main_layout.addWidget(self.entryBox)

        button_1 = QPushButton(text = '1', clicked = lambda:self.insertNum('1'))
        button_2 = QPushButton(text = '2', clicked = lambda:self.insertNum('2'))
        button_3 = QPushButton(text = '3', clicked = lambda:self.insertNum('3'))
        button_4 = QPushButton(text = '4', clicked = lambda:self.insertNum('4'))
        button_5 = QPushButton(text = '5', clicked = lambda:self.insertNum('5'))
        button_6 = QPushButton(text = '6', clicked = lambda:self.insertNum('6'))
        button_7 = QPushButton(text = '7', clicked = lambda:self.insertNum('7'))
        button_8 = QPushButton(text = '8', clicked = lambda:self.insertNum('8'))
        button_9 = QPushButton(text = '9', clicked = lambda:self.insertNum('9'))
        button_0 = QPushButton(text = '0', clicked = lambda:self.insertNum('0'))
      
        button_dot = QPushButton(text = '.', clicked = lambda:self.insertNum('.'))
        button_openpar = QPushButton(text = '(', clicked = lambda:self.insertNum('('))
        button_closepar = QPushButton(text = ')', clicked = lambda:self.insertNum(')'))
        
        button_add = QPushButton(text = '+', clicked = lambda:self.insertNum('+'))
        button_sub = QPushButton(text = '-', clicked = lambda:self.insertNum('-'))
        button_mult = QPushButton(text = '*', clicked = lambda:self.insertNum('*'))
        button_div = QPushButton(text = '/', clicked = lambda:self.insertNum('/'))

        button_clear = QPushButton(text= 'C', clicked = lambda:self.clear_items())
        button_calculate = QPushButton(text = '=', clicked = lambda:self.calculate())

        button_sqrt = QPushButton(text= '√', clicked = lambda:self.insertNum('√'))
        button_square = QPushButton(text= '^', clicked = lambda:self.insertNum('^'))

        button_layout.addWidget(button_1, 0, 0)
        button_layout.addWidget(button_2, 0, 1)
        button_layout.addWidget(button_3, 0, 2)
        button_layout.addWidget(button_4, 1, 0)
        button_layout.addWidget(button_5, 1, 1)
        button_layout.addWidget(button_6, 1, 2)
        button_layout.addWidget(button_7, 2, 0)
        button_layout.addWidget(button_8, 2, 1)
        button_layout.addWidget(button_9, 2, 2)
        button_layout.addWidget(button_0, 3, 1)

        button_layout.addWidget(button_dot, 4, 1)
        button_layout.addWidget(button_openpar, 3, 0)
        button_layout.addWidget(button_closepar, 3, 2)
        
        button_layout.addWidget(button_add, 0, 3)
        button_layout.addWidget(button_sub, 1, 3)
        button_layout.addWidget(button_div, 2, 3)
        button_layout.addWidget(button_mult, 3, 3)
         
        button_layout.addWidget(button_clear, 4, 0)
        button_layout.addWidget(button_calculate, 5, 0, 1, 4)

        button_layout.addWidget(button_sqrt, 4, 3)
        button_layout.addWidget(button_square, 4, 2)






        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
    



    def insertNum(self, num):
        self.entryBox.insert(num)

    def clear_items(self):
        self.entryBox.clear()

    def calculate(self):
        items_to_calculate = self.entryBox.text()
        try:
            if items_to_calculate:
                items_to_calculate = str(items_to_calculate)
                items_to_calculate = self.convert_sqrt(items_to_calculate)
                print(items_to_calculate)
                result = eval(items_to_calculate) #calculation function
                self.entryBox.setText(str(result))
                # self.historyBox.addItem(str(result))
                self.historyBox.addItem(f"{items_to_calculate} = {result}")

        except Exception as e:
            print(e)
            self.entryBox.setText(f"error :{e}")

    def convert_sqrt(self, process:str)-> str:
        process = list(process)
        i = 0
        while i < len(process):
            if process[i] == '√':
                process.insert(i+2, '*')
                process.insert(i+3, '*')
                process.insert(i+4, '0.5')
                del process[i]
            i += 1
        return ''.join(process)


app = QApplication([])
app.setStyle('fusion')
main = Main()
app.exec_()


a : int = 3 