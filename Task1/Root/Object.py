from Subsistems.ResiterSubsistem import NameSubsistem


class UObject():
    def __init__(self, ID=-1, Outer=None):
        if (not NameSubsistem.RegisterNewObject(self, ID)):
            print("Error: wrong ID")
        self.__ID = NameSubsistem.GetIDByReference(self)
        self.__Outer = Outer

    def __del__(self):
        NameSubsistem.DeleteObject(self)

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, NewID):
        self.__ID = NewID

    @property
    def Outer(self):
        return self.__Outer

    @Outer.setter
    def Outer(self, NewOuter):
        self.__Outer = NewOuter.ref()

    def Print(self):
        pass
