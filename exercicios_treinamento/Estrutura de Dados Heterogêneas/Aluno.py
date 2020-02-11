from Data import Data

class Aluno:
    nome = ""
    idade = 0
    status = False
    dataNasc = Data()
    
    # Construtor
    def __init__(self):
        self.dataNasc = Data()
        