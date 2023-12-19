class Classe :
    def __init(self,nb):
        self.nb=nb  #nombre de personne 

class Dossier :
    def __init__(self,nom,prenom,age,adresse,etat_civil,n_tel):
        self.nom=nom 
        self.prenom=prenom
        self.age=age
        self.adresse=adresse
        self.etat_civil=etat_civil
        self.n_tel=n_tel 
    def __str__(self):
        ch="coordonnées de la personne:{} {} il a {} son addresse est : {} son état civil {} son numero de telephone {} ".format(self.nom,self.prenom,self.age,self.adresse,self.etat_civil,self.n_tel)   
        return ch
    

     
class Professeur:
    def __init__(self, dossier , role="professeur"):
        self.dossier = dossier
        self.role = role
    def __str__(self):
        ch=Dossier.__str__(self.dossier)+" " +str(self.role)
        return ch
          
class Eleve:
    def __init__(self,dossier,matricule,role="eleve"):
        self.dossier = dossier
        self.matricule=matricule 
        self.role = role
        
    def __str__(self):
        ch=Dossier.__str__(self.dossier)+" " +str(self.matricule)+" " +str(self.role)
        return ch
        
dossier1=Dossier("Salmi","Siwar",22,"Kraainem","celib",4234567)
#print(dossier1)
dossier2=Dossier("MR","leProf",40,"Wavre","celib",999999)
#dossier2=Dossier("Monsieur","Le prof",40,"Wavre","Marié",2563658)
e1=Eleve(dossier1,"HE201969")
p1=Professeur(dossier2)
print(e1)
print(p1)