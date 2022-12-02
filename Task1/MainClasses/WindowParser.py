import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import urllib.request
from MainClasses.Client import UClient
from MainClasses.HotelRoom import UHotelRoom
from MainClasses.Booking import UBooking

class UWindowParser:
    def __init__(self, Url):
        self.Url = Url
        self.doc = minidom.parse(Url)
        self.xmlHotel = self.doc.getElementsByTagName("Hotel")[0]

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
            Hotel.Clients.append(UClient(Name, Family, Second_Name, passport, Comment))
        HotelRooms = self.xmlHotel.getElementsByTagName("HotelRoom")

        for HotelRoom in HotelRooms:
            MaxNumber = HotelRoom.getAttribute("MaxNumber")
            Comfort = HotelRoom.getAttribute("Comfort")
            Pay = HotelRoom.getAttribute("Pay")
            ID = HotelRoom.getAttribute("ID")
            Hotel.HotelRooms.append(UHotelRoom(MaxNumber, Comfort, Pay, ID))
        Bookings = self.xmlHotel.getElementsByTagName("Booking")

        for Booking in Bookings:
            DateOn = Booking.getAttribute("DateOn")
            DateOff = Booking.getAttribute("DateOff")
            Passport = int(Booking.getAttribute("Passport"))

            Client = Hotel.GetClientByPassport(Passport)
            if Client == None:
                continue
            ID = int(Booking.getAttribute("ID"))
            HotelRoom = Hotel.GetRoomByID(ID)
            if HotelRoom is None:
                continue
            Hotel.Bookings.append(UBooking(Client,HotelRoom,DateOn,DateOff))

        print("ParserEnd")

    def getElement(self, element):
        return self.getText(element.childNodes)

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc

