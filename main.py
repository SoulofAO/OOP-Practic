# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


class UHotelRoom:
    def __init__(self, MaxNumber=1, Comfort=1, Pay=1000, OwnerHotel=None):
        self.MaxNumber= MaxNumber
        self.Comfort = Comfort
        self.Pay = Pay
        self.MainHotel = OwnerHotel

class UClient():
    def __init__(self,  Family="Noname", Name="Nona", Second_Name="Nonameovich", Pasport=6458203940,Comment = "None"):
        self.Name=Name
        self.Family =Family
        self.Second_Name = Second_Name
        self.Pasport = Pasport
        self.Comment = Comment

class UDiscount():
    def __init__(self, Client):
        self.Client = Client
        self.Number = 1
    def CheckDiscount(self, Pay):
        if self.Number>1:
            return self.ApplyDiscount(Pay)
    def ApplyDiscount(self, Pay):
        return Pay*0.9

class UBooking:
    def __init__(self,Client,HotelRoom,DateOn= "0.0.0", DateOff="0.0.0",Comment="None"):
        self.Client =Client
        self.HotelRoom = HotelRoom
        self.DateOn = DateOn
        self.DateOff = DateOff
        self.Comment = Comment

class UHotel:
    def __init__(self, HotelRooms =[], Bookings = [], Discounts = []):
        self.HotelRooms = HotelRooms
        self.Bookings = Bookings
        self.Discounts = Discounts


    def TakeOffer(self, Client, MaxNumber, Comfort, Pay, DateOn, DateOff):
        GoodHotelRooms = []
        for HotelRoom in self.HotelRooms:
            Discount = self.FindDiscountByClient(Client)
            if (Discount):
                PayAfterDiscount = Discount.CheckDiscount(HotelRoom.Pay)
            else:
                PayAfterDiscount = HotelRoom.Pay

            if HotelRoom.MaxNumber>=MaxNumber and HotelRoom.Comfort>=Comfort and PayAfterDiscount<=Pay:
                HaveAnotherBooking = False
                for Booking in self.Bookings:
                    if(Booking.DateOn <= DateOn and Booking.DateOff>=DateOff):
                        HaveAnotherBooking = True
                        break
                    else:
                        pass

                if (HaveAnotherBooking == False):
                    GoodHotelRooms.append([HotelRoom,PayAfterDiscount])
        return GoodHotelRooms

    def FindDiscountByClient(self, Client):
        for Discount in self.Discounts:
            if(Discount.Client == Client):
                return Client
        return None

    def TakeRoom(self, Client, HotelRoom, DateOn,DateOff,Comment):
        NewRoom = UBooking(Client,HotelRoom,DateOn, DateOff,Comment)
        self.Bookings.append(NewRoom)
        Discount = self.FindDiscountByClient(Client)
        if(Discount ==None):
            NewDiscount = UDiscount(Client)
            self.Discounts.append(NewDiscount)
        else:
            Discount.Number = Discount.Number +1

def PrintOffer(GoodHotelRoomsResult):
    for GoodHotelRoom in GoodHotelRoomsResult:
        print("MaxNumber "+str(GoodHotelRoom[0].MaxNumber) + ", Comfort " + str(GoodHotelRoom[0].Comfort) +", Price "+str(GoodHotelRoom[0].Pay)+", PriceWithDiscount "+ str(GoodHotelRoom[1]))

MainHotel = UHotel(HotelRooms=[UHotelRoom(2,1,500),UHotelRoom(1,4,1000)])
def SimpleExample():
    BrejnevClient = UClient("Brejnev","Leonid", "Ivanovich",Comment="Medalist")
    HotelRoomOffer= MainHotel.TakeOffer(BrejnevClient,1,3,1000000,"0.0.2","0.0.5")
    PrintOffer(HotelRoomOffer)
    HotelChoise = HotelRoomOffer[random.randint(0,len(HotelRoomOffer)-1)]




if __name__ == '__main__':
    SimpleExample()



