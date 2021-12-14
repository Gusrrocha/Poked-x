import httpx
from controller.tipo_poke import TipoPoke
from qt_core import *
FILE_UI = 'view/card_pokemon.ui'
class CardPoke(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.id.setText(f'{pokemon.id}')
        self.nome.setText(pokemon.nome)
        self.loadImg(pokemon.foto)

        # carrega os tipos
        self.load_type(pokemon.tipos)
    
    def load_type(self, tipos):
        for t in tipos:
            nome_tipo = t['type']['name']
            self.tipo_layout.addWidget(TipoPoke(nome_tipo))
            
    def loadImg(self, url):
        img = httpx.get(url).content
        image = QImage()
        image.loadFromData(img)
        self.img.setPixmap(QPixmap(image))
