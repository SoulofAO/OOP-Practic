class UNameSubsistem:
    def __init__(self):
        self.IDs = []
        self.RegisterObjects = []

    def GetName(self, Caller):
        ID = 0
        Name = type(Caller).__name__()
        Find = False
        for LocalID in self.IDs:
            if LocalID.Class == Name:
                ID = LocalID.ID
                LocalID.ID = LocalID+1
                Find = True
                break
        if(not(Find)):
            self.IDs.append([Name,ID])
        RegisteredObject = [str(Caller)+"."+str(ID),Caller]
        self.RegisterObjects.append(RegisteredObject)
        return  RegisteredObject

    def GetLinkByName(self, Name):
        for RegisterObject in self.RegisterObjects:
            if(RegisterObject[0] == Name):
                return RegisterObject[1]
        return None

NameSubsistem = UNameSubsistem()

