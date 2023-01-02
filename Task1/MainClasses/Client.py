class UClient():
    def __init__(self, Family="Noname", Name="Nona", Second_Name="Nonameovich", passport=6458203940, Comment="None"):
        self.__Name = Name
        self.__Family = Family
        self.__Second_Name = Second_Name
        self.__passport = int(passport)
        self.__Comment = Comment

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, NewName):
        self.__Name = NewName

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, NewFamily):
        self.__Family = NewFamily

    @property
    def Second_Name(self):
        return self.__Second_Name

    @Name.setter
    def Second_Name(self, NewSecond_Name):
        self.__Second_Name = NewSecond_Name

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, Newpassport):
        self.__passport = Newpassport

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, NewComment):
        self.__Comment = NewComment

    def Print(self):
        print("Client " + self.Name + " " + self.Family + " " + self.Second_Name + " with passport " + str(self.passport))