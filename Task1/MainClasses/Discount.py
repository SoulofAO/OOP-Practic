class UDiscount():
    def __init__(self, Client):
        self.__Client = Client
        self.__Number = 1

    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, NewClient):
        self.__Client = NewClient

    @property
    def Number(self):
        return self.__Number

    @Number.setter
    def Number(self, NewNumber):
        self.__Number = NewNumber

    def CheckDiscount(self, Pay):
        if self.Number > 1:
            return self.ApplyDiscount(Pay)

    def ApplyDiscount(self, Pay):
        return Pay * 0.9
