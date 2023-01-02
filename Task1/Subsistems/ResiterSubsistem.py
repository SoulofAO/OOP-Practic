class UNameSubsistem:
    def __init__(self):
        self.RegisterAllObjects = []

    class FRegisterClass:
        class FRegisterObject:
            def __init__(self,Reference,ID):
                self.Reference = Reference
                self.ID = ID

        def __init__(self, ClassName = "Class", RegisterObjects = []):
            self.ClassName= ClassName
            self.RegisterObjects = RegisterObjects

    def RegisterNewCaller(self, Caller = None, ID = -1):
        if(ID==-1):
            ClassName = type(Caller).__name__()
            RegisterClass = None
            for LocalRegisterClass in self.RegisterAllObjects:
                if LocalRegisterClass.ClassName == ClassName:
                    RegisterClass = LocalRegisterClass
            if(not RegisterClass):
                RegisterClass = self.FRegisterClass(type(Caller).__name__(),[])
                self.RegisterAllObjects.append(RegisterClass)
            if(RegisterClass):
                LastIndex = len(RegisterClass.RegisterObjects)
                LastID = RegisterClass.RegisterObjects[LastIndex].ID
                LastID = LastID + 1
                RegisterClass.RegisterObjects.append(RegisterClass.FRegisterObject(Caller.ref(),LastID))
            return True
        else:
            ClassName = type(Caller).__name__()
            RegisterClass = None
            for LocalRegisterClass in self.RegisterAllObjects:
                if LocalRegisterClass.ClassName == ClassName:
                    RegisterClass = LocalRegisterClass
                    for RegisterObject in LocalRegisterClass.RegisterObjects:
                        if(RegisterObject.ID == ID):
                            return False
                    break
            if(not RegisterClass):
                RegisterClass = self.FRegisterClass(type(Caller).__name__(),[])
                self.RegisterAllObjects.append(RegisterClass)
            if(RegisterClass):
                RegisterClass.RegisterObjects.append(RegisterClass.FRegisterObject(Caller.ref(), ID))


    def GetLinkByID(self,ClassName, ID):
        for RegisterClass in self.RegisterAllObjects:
            for LocalRegisterClass in self.RegisterAllObjects:
                if LocalRegisterClass.ClassName == ClassName:
                    RegisterClass = LocalRegisterClass
                    for RegisterObject in LocalRegisterClass.RegisterObjects:
                        if (RegisterObject.ID == ID):
                            return RegisterObject.Reference
        return None

NameSubsistem = UNameSubsistem()

