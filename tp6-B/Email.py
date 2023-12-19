class Email :
    def __init__(self,adresse_emailEx,adresse_emailDestin, fichier_joint,titre="",text=""):
        self.adresse_emailEx = adresse_emailEx
        self.adresse_emailDestin=adresse_emailDestin
        self.fichier_joint = fichier_joint
        self.titre = titre
        self.text = text
    def __str__(self):
        return f"ce mail de {self.titre} contient {self.text} avec l'adresse mail {self.adresse_emailEx} contient le fichier joint{self.fichier_joint}"
        
class Fichier:
    def __init__(self,nom,extension):
        self.nom = nom
        self.extension =extension
    def __str__(self):
        return  f"{self.nom}.{self.extension}"
        

    
class Destination:
    def __init__(self, address):
        if '@' in address and address.count('@') == 1 and address.index('@') > 0 and address.index('@') < len(address) - 1 :
           self.address = address
        else : 
           raise ValueError("adresse non valide")
    
    def __str__(self):
        return  self.address
        
class  Expéditeur: 
    def __init__(self,address):
        if '@' in address and address.count('@') == 1 and address.index('@') > 0 and address.index('@') < len(address) - 1 :
            self.address = address
        else : 
            raise ValueError("adresse non valide")
        
    def __str__(self):
        return  self.address
        
D=Destination("premierTest@example.com")
E=Expéditeur("DeuxièmeTest@example.com")
F=Fichier("file","txt")
EM=Email(D,E,F)
print(EM)

    
    
        
    