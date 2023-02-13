
from MainClasses.Client import UClient
from MainClasses.MainHotel import UHotel
import random
from MainClasses.Sqlite import DataBase

MainHotel = UHotel()

def PrintOffer(GoodHotelRoomsResult):
    for GoodHotelRoom in GoodHotelRoomsResult:
        print("MaxNumber " + str(GoodHotelRoom[0].MaxNumber) + ", Comfort " + str(
            GoodHotelRoom[0].Comfort) + ", Price " + str(GoodHotelRoom[0].Pay) + ", PriceWithDiscount " + str(
            GoodHotelRoom[1]))


def SimpleExample():
    BrejnevClient = UClient(-1,None,"Brejnev", "Leonid", "Ivanovich", Comment="Medalist")
    MainHotel.Clients.append(BrejnevClient)
    HotelRoomOffer = MainHotel.TakeOffer(BrejnevClient, 1, 3, 1000000, "0.0.2", "0.0.5")
    PrintOffer(HotelRoomOffer)
    if(len(HotelRoomOffer)>0):
        HotelChoise = HotelRoomOffer[random.randint(0, len(HotelRoomOffer) - 1)]
    print(BrejnevClient.Print())

def PrintAllInfo():
    MainHotel.PrintAllInfo()

def CheckDateBase():
    DataBase.SaveAll(MainHotel)
    DataBase.LoadAll()
def SaveAll():
    DataBase.SaveAll(MainHotel)