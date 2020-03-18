import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Unit import unit
from Place import place
from enum import Enum
import Char_gen
import threading
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("UI\MainWindow.ui")[0]

class strFlag(Enum):
    NONE = None

class sceneFlag(Enum):
    START = 0
    IDLE = 1

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    Home = place("집",[])
    StrFlag = strFlag.NONE
    SceneFlag = sceneFlag.START
    lastStr = "None"

    player = unit("???", 120, 20, 20, Home, None)
    enemy = unit("ㅏㅏㅏ", 120, 20, 2, Home, None)

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.btn_1.clicked.connect(self.button1Function)
        #self.btn_2.clicked.connect(self.button2Function)
        self.btn_clear.clicked.connect(self.mainTextBrowser.clear)
        self.mainLineEdit.returnPressed.connect(self.enterString)
        self.tabRefrash()
        Char_gen.charGenWindow(self)
        self.player.Window = self
        self.enemy.Window = self
        self.t = threading.Thread(target = self.gameLoop)
        self.t.daemon = True
        self.t.start()

    def enterString(self): # 입력
        text = self.mainLineEdit.text()
        if text != "":
            self.lastStr = text
            self.appendString(text,self.player.Name)
            self.mainLineEdit.clear()

    def appendString(self,text, *speaker): #말하기
        if speaker == ():
            speaker = ("System",)
        speakers = ""
        for i in range(len(speaker)):
            speakers += str(speaker[i])
            if i != len(speaker)-1:
                speakers += ","
        self.mainTextBrowser.append(speakers + " : " + str(text))

    def tabRefrash(self):
        self.text_name.setText(self.player.Name)
        self.text_hp.setText(str(self.player.HP))
        self.text_atk.setText(str(self.player.Atk))
        self.text_place.setText(str(self.player.Place))
        self.text_def.setText(str(self.player.Def))

    def gameLoop(self):
        done = False

        while not done:
            if  time.time() - int(time.time()) < 0.005:

                time.sleep(0.005)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()