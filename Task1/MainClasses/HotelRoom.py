class UHotelRoom:
    def __init__(self, MaxNumber=1, Comfort=1, Pay=1000, ID=0):
        self.MaxNumber = int(MaxNumber)
        self.Comfort = int(Comfort)
        self.Pay = int(Pay)
        self.ID = int(ID)

    def Print(self):
        Text = " HotelRoom number" + str(self.ID) + " Can support only " + str(self.MaxNumber) + " persons, have comfort Star "+ str(self.Comfort) + " and cost only "+str(self.Pay)
        print(Text)


