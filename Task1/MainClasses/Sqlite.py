import sqlite3
from xml.etree.ElementTree import Element, SubElement, tostring
from Subsistems.ResiterSubsistem import NameSubsistem
class UHotelDataBase:
    def __init__(self):
        self.__Connect = sqlite3.connect('DataBaseHotel.db')
        self.__Cursor = self.Connect.cursor()
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Clients(
        Name TEXT, 
        Family TEXT,
        Second_Name TEXT,
        Passport TEXT,
        Comment TEXT,
        ID TEXT);
        """)

        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS HotelRooms(
        MaxNumber TEXT, 
        Comfort TEXT,
        Pay TEXT,
        ID TEXT);
        """)

        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Bookings(
         DateOn TEXT, 
         DateOff TEXT,
         Passport TEXT,
         HotelRoomID TEXT,
         ClientID TEXT);
         """)

    @property
    def Connect(self):
        return self.__Connect

    @Connect.setter
    def Connect(self, NewConnect):
        self.__Connect = NewConnect

    @property
    def Cursor(self):
        return self.__Cursor

    @Cursor.setter
    def Cursor(self, NewCursor):
        self.__Cursor = NewCursor

    def SaveAll(self, Hotel):
        self.Cursor.execute('DELETE FROM Clients;',)
        self.Cursor.execute('DELETE FROM HotelRooms;', )
        self.Cursor.execute('DELETE FROM Bookings;', )

        for Client in Hotel.Clients:
            LocalClient = (Client.Name, Client.Family, Client.Second_Name, Client.passport, Client.Comment, Client.ID)
            self.Cursor.execute("INSERT INTO Clients VALUES(?, ?, ?, ?, ?, ?);",  LocalClient)
        for Room in Hotel.HotelRooms:
            LocalHotel = (Room.MaxNumber, Room.Comfort, Room.Pay, Room.ID)
            self.Cursor.execute("INSERT INTO HotelRooms VALUES(?, ?, ?, ?);", LocalHotel)
        for Booking in Hotel.Bookings:
            Passport = Booking.Client.passport
            ID = Booking.HotelRoom.ID
            ClientID = NameSubsistem.GetIDByReference(Booking.Client)
            HotelRoomID = NameSubsistem.GetIDByReference(Booking.HotelRoom)
            LocalBooking=(Booking.DateOn, Booking.DateOff, Passport, ClientID, HotelRoomID)
            self.Cursor.execute("INSERT INTO Bookings VALUES(?, ?, ?, ?, ?);", LocalBooking)
    def LoadAll(self):
        root = Element('Hotel')
        self.Cursor.execute("SELECT * FROM Clients;")
        Clients = self.Cursor.fetchall()
        for Client in Clients:
            child = SubElement(root, "Client")
            child.set("Name", Client[0])
            child.set("Family", Client[1])
            child.set("Second_Name", Client[2])
            child.set("Passport", Client[3])
            child.set("Comment", Client[4])
            child.set("ID", Client[5])
        self.Cursor.execute("SELECT * FROM Bookings;")
        Bookings = self.Cursor.fetchall()
        for Booking in Bookings:
            child = SubElement(root, "Booking")
            child.set("DateOn", Booking[0])
            child.set("DateOff", Booking[1])
            child.set("Passport", Booking[2])
            child.set("HotelRoomID", Booking[3])
            child.set("ClientID", Booking[4])
        self.Cursor.execute("SELECT * FROM HotelRooms;")
        HotelRooms = self.Cursor.fetchall()
        for HotelRoom in HotelRooms:
            child = SubElement(root, "HotelRoom")
            child.set("MaxNumber",HotelRoom[0])
            child.set("Comfort", HotelRoom[1])
            child.set("Pay", HotelRoom[2])
            child.set("ID", HotelRoom[3])

        file = open('Hotel.xml', 'w')
        Answer = str(tostring(root))[2:]
        Answer = Answer[:(len(Answer)-1)]
        print(Answer)

        file.write(Answer)
        file.close()





DataBase = UHotelDataBase()