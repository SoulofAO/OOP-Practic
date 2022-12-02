class UClient():
    def __init__(self, Family="Noname", Name="Nona", Second_Name="Nonameovich", passport=6458203940, Comment="None"):
        self.Name = Name
        self.Family = Family
        self.Second_Name = Second_Name
        self.passport = int(passport)
        self.Comment = Comment

    def Print(self):
        print("Client " + self.Name + " " + self.Family + " " + self.Second_Name + " with passport " + str(self.passport))