class place:
    Name = "Somewhere"
    Units = []
    Things = []
    ConnectedPlace = []

    def __init__(self,name,CNP):
        self.Name = name
        self.ConnectedPlace = CNP

    def __str__(self):
        return self.Name

    def returnDict(self):
        dic={'Name':self.Name , 'Units':self.Units , 'Things':self.Things , 'ConnectedPlace':self.ConnectedPlace}
        return dic