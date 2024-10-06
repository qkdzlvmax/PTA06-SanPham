import webbrowser
class Game:
    def __init__(self, _l, _n, _c, _i, _s, _t, _nph):
        self.link = _l
        self.name = _n
        self.creator = _c
        self.install = _i
        self.style = _s
        self.trailer = _t
        self.nhaphathanh = _nph
    def open(self):
        webbrowser.open(self.link)
    def openlinktrailer(self):
        webbrowser.open(self.trailer)
    def openlinknph(self):
        webbrowser.open(self.nhaphathanh)

g1 = Game("https://www.leagueoflegends.com/vi-vn/", "Lien Minh Huyen Thoai", "Jeff Jew", "50 Mil", "PvP", "https://www.youtube.com/watch?v=P3UhR7-hDpA&pp=ygUodHJhaWxlciBnYW1lIGxpw6puIG1pbmggaHV54buBbiB0aG_huqFpIA%3D%3D", "https://www.garena.vn/")
g1.openlinknph()
g2 = Game("https://playvalorant.com/vi-vn/", "Valorant", "Anna Donlon John Goscicki", "30 Mil", "Pvp", "https://www.youtube.com/watch?v=IhhjcB2ZjIM&pp=ygUWdHJhaWxlciBnYW1lIHZhbG9yYW50XA%3D%3D", "https://www.riotgames.com/vi")
g2.openlinknph()
