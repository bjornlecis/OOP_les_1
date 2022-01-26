
class Persoon:
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def print_info(self):
        print(self.naam+" "+str(self.leeftijd))

def toon_dictonary(dict):
    for x in dict:
         print("{} is {} jaar oud".format(dict[x].naam,dict[x].leeftijd))
        #commentaar

def zoek_naam_in_dict(dict,zoeknaam):
    for x in dict:
        if zoeknaam == dict[x].naam:
            print(zoeknaam+" gevonden")

def voeg_persoon_toe(dict,key,naam,leeftijd):
    p = Persoon(naam,leeftijd)
    dict[key]=p


p1 = Persoon("Mark",25)
p2 = Persoon("Wendy",32)
p3 = Persoon("Kelly",28)
p4 = Persoon("Arne",35)

personen = {"Persoon1":p1,"Persoon2":p2, "Persoon3":p3,"Persoon4":p4}

#toon_dictonary(personen)
zoek_naam_in_dict(personen,"Peter")
voeg_persoon_toe(personen,"Persoon5","Mario",22)
toon_dictonary(personen)

