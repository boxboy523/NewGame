from enum import Enum
from Place import place
class unit:

    Name = "UnKnown"
    MaxHP = 100
    HP=MaxHP
    Atk = 0
    Def = 0
    Place = None
    Window = None
    Live = True
    item = []

    def __init__(self, name = Name, hp = MaxHP, atk = Atk, deff = Def, place = Place, window = Window):
        self.Name = name
        self.MaxHP = hp
        self.HP = self.MaxHP
        self.Atk = atk
        self.Def = deff
        self.Place = place
        self.Window = window

    def __str__(self):
        return ("Name:"+self.Name)

    def Attack(self,target):
        damage = max(self.Atk-target.Def,1)
        target.HP -= damage
        if target.Live:
            self.Window.appendString(self.Name+"은 "+target.Name+"에게 "+str(damage)+"만큼의 피해를 주었다!")
            if target.HP <= 0:
                target.Die()
        else:
            self.Window.appendString("죽은 적은 때릴수 없다.")

    def Die(self):
        self.Window.appendString(self.Name+"은 쓰러졌다!")
        self.Live = False

    def returnDict(self):
        dic = {'Name': self.Name, 'MaxHP': self.MaxHP, 'HP': self.HP, 'Atk': self.Atk, 'Def': self.Def, 'Place': self.Place, 'Live': str(self.Live), 'item': self.item }
        return dic