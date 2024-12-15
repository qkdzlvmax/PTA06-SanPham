from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox # Them widgets vao
from PyQt6 import uic # Doc giao dien UI
import sys # He thong may tinh
import webbrowser
from model.account import Account

class LoginPage(QMainWindow):
    # Ham khoi tao
    def __init__(self):
        super().__init__()
        # Doc giao dien tu file UI
        uic.loadUi("UI-GiaoDien/login.ui", self)
        # Ket noi su kien khi nhan vao nut dang nhap
        self.btnLogin.clicked.connect(self.checkLogin)

    def checkLogin(self):
        acc = Account()
        check = acc.checkAccount(self.txtUsername.text(), self.txtPassword.text)
        if check == True:
            self.close()
            ip.show()
        else:
            htb = QMessageBox()
            htb.setWindowTile("Loi dang nhap")
            htb.setIcon(QMessageBox.Icon.Warning)
            htb.setText("Sai thong tin tk hoac mk !! \n Vui long kiem tra lai")
            htb.setStyleSheet("background-color: yellow; color:black;")
            sys.exit(htb.exec())

class IphonePage(QMainWindow):
    # Ham khoi tao
    def __init__(self):
        super().__init__()
        # Doc giao dien tu file UI
        uic.loadUi("UI-GiaoDien/Iphone.ui", self)        

class HomePage(QMainWindow):
    # Ham khoi tao
    def __init__(self):
        super().__init__()
        # Doc giao dien tu file UI
        uic.loadUi("UI-GiaoDien/home.ui", self)
        # Ket noi su kien cua nut
        # chuyen trang
        self.btnPlayCW.clicked.connect(lambda:self.changePage(1))
        self.btnPlayOLS.clicked.connect(lambda:self.changePage(2))
        self.btnPlayH.clicked.connect(lambda:self.changePage(3))
        # self.btnProfile.clicked.connect(self.showProfile)
        # phat phim
        self.btnWatchCW.clicked.connect(lambda:self.playMovie("https://www.netflix.com/vn/title/81609374"))
        self.btnWatchOLS.clicked.connect(lambda:self.playMovie("https://www.netflix.com/vn/title/81498404"))
        self.btnWatchH.clicked.connect(lambda:self.playMovie("https://www.netflix.com/vn/title/81256675"))
    def changePage(self,id):
        self.stackedWidget.setCurrentIndex(id)
    def playMovie(self,linkMovie):
        webbrowser.open(linkMovie)
    # def showProfile(self):
    #     profile.show()

class ProfilePage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Profile.ui", self)
        self.loadInfor()
        self.btnFaceBook.clicked.connect(self.openlinkFB)
        self.btnSave.clicked.connect(self.saveInfor)
    def saveInfor(self):
        a = self.txtEmail.text()
        b = self.txtPhone.text()
        c = self.txtAddress.text()
        d = self.txtEducation.text()
        e = self.txtFavSong.text()
        f = self.txtFavArtist.text()
        g = self.txtFavKind.text()
        print(a, b, c, d, e, f, g)
    def openlinkFB(self):
        webbrowser.open("https://www.facebook.com/")
    def loadInfor(self):
        self.txtFullName.setText("Name")
        self.txtNickName.setText("Name")
        self.txtEmail.setText("Name")
        self.txtPhone.setText("Name")
        self.txtAddress.setText("Name")
        self.txtEducation.setText("Name")
        self.txtBirthDate.setText("Name")
        self.txtFavSong.setText("Name")
        self.txtFavArtist.setText("Name")
        self.txtFavKind.setText("Name")

if __name__ == "__main__":
    #Tao ra 1 app
    app = QApplication(sys.argv)
    lg = LoginPage()
    ip = IphonePage()
    hp = HomePage()
    # profile = ProfilePage()
    hp.show()
    app.exec()
