from Root.Object import UObject
class UHotelRoom(UObject):
    def __init__(self, ID = -1, Outer = None, MaxNumber=1, Comfort=1, Pay=1000):
        UObject.__init__(self,ID,Outer)
        self.__MaxNumber = int(MaxNumber)
        self.__Comfort = int(Comfort)
        self.__Pay = int(Pay)

    @property
    def MaxNumber(self):
        return self.__MaxNumber

    @MaxNumber.setter
    def MaxNumber(self, NewMaxNumber):
        self.__MaxNumber = NewMaxNumber

    @property
    def Comfort(self):
        return self.__Comfort

    @Comfort.setter
    def Comfort(self, NewComfort):
        self.__Comfort = NewComfort

    @property
    def Pay(self):
        return self.__Pay

    @Pay.setter
    def Pay(self, NewPay):
        self.__Pay = NewPay

    def Print(self):
        Text = " HotelRoom number" + str(self.ID) + " Can support only " + str(self.MaxNumber) + " persons, have comfort Star "+ str(self.Comfort) + " and cost only "+str(self.Pay)
        print(Text)


