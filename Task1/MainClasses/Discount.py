class UDiscount():
    def __init__(self, Client):
        self.Client = Client
        self.Number = 1

    def CheckDiscount(self, Pay):
        if self.Number > 1:
            return self.ApplyDiscount(Pay)

    def ApplyDiscount(self, Pay):
        return Pay * 0.9
