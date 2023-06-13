import cherrypy
from Subsistems.ResiterSubsistem import NameSubsistem
from MainClasses.Client import UClient
from MainClasses.HotelRoom import UHotelRoom
from MainClasses.Booking import UBooking
class Page1:
    def index(self):
        s = """
            <html>
                <head>
                    <title>Page 1</title>
                </head>
                <body>
                    <p><a href="/clients"> Clients</a></p>
                    <p><a href="/bookings"> Bookings</a></p>
                    <p><a href="/hotel_rooms"> Rooms</a></p>
        """

        s=s+ """</body>
            </html>"""
        return s
    index.exposed = True

class Clients:
    def index(self):
        s = """
            <html>
                <head>
                    <title>Clients</title>
                </head>
                <body>
                    <h1>Clients</h1>
                    <p><a href="/">Go back</a></p>
                    <p><a href="/clients_add"> Add</a></p>
                    <p><a href="/clients_remove"> Remove</a></p>
                </body>
            </html>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>Name</th>
                <th>Family</th>
                <th>Second_Name</th>
                <th>Passport</th>
                <th>Comment</th>
                <th>ID</th>
                  </tr>"""
        ClientsArray = NameSubsistem.GetReferencesByClass("UClient")
        for Client in ClientsArray:
            s = s + """ <tr>"""
            s = s+"<th>"+ str(Client.Name)+"</th>"
            s = s + "<th>" + str(Client.Family) + "</th>"
            s = s + "<th>" + str(Client.Second_Name) + "</th>"
            s = s + "<th>" + str(Client.passport) + "</th>"
            s = s + "<th>" + str(Client.Comment) + "</th>"
            s = s + "<th>" + str(Client.ID) + "</th>"
            s = s + """ </tr>"""

        s = s + "</table>"
        return s
    index.exposed = True

class ClientsAdd:
    def index(self):
        s = """
            <html>
                <head>
                    <title>Clients</title>
                </head>
                <body>
                    <h1>Clients</h1>
                    <p><a href="/clients">Go back</a></p>
        """
        s = s + "<table>"
        s = s + '''
                 <tr>
                 <tr>
                 <form method="post" action="submit">
                 <th>
                 Name
                 </th>
                 <th>
                 <input type="Name" name="Name" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Family
                 </th>
                 <th>
                 <input type="Family" name="Family" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Second_Name
                 </th>
                 <th>
                 <input type="SecondName" name="SecondName" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Passport
                 </th>
                 <th>
                 <input type="Passport" name="Passport" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Comment
                 </th>
                 <th>
                 <input type="Comment" name="Comment" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 <input type="submit" value="Submit" />
                 </th>
                 </tr>'''
        s = s + """                </body>
            </html>"""
        return s

    index.exposed = True

    @cherrypy.expose
    def submit(self, Name, Family, SecondName, Passport, Comment):
        Client = UClient()
        Client.Name = Name
        Client.Family = Family
        Client.Second_Name = SecondName
        Client.passport = Passport
        Client.Comment = Comment
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Add Sucsess.</p>
                    <p><a href="/clients">Go back to clients</a></p>
                </body>
            </html>
        """
class ClientsRemove:
    def index(self):
        s = """
            <html>
                <head>
                    <title>ClientsRemove</title>
                </head>
                <body>
                    <h1>Clients</h1>
                    <p><a href="/clients">Go back</a></p>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>ID</th>
                  </tr>"""
        s = s + '''
                <tr>
                <form method="post" action="submit">
                <input type="ID" name="ID" />
                <input type="submit" value="Submit" />
                </tr>'''
        s = s + """</body>
            </html>"""
        return s

    @cherrypy.expose
    def submit(self, ID):
        NameSubsistem.DeleteObject(NameSubsistem.GetReferenceByID("UClient",int(ID)))
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Remove item.</p>
                    <p><a href="/clients">Go back to clients</a></p>
                </body>
            </html>
        """
    index.exposed = True
class Bookings:
    def index(self):
        s = """
            <html>
                <head>
                    <title>Bookings</title>
                </head>
                <body>
                    <h1>Bookings</h1>
                    <p><a href="/">Go back</a></p>
                    <p><a href="/bookings_add"> Add</a></p>
                    <p><a href="/bookings_remove"> Remove</a></p>
                </body>
            </html>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>Client</th>
                <th>HotelRoom</th>
                <th>DateOn</th>
                <th>DateOff</th>
                <th>Comment</th>
                <th>ID</th>
                  </tr>"""
        ClientsArray = NameSubsistem.GetReferencesByClass("UBooking")
        for Client in ClientsArray:
            s = s + """ <tr>"""
            try:
                s = s + "<th>" + str(Client.Client.ID) + "</th>"
            except:
                s = s + "<th>" + "None" + "</th>"
            try:
                s = s + "<th>" + str(Client.HotelRoom.ID) + "</th>"
            except:
                s = s + "<th>" + "None" + "</th>"
            s = s + "<th>" + str(Client.DateOn) + "</th>"
            s = s + "<th>" + str(Client.DateOff) + "</th>"
            s = s + "<th>" + str(Client.Comment) + "</th>"
            s = s + "<th>" + str(Client.ID) + "</th>"
            s = s + """ </tr>"""

        s = s + "</table>"
        return s

    index.exposed = True
class BookingsAdd:
    def index(self):
        s = """
            <html>
                <head>
                    <title>Bookings</title>
                </head>
                <body>
                    <h1>Bookings</h1>
                    <p><a href="/bookings">Go back</a></p>
        """
        s = s + '''
                "<table>"'''
        s = s + '''
                 <tr>
                 <tr>
                 <form method="post" action="submit">
                 <th>
                 Client ID
                 </th>
                 <th>
                 <input type="number" name="Client"/>
                 </th>
                 </tr>
                 <tr>
                 <th>
                 HotelRoom ID
                 </th>
                 <th>
                 <input type="number" name="HotelRoom"/>
                 </th>
                 </tr>
                 <tr>
                 <th>
                 DateOn
                 </th>
                 <th>
                 <input type="text" name="DateOn" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 DateOff
                 </th>
                 <th>
                 <input type="text" name="DateOff" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Comment
                 </th>
                 <th>
                 <input type="text" name="Comment" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 <input type="submit" value="Submit" />
                 </th>
                 </tr>'''
        s = s + """                </body>
            </html>"""
        return s

    index.exposed = True

    @cherrypy.expose
    def submit(self, Client, HotelRoom, DateOn, DateOff, Comment):
        Booking = UBooking()
        Booking.Client = NameSubsistem.GetReferenceByID("UClient",int(Client))
        Booking.HotelRoom = NameSubsistem.GetReferenceByID("UHotelRoom",int(HotelRoom))
        Booking.DateOn = DateOn
        Booking.DateOff = DateOff
        Booking.Comment = Comment
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Add Sucsess.</p>
                    <p><a href="/bookings">Go back to bookings</a></p>
                </body>
            </html>
        """
class BookingsRemove:
    def index(self):
        s = """
            <html>
                <head>
                    <title>BookingsRemove</title>
                </head>
                <body>
                    <h1>Bookings</h1>
                    <p><a href="/bookings">Go back</a></p>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>ID</th>
                  </tr>"""
        s = s + '''
                <tr>
                <form method="post" action="submit">
                <input type="ID" name="ID" />
                <input type="submit" value="Submit" />
                </tr>'''
        s = s + """</body>
            </html>"""
        return s

    @cherrypy.expose
    def submit(self, ID):
        NameSubsistem.DeleteObject(NameSubsistem.GetReferenceByID("UBooking",int(ID)))
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Remove item.</p>
                    <p><a href="/bookings">Go back to bookings</a></p>
                </body>
            </html>
        """
    index.exposed = True



class HotelRooms:
    def index(self):
        s = """
            <html>
                <head>
                    <title>HotelRooms</title>
                </head>
                <body>
                    <h1>HotelRooms</h1>
                    <p><a href="/">Go back</a></p>
                    <p><a href="/hotel_rooms_add"> Add</a></p>
                    <p><a href="/hotel_rooms_remove"> Remove</a></p>
                </body>
            </html>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>MaxNumber</th>
                <th>Comfort</th>
                <th>Pay</th>
                <th>ID</th>
                """
        ClientsArray = NameSubsistem.GetReferencesByClass("UHotelRoom")
        for Client in ClientsArray:
            s = s + """ <tr>"""
            s = s+"<th>"+ str(Client.MaxNumber)+"</th>"
            s = s + "<th>" + str(Client.Comfort) + "</th>"
            s = s + "<th>" + str(Client.Pay) + "</th>"
            s = s + "<th>" + str(Client.ID) + "</th>"
            s = s + """ </tr>"""
        s = s + "</table>"
        s = s + """</body>
            </html>"""
        return s
    index.exposed = True

class HotelAdd:
    def index(self):
        s = """
            <html>
                <head>
                    <title>HotelRooms</title>
                </head>
                <body>
                    <h1>HotelRooms</h1>
                    <p><a href="/hotel_rooms">Go back</a></p>
        """
        s = s + "<table>"
        s = s + '''
                 <tr>
                 <tr>
                 <form method="post" action="submit">
                 <th>
                 MaxNumber
                 </th>
                 <th>
                 <input type="number" name="MaxNumber" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Comfort
                 </th>
                 <th>
                 <input type="number" name="Comfort" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 Pay
                 </th>
                 <th>
                 <input type="number" name="Pay" />
                 </th>
                 </tr>
                 <tr>
                 <th>
                 <input type="submit" value="Submit" />
                 </th>
                 </tr>'''
        s = s + """                </body>
            </html>"""
        return s

    index.exposed = True
    @cherrypy.expose
    def submit(self, MaxNumber,Comfort, Pay,):
        HotelRoom = UHotelRoom()
        HotelRoom.MaxNumber = int(MaxNumber)
        HotelRoom.Pay = int(Pay)
        HotelRoom.Comfort = int(Comfort)
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Add Sucsess.</p>
                    <p><a href="/hotel_rooms">Go back to rooms</a></p>
                </body>
            </html>
        """
class HotelRemove:
    def index(self):
        s = """
            <html>
                <head>
                    <title>HotelRooms</title>
                </head>
                <body>
                    <h1>HotelRooms</h1>
                    <p><a href="/hotel_rooms">Go back</a></p>
        """
        s = s + "<table>"
        s = s + """ <tr>
                <th>ID</th>
                  </tr>"""
        s = s + '''
                <tr>
                <form method="post" action="submit">
                <input type="ID" name="ID" />
                <input type="submit" value="Submit" />
                </tr>'''
        s = s + """</body>
            </html>"""
        return s

    @cherrypy.expose
    def submit(self, ID):
        NameSubsistem.DeleteObject(NameSubsistem.GetReferenceByID("UHotelRoom",int(ID)))
        return """
            <html>
                <head>
                    <title>Congratulation</title>
                </head>
                <body>
                    <p>Remove item.</p>
                    <p><a href="/hotel_rooms">Go back to hotel_rooms</a></p>
                </body>
            </html>
        """
    index.exposed = True
def CherryExecute():
    root = Page1()
    LClient = Clients()
    ClientAdd = ClientsAdd()
    root.clients = LClient
    root.clients_add = ClientAdd
    root.clients_remove = ClientsRemove()
    root.bookings = Bookings()
    root.bookings_add = BookingsAdd()
    root.bookings_remove = BookingsRemove()
    root.bookings = Bookings()
    root.hotel_rooms = HotelRooms()
    root.hotel_rooms_add = HotelAdd()
    root.hotel_rooms_remove = HotelRemove()
    cherrypy.quickstart(root)