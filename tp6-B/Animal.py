class Animal:
    def __init__(self, nom, habitat):
        self.nom = nom
        self.habitat = habitat
        self.tete = True
        self.corps = True
        self.membres = True
        

    def __str__(self):
        return(f"{self.nom} est un animal qui habite dans {self.habitat}. Il a une tête, un corps et des membres.")

class Herbivore(Animal):
    def __init__(self, nom, habitat,reg_alimentaire='herbivore'):
        super().__init__(nom, habitat)
        self.reg_alimentaire=reg_alimentaire 
        
class Carnivore(Animal):
    def __init__(self, nom, habitat,reg_alimentaire='carnivore'):
        super().__init__(nom, habitat)
        self.reg_alimentaire=reg_alimentaire        
        
class Habitat:
    def __init__(self, nom):
        self.nom = nom
    
    def __str__(self):
        return f"{self.nom}"
        
       
h=Habitat('Les champs')    
lapin = Herbivore("Lapin", h)
print(lapin)






