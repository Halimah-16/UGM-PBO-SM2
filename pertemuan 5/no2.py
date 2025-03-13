class AlatMusik:
    def suara(self):
        return "Alat musik ini menghasilkan suara."

class Gitar(AlatMusik):
    def suara(self):
        return "Gitar berbunyi: 'mak jreng!'"

class Piano(AlatMusik):
    def suara(self):
        return "Piano berbunyi: 'Ting ting!'"

class Drum(AlatMusik):
    def suara(self):
        return "Drum berbunyi: 'Dum dum ctak!'"

alat_musik_list = [Gitar(), Piano(), Drum(), AlatMusik()]
for alat in alat_musik_list:
    print(alat.suara())
