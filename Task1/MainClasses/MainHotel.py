from MainClasses.WindowParser import UWindowParser
from MainClasses.Booking import UBooking
from MainClasses.Discount import UDiscount


class UHotel:
    def __init__(self, HotelRooms=[], Bookings=[], Discounts=[], Clients=[]):
        self.HotelRooms = HotelRooms
        self.Bookings = Bookings
        self.Discounts = Discounts
        self.Clients = Clients
        self.Parser = UWindowParser("Hotel.xml")
        self.Parser.ApplyParser(self)

    def TakeOffer(self, Client, MaxNumber, Comfort, Pay, DateOn, DateOff):
        GoodHotelRooms = []
        for HotelRoom in self.HotelRooms:
            Discount = self.FindDiscountByClient(Client)
            if (Discount):
                PayAfterDiscount = Discount.CheckDiscount(HotelRoom.Pay)
            else:
                PayAfterDiscount = HotelRoom.Pay

            if HotelRoom.MaxNumber >= MaxNumber and HotelRoom.Comfort >= Comfort and PayAfterDiscount <= Pay:
                HaveAnotherBooking = False
                for Booking in self.Bookings:
                    if (Booking.DateOn <= DateOn and Booking.DateOff >= DateOff):
                        HaveAnotherBooking = True
                        break
                    else:
                        pass

                if (HaveAnotherBooking == False):
                    GoodHotelRooms.append([HotelRoom, PayAfterDiscount])
        return GoodHotelRooms

    def FindDiscountByClient(self, Client):
        for Discount in self.Discounts:
            if (Discount.Client == Client):
                return Client
        return None

    def TakeRoom(self, Client, HotelRoom, DateOn, DateOff, Comment):
        NewRoom = UBooking(Client, HotelRoom, DateOn, DateOff, Comment)
        self.Bookings.append(NewRoom)
        Discount = self.FindDiscountByClient(Client)
        if (Discount == None):
            NewDiscount = UDiscount(Client)
            self.Discounts.append(NewDiscount)
        else:
            Discount.Number = Discount.Number + 1

    def GetClientByPassport(self, passport):
        for Client in self.Clients:
            if Client.passport == passport:
                return Client
        return None

    def GetRoomByID(self, ID):
        for HotelRoom in self.HotelRooms:
            if HotelRoom.ID == ID:
                return HotelRoom
        return None
    def PrintAllInfo(self):
        for Hotel in self.HotelRooms:
            Hotel.Print()
        for Booking in self.Bookings:
            Booking.Print()
        for Client in self.Clients:
            Client.Print()

