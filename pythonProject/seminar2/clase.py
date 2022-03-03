class Entitate(object): #clasa mostenteste din object
    # __init__ este echivalentul unui constructor
    def __init__(self, id, nume): #parametri
        self.id = id #this.nume=valoare
        self.nume = nume

    def display(self):  #echivalentul lui this
        print(self.id, self.nume)

class Tara(Entitate):
    def __init__(self, id, nume, populatie, pib):
        super().__init__(id, nume)
        self.populatie = populatie
        self.pib = pib

    def display(self):
        print(self.id, self.nume, self.populatie, self.pib)

    def __str__(self):  #pt string-uri
        #return self.id + " " + self.nume
        return "{0} {1} {2} {3}".format(self.id, self.nume, self.populatie, self.pib)

    def __lt__(self, other):  #cand comparam obiecte
        return self.pib < other.pib



