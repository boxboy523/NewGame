class squad:
    Name = "Unknown Squad"
    def __init__(self, name, *units):
        self.Name = name
        self.Units = list(units)
