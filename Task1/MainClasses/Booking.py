from Root.Object import UObject
class UBooking(UObject):
    def __init__(self, ID = -1, Outer = None, Client = None, HotelRoom = None, DateOn="0.0.0", DateOff="0.0.0", Comment="None"):
        UObject.__init__(self,ID,Outer)
        self.__Client = Client
        self.__HotelRoom = HotelRoom
        self.__DateOn = DateOn
        self.__DateOff = DateOff
        self.__Comment = Comment

    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, NewClient):
        self.__Client = NewClient

    @property
    def HotelRoom(self):
        return self.__HotelRoom

    @HotelRoom.setter
    def HotelRoom(self, NewHotelRoom):
        self.__HotelRoom = NewHotelRoom

    @property
    def DateOn(self):
        return self.__DateOn

    @DateOn.setter
    def DateOn(self, NewDateOn):
        self.__DateOn = NewDateOn

    @property
    def DateOff(self):
        return self.__DateOff

    @DateOff.setter
    def DateOff(self, NewDateOff):
        self.__DateOff = NewDateOff

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, NewComment):
        self.__Comment = NewComment

    def Print(self):
        print("This room ID"  + " Take By " + str(self.Client.Name) + " from " + self.DateOn+" to " + self.DateOff)