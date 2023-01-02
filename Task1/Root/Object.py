class UObject():
    def __init__(self):
        self.__ID = 0
        self.__Outer = None

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
