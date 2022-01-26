
class Persoon:
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def print_info(self):
        print(self.naam+" "+str(self.leeftijd))



def voeg_persoon_toe(lijst,naam,leeftijd):
    lijst.append(Persoon(naam,leeftijd))

def verander_persoonsnaam_in_lijst(lijst,zoek_naam,nieuwe_naam):
    for x in personen:
        if(zoek_naam == x.naam):
            print("naam in lijst")
            x.naam = nieuwe_naam

def is_persoon_in_lijst(lijst,zoek_naam):
    for x in personen:
        if(zoek_naam == x.naam):
            print("naam in lijst")

def verwijder_persoon_uit_lijst(lijst,zoek_naam):
    for x, o in enumerate(personen):
        if o.naam == zoek_naam:
            del personen[x]
            break
def print_sorteerde_lijst_op_naam(lijst):
    lijst.sort(key=lambda x: x.naam)
    for x in lijst:
       x.print_info()




p1 = Persoon("Mark",25)
p2 = Persoon("Wendy",32)
p3 = Persoon("Kelly",28)
p4 = Persoon("Arne",35)
p5 = Persoon("Jos",52)

personen = [p1,p2,p3,p4,p5]
voeg_persoon_toe(personen,"Bjorn",30)
verander_persoonsnaam_in_lijst(personen,"Bjorn","Karel")
verwijder_persoon_uit_lijst(personen,"Mark")

print_sorteerde_lijst_op_naam(personen)






