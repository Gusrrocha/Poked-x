from qt_core import *
FILE_UI = 'view/tipo_poke.ui'
class TipoPoke(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)