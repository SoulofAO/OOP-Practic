
def ParseString(String, Determine):
    StringArray = []
    LocalString=""
    for x in String:
        if x == Determine:
            StringArray.append(LocalString)
            LocalString = ""
        else:
            LocalString = LocalString+x
    if(LocalString!=""):
        StringArray.append(LocalString)
    return StringArray

def GetVarName(String, WithPrivate):
    String = ParseString(String, ".")[1]
    String = ParseString(String, " ")[0]
    if(WithPrivate):
        return String
    else:
        LastIndex= len(ParseString(String, "_"))-1
        String = ParseString(String,"_")[LastIndex]
        return String


sentinel = '' # ends when this string is seen
InputStrings = []
for line in iter(input, sentinel):
    InputStrings.append(line)
for String in InputStrings:
    print("@property")
    VariableName = GetVarName(String, False)
    print("def "+VariableName+"(self):")
    print("\t"+"return "+"self.__"+VariableName)
    print("@"+VariableName+".setter")
    print("def "+VariableName+"(self,"+"New"+VariableName+"):")
    print("\t"+"self.__"+VariableName+"="+"New"+VariableName)
    print()



