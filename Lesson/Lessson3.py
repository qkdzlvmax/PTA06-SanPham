#Lop cha - super class
class Animal:
    #Ham khoi tao
    def __init__(self, _n = "Chua biet", _a = 0):
        self.name = _n
        self.age = _a
    #Ham in ra thong tin
    def show(self):
        print(self.__dict__)
    #Ham tao tieng keu cua dong vat
    def make_sound(self):
        print("Chua biet minh la dong vat gi, chua the keu duoc")
#Lop con
class Dog(Animal):
    #Da co ham Init, khong can lam lai
    def __init__(self, _n = "Chua biet", _a = 0):
        super().__init__(_n, _a)
    #Overwrite ham make sound
    def make_sound(self):
        print("Gau gau gau")
    def gam_xuong(self):
        print("Mam mam mam")

class Bird(Animal):
    def make_sound(self):
        print("Chip chip chip")
    def fly(self):
        print("Xoat xoat xoat")

class Snake(Animal):
    def make_sound(self):
        print("Sss")
    def uong_ang(self):
        print("Xoat xoat xoat")

class Fish(Animal):
    def make_sound(self):
        print("Ot ot ot")
    def swim(self):
        print("Ot ot ot")

list_animals = [
    Dog("Kiki", 3),
    Bird("Mimi", 2),
    Snake("LB", 1),
    Fish("RB", 5)
]
#Show ra cac dong vat hien co trong so thu
print("Xin chao den voi so thu 3 Anh Em")
print("=================================")
print(f"Bay gio trong so thu hien dang co {len(list_animals)} loai dong vat")
print("=================================")
for animal in list_animals:
    print(f"Xin chao, to ten la {animal.name}, tieng keu cua to la")
    animal.make_sound()
print("=================================")

