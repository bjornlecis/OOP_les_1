class Persoon:

    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def print_info(self):
        print(self.naam+" "+str(self.leeftijd))

    def toon_info(self):
        return self.naam+" "+str(self.leeftijd)

    def set_leeftijd(self,leeftijd):
        if(leeftijd > 17 and leeftijd < 121):
            self.leeftijd = leeftijd
        else:
            print("leeftijd te jong of oud")

    def set_naam(self,naam):
        if naam.isalpha():
            self.naam = naam
        else:
            print("Enkel letters")
#einde klasse persoon
#---------------------------------------------------------------------------------
#hoofdprogramma

#functie dat de lijst afdrukt
def toon_lijst(lijst):
    for x in personen:
        print(x.toon_info())
    print("-------------------------------------")

#een persoon toevoegen aan de lijst
def voeg_persoon_toe(lijst):
    naam = input("geef naam")
    leeftijd = input("geef leeftijd")
    lijst.append(Persoon(naam,leeftijd))

#zien of de naam in de lijst voorkomt
def naam_in_lijst(lijst):
    zoeknaam = input("geef je naam in")
    for x in lijst:
        if(zoeknaam == x.naam):
            print("naam in de lijst")

#verander naam in lijst
def verander_naam_in_lijst(lijst):
    zoeknaam = input("geef je naam in")
    for x in lijst:
        if(zoeknaam == x.naam):
            nieuwe_naam = input("Geef een nieuwe naam")
            x.naam = nieuwe_naam
#verander leeftijd
def verander_leeftijd_in_lijst(lijst):
    zoeknaam = input("geef je naam in")
    for x in lijst:
        if(zoeknaam == x.naam):
            nieuwe_leeftijd = input("Geef een nieuwe leeftijd")
            x.leeftijd = nieuwe_leeftijd
#verwijder een persoon uit de lijst.
def verwijder_persoon_uit_lijst(lijst):
    zoeknaam = input("geef de naam die je wenst te verwijderen")
    for x,o in enumerate(lijst):
        if o.naam == zoeknaam:
            del lijst[x]
            break
#print lijst gesorteerd op naar A-Z
def print_lijst_sort_naam(lijst):
    lijst.sort(key=lambda x: x.naam)
    toon_lijst(lijst)

def print_lijst_sort_naam_za(lijst):
    lijst.sort(key=lambda x: x.naam)
    lijst.reverse()
    toon_lijst(lijst)

#print lijst gesorteerd op leeftijd
def print_lijst_sort_leeftijd(lijst):
    lijst.sort(key=lambda x: x.leeftijd)
    toon_lijst(lijst)

#print lijst gesorteerd op leeftijd
def print_lijst_sort_leeftijd_oj(lijst):
    lijst.sort(key=lambda x: x.leeftijd)
    lijst.reverse()
    toon_lijst(lijst)

p0 = Persoon("Zoe",19)
p = Persoon("Bart",25)
p2 = Persoon("Mark",32)
p3 = Persoon("Wendy",30)
p4 = Persoon("Arne",41)


personen = [p0,p,p2,p3,p4]
toon_lijst(personen)
#verander_naam_in_lijst(personen)
#verander_leeftijd_in_lijst(personen)
#verwijder_persoon_uit_lijst(personen)
#voeg_persoon_toe(personen)
toon_lijst(personen)
#naam_in_lijst(personen)
print_lijst_sort_naam_za(personen)
print_lijst_sort_leeftijd_oj(personen)
