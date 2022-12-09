import sqlite3
from xml.etree.ElementTree import Element, SubElement, tostring

class UHotelDataBase:
    def __init__(self):
        self.Connect = sqlite3.connect('DataBaseHotel.db')
        self.Cursor = self.Connect.cursor()
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Clients(
        Name TEXT, 
        Family TEXT,
        Second_Name TEXT,
        Passport TEXT,
        Comment TEXT);
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
         ID TEXT);
         """)

    def SaveAll(self, Hotel):
        self.Cursor.execute('DELETE FROM Clients;',)
        self.Cursor.execute('DELETE FROM HotelRooms;', )
        self.Cursor.execute('DELETE FROM Bookings;', )

        for Client in Hotel.Clients:
            LocalClient = (Client.Name, Client.Family, Client.Second_Name,Client.passport, Client.Comment)
            self.Cursor.execute("INSERT INTO Clients VALUES(?, ?, ?, ?, ?);",  LocalClient)
        for Room in Hotel.HotelRooms:
            LocalHotel = (Room.MaxNumber, Room.Comfort, Room.Pay, Room.ID)
            self.Cursor.execute("INSERT INTO HotelRooms VALUES(?, ?, ?, ?);", LocalHotel)
        for Booking in Hotel.Bookings:
            Passport = Booking.Client.passport
            ID = Booking.HotelRoom.ID
            LocalBooking=(Booking.DateOn, Booking.DateOff,Passport,ID)
            self.Cursor.execute("INSERT INTO Bookings VALUES(?, ?, ?, ?);", LocalBooking)
    def LoadAll(self):
        root = Element('Hotel')
        self.Cursor.execute("SELECT * FROM Clients;")
        Clients = self.Cursor.fetchall()
        for Client in Clients:
            print(Client[0])
            child = SubElement(root, "Client")
            child.attrib = {"Name": str(Client[0]), "Family": str(Client[1]), "Second_Name":str(Client[2]),"Passport":str(Client[3]),"Comment":str(Client[4])}
        file = open('Hotel.xml', 'w')
        print(tostring(root))

        file.write(str(tostring(root)))
        file.close()





DataBase = UHotelDataBase()