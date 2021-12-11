from controller.card_pokemon import CardPoke
from qt_core import *
import services.api as api
FILE_UI = 'view/main_window.ui'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.load_pokemons()
   
    # carrega os pokemons no grind
    def load_pokemons(self):
        # receber uma lista contendo todos os pokemons
        # LÓGICA PARA PREENCHER O GRID COM OS CARDS
        lista = api.load()
        linha = 0
        i = 0
        try:
            while i < len(lista):
                for coluna in range(0,4): # for para mover nas colunas
                    # insere o pokemon no grid
                    self.grid_pokemons.addWidget(CardPoke(lista[i]), linha, coluna)
                    i += 1
                linha += 1
        except:
            print("Acabou a lista...")
        