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
