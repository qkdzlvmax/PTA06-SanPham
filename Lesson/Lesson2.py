class Sach:
    def __init__(self, _n = "Chua biet", _tg = "Chua biet", _nxb = "Chua biet", _ttm = "Chua biet"):
        self.name = _n
        self.tacgia = _tg
        self.namxuatban = _nxb
        self.trangthaimuon = _ttm
    #Ham de show ra thong tin cua lop
    def show(self):
        #Ham duoc dung san de in ra tat ca thuoc tinh co trong class
        print(self.__dict__)
#Truong hop chua truyen tham so vao
sach1 = Sach()
sach1.show()
#Truong hop truyen tham so vao
sach2 = Sach("Hiromiya")
sach2.show()
sach3 = Sach("Hiromiya", "Hagiwara Daisuke")
sach3.show()
sach4 = Sach("Hiromiya", "Hagiwara Daisuke", 2011)
sach4.show()
sach5 = Sach("Hiromiya", "Hagiwara Daisuke", 2011, "Da muon")
sach5.show

