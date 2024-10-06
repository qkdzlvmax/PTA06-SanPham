import webbrowser
class Music:
    def __init__(self, _l, _n, _a, _s, _d):
        self.link = _l
        self.name = _n
        self.artist = _a
        self.stream = _s
        self.duration = _d
    #Ham de mo bai hat
    def open(self):
        webbrowser.open(self.link)
listmusics = []
#Lay link youtube
ms1 = Music("https://www.youtube.com/watch?v=KyAcMpQUY5s&pp=ygUEaG9wZQ%3D%3D", "HOPE", "XXXTENTACION", "440 Mil", "1:51")
ms1.open()
listmusics.append(ms1)
#Lay link spotify
ms2 = Music("https://open.spotify.com/track/285pBltuF7vW8TeWk8hdRR?si=b4c067bd3ff846bb", "Lucid Dreams", "Juice WRLD", "2.6 BIL", "3:59")
ms2.open()
listmusics.append(ms2)

listmusics[1].open()
