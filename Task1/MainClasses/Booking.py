class UBooking:
    def __init__(self, Client, HotelRoom, DateOn="0.0.0", DateOff="0.0.0", Comment="None"):
        self.Client = Client
        self.HotelRoom = HotelRoom
        self.DateOn = DateOn
        self.DateOff = DateOff
        self.Comment = Comment

    def Print(self):
        print("This room ID" + str(self.HotelRoom.ID) + " Take By " + str(self.Client.Name) + " from " + self.DateOn+" to " + self.DateOff)