import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
form_class = uic.loadUiType("UI/CharGen.ui")[0]

class charGenWindow(QDialog,form_class):
    def __init__(self,parant):
        super(charGenWindow, self ).__init__(parant)
        self.setupUi(self)
        self.btn_findimg.clicked.connect(self.btn_findimgclick)
        self.show()

    def btn_findimgclick(self):
        fname = QFileDialog.getOpenFileName(self, 'Select Image', "","Image Files(*.png *.jpg *.gif)", '/home')
        if fname[0]:
            qPixmapVar = QPixmap()
            qPixmapVar.load(fname[0])
            self.label_img.setPixmap(qPixmapVar)
        else:
            QMessageBox.about(self, "Warning","파일을 선택하지 않았습니다.")
        # TODO:class의 json과 연동하기