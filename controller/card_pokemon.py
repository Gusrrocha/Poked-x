import httpx
from qt_core import *
FILE_UI = 'view/card_pokemon.ui'
class CardPoke(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.id.setText(f'{pokemon.id}')
        self.nome.setText(pokemon.nome)
        self.loadImg(pokemon.foto)
    
    def loadImg(self, url):
        img = httpx.get(url).content
        image = QImage()
        image.loadFromData(img)
        self.img.setPixmap(QPixmap(image))
