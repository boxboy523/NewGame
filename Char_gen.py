import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class charGenWindow(QDialog):
    def __init__(self,parant):
        super(charGenWindow, self ).__init__(parant)
        charGen_ui = "UI/CharGen.ui"
        uic.loadUi(charGen_ui, self)
        self.show()