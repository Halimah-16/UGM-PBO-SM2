class Lagu:
    def genre(self):
        return "Genre lagu tidak diketahui"

class Pop(Lagu):
    def genre(self):
        return "Pop - Lagu dengan melodi ringan."

class Rock(Lagu):
    def genre(self):
        return "Rock - Lagu dengan irama kuat dan dominasi instrumen gitar."

class Jazz(Lagu):
    def genre(self):
        return "Jazz - Lagu dengan improvisasi dan harmoni yang kompleks."

# Contoh penggunaan
lagu_list = [Pop(), Rock(), Jazz(), Lagu()]
for lagu in lagu_list:
    print(lagu.genre())
