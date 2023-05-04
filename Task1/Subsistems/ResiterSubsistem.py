import weakref

class UNameSubsistem:
    def __init__(self):
        self.RegisterAllObjects = []

    class FRegisterClass:
        class FRegisterObject:
            def __init__(self,Reference,ID):
                self.Reference = Reference
                self.ID = int(ID)

        def __init__(self, ClassName = "Class", RegisterObjects = []):
            self.ClassName= ClassName
            self.RegisterObjects = RegisterObjects

    def RegisterNewObject(self, Caller = None, ID = -1):
        if(ID==-1):
            ClassName = Caller.__class__.__name__
            RegisterClass = None
            for LocalRegisterClass in self.RegisterAllObjects:
                if LocalRegisterClass.ClassName == ClassName:
                    RegisterClass = LocalRegisterClass
            if(not RegisterClass):
                RegisterClass = self.FRegisterClass(Caller.__class__.__name__,[])
                self.RegisterAllObjects.append(RegisterClass)
            if(RegisterClass):
                LastIndex = len(RegisterClass.RegisterObjects)-1
                if(LastIndex==-1):
                    RegisterClass.RegisterObjects.append(RegisterClass.FRegisterObject(Caller,0))
                else:
                    LastID = RegisterClass.RegisterObjects[LastIndex].ID
                    LastID = LastID + 1
                    RegisterClass.RegisterObjects.append(RegisterClass.FRegisterObject(Caller,LastID))
            return True
        else:
            ClassName = Caller.__class__.__name__
            RegisterClass = None
            for LocalRegisterClass in self.RegisterAllObjects:
                if LocalRegisterClass.ClassName == ClassName:
                    RegisterClass = LocalRegisterClass
                    for RegisterObject in LocalRegisterClass.RegisterObjects:
                        if(RegisterObject.ID == ID):
                            return False
                    break
            if(not RegisterClass):
                RegisterClass = self.FRegisterClass(Caller.__class__.__name__,[])
                self.RegisterAllObjects.append(RegisterClass)
            if(RegisterClass):
                RegisterClass.RegisterObjects.append(RegisterClass.FRegisterObject(Caller, ID))
            return True


    def GetReferenceByID(self,ClassName, ID):
        for LocalRegisterClass in self.RegisterAllObjects:
            if LocalRegisterClass.ClassName == ClassName:
                RegisterClass = LocalRegisterClass
                for RegisterObject in LocalRegisterClass.RegisterObjects:
                    if (RegisterObject.ID == ID):
                        return RegisterObject.Reference
        return None

    def GetReferencesByClass(self,ClassName):
        ReturnArray = []
        for LocalRegisterClass in self.RegisterAllObjects:
             if LocalRegisterClass.ClassName == ClassName:
                RegisterClass = LocalRegisterClass
                for RegisterObject in LocalRegisterClass.RegisterObjects:
                    ReturnArray.append(RegisterObject.Reference)
        return ReturnArray

    def GetIDByReference(self, Reference):
        ClassName = Reference.__class__.__name__
        for LocalRegisterClass in self.RegisterAllObjects:
            if LocalRegisterClass.ClassName == ClassName:
                RegisterClass = LocalRegisterClass
                for RegisterObject in LocalRegisterClass.RegisterObjects:
                    if (RegisterObject.Reference == Reference):
                          return RegisterObject.ID

    def GetAllReferenceByOuter(self,Outer, ClassSort = ""):
        ReferenceArray = []
        for RegisterClass in self.RegisterAllObjects:
            for RegisterObject in RegisterClass.RegisterObjects:
                if(Outer==RegisterObject.Reference.Outer):
                    ReferenceArray.append(RegisterObject.Reference.Outer)
    def RemoveObject(self,Reference):
        ClassName = Reference.__class__.__name__
        for LocalRegisterClass in self.RegisterAllObjects:
            if LocalRegisterClass.ClassName == ClassName:
                RegisterClass = LocalRegisterClass
                LocalRegisterClass.RegisterObjects.pop(Reference)
                for RegisterObject in LocalRegisterClass.RegisterObjects:
                    if (RegisterObject.Reference == Reference):
                          return RegisterObject.ID




NameSubsistem = UNameSubsistem()

