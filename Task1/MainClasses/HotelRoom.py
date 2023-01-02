class UHotelRoom:
    def __init__(self, MaxNumber=1, Comfort=1, Pay=1000, ID=0):
        self.__MaxNumber = int(MaxNumber)
        self.__Comfort = int(Comfort)
        self.__Pay = int(Pay)
        self.__ID = int(ID)

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

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, NewID):
        self.__ID = NewID

    def Print(self):
        Text = " HotelRoom number" + str(self.ID) + " Can support only " + str(self.MaxNumber) + " persons, have comfort Star "+ str(self.Comfort) + " and cost only "+str(self.Pay)
        print(Text)


