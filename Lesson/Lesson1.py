class Person:
    #Ham khoi tao -> khi tao ra mot doi tuong moi
    def __init__(self, _cP, _aP, fn, nn, bd, rl, ed):
        self.coverPicture = _cP
        self.avatarPicture = _aP
        self.fullname = fn
        self.nickname = nn
        self.birthdate = bd
        self.relationship = rl
        self.education = ed
    #Ham in ra thong tin cua nguoi do
    def show(self):
        print(self.__dict__)
    #Ham luu thong tin cua file
    def saveDataToFile(self):
        #Mo file duoi dang viet
        with open("person.txt", "w") as file:
            data = ""
            data += self.coverPicture + ","
            data += self.avatarPicture + ","
            data += self.fullname + ","
            data += self.nickname + ","
            data += self.birthdate + ","
            data += self.relationship + ","
            data += self.education 
            #Ghi vao file
            file.write(data)
    #Ham doc thong tin tu file
    def loadDataFromFile(self):
        #Mo file duoi dang doc
        with open("person.txt", 'r') as file:
            #Doc tat ca cac dong (readline ko co chu s = doc 1 dong / co chu s = doc tat ca dong)
            data = file.readline()
            #Chia du lieu vao tung thuoc tinh
            self.coverPicture, self.avatarPicture, self.fullname, self.nickname, self.birthdate, self.relationship, self.education = data.strip().split(",")

ps1 = Person("null", "null", "Dinh Quang Khoi", "Bo", "07/06/2010", "Unknown", "THCS LTT")
ps1.show()
# ps1.saveDataToFile()
ps1.loadDataFromFile()