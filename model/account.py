class Account:
    #Ham khoi tao -> khi tao ra mot doi tuong moi
    def __init__(self, _un = "taikhoan", _pw = "123"):
        self.username = _un
        self.password = _pw
        self.loadDataFromFile()
    #Ham in ra thong tin cua nguoi do
    def show(self):
        print(self.__dict__)
    #Ham luu thong tin cua file
    def saveDataToFile(self):
        #Mo file duoi dang viet
        with open("Data/account.txt", "w") as file:
            data = ""
            data += self.username + ","
            data += self.password
            #Ghi vao file
            file.write(data)
    #Ham doc thong tin tu file
    def loadDataFromFile(self):
        #Mo file duoi dang doc
        with open("Data/account.txt", "r") as file:
            #Doc tat ca cac dong (readline ko co chu s = doc 1 dong / co chu s = doc tat ca dong)
            data = str(file.readline())
            #Chia du lieu vao tung thuoc tinh
            self.username, self.password = data.split(",")
    #Ham doi mat khau
    def changePassword(self, newPassword):
        self.password = newPassword
        self.saveDataToFile()
    #Ham kiem tra dang nhap
    def checkAccount(self, _un, _pw):
        if _un == self.username and _pw == self.password:
            return True
        else:
            return False