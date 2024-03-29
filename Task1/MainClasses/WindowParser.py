import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import urllib.request
from MainClasses.Client import UClient
from MainClasses.HotelRoom import UHotelRoom
from MainClasses.Booking import UBooking
from Subsistems.ResiterSubsistem import NameSubsistem

class UWindowParser:
    def __init__(self, Url):
        self.__Url = Url
        try:
            self.__doc = minidom.parse(Url)
            self.__xmlHotel = self.doc.getElementsByTagName("Hotel")[0]
        except:
            pass

    @property
    def Url(self):
        return self.__Url

    @Url.setter
    def Url(self, NewUrl):
        self.__Url = NewUrl

    @property
    def doc(self):
        return self.__doc

    @doc.setter
    def doc(self, Newdoc):
        self.__doc = Newdoc

    @property
    def xmlHotel(self):
        return self.__xmlHotel

    @xmlHotel.setter
    def xmlHotel(self, NewxmlHotel):
        self.__xmlHotel = NewxmlHotel

    def GetAsString(self):
        tree = ET.parse(self.Url)
        root = tree.getroot()
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        return xmlstr

    def SetFromString(self, string):
        with open("Hotel", "w") as f:
            f.write(string)
        self.doc = minidom.parse()
        self.xmlHotel = self.doc.getElementsByTagName("Hotel")[0]


    def ApplyParser(self, Hotel):
            Clients = self.xmlHotel.getElementsByTagName("Client")

            for Client in Clients:
                Name = Client.getAttribute("Name")
                Family = Client.getAttribute("Family")
                Second_Name = Client.getAttribute("Second_Name")
                passport = Client.getAttribute("Passport")
                Comment = Client.getAttribute("Comment")
                ID = Client.getAttribute("ID")
                Hotel.Clients.append(UClient(ID,Hotel,Name, Family, Second_Name, passport, Comment))
            HotelRooms = self.xmlHotel.getElementsByTagName("HotelRoom")

            for HotelRoom in HotelRooms:
                MaxNumber = HotelRoom.getAttribute("MaxNumber")
                Comfort = HotelRoom.getAttribute("Comfort")
                Pay = HotelRoom.getAttribute("Pay")
                ID = HotelRoom.getAttribute("ID")
                Hotel.HotelRooms.append(UHotelRoom(ID,Hotel,MaxNumber, Comfort, Pay))
            Bookings = self.xmlHotel.getElementsByTagName("Booking")

            for Booking in Bookings:
                DateOn = Booking.getAttribute("DateOn")
                DateOff = Booking.getAttribute("DateOff")
                Passport = int(Booking.getAttribute("Passport"))
                ClientID = int(Booking.getAttribute("ClientID"))
                Client = NameSubsistem.GetReferenceByID("UClient", ClientID)
                if Client == None:
                    continue
                HotelRoomID = int(Booking.getAttribute("HotelRoomID"))
                HotelRoom = NameSubsistem.GetReferenceByID("UHotelRoom", HotelRoomID)
                if HotelRoom is None:
                    continue
                Hotel.Bookings.append(UBooking(-1,Hotel,Client,HotelRoom,DateOn,DateOff))

            print("ParserEnd")

    def getElement(self, element):
        return self.getText(element.childNodes)

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc

