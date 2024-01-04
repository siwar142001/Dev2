class Classe :
    def __init__(self,eleve,professeur): 
        self.eleves=[eleve]
        self.prof=professeur
        
    def add_eleves(self,e):
        self.eleves.append(e)
        
    def __str__(self):
        return "cette classe est composée par le prof {} et le nombre d'eleves est {} ".format(self.prof,len(self.eleves))
        

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
    def __init__(self ,nom,prenom,age,adresse,etat_civil,n_tel, role="professeur"):
        self.dossier = Dossier(nom,prenom,age,adresse,etat_civil,n_tel)
        self.role = role
    def __str__(self):
        ch=Dossier.__str__(self.dossier)+" " +str(self.role)
        return ch
          
class Eleve:
    def __init__(self,nom,prenom,age,adresse,etat_civil,n_tel,matricule,role="eleve"):
        self.dossier = Dossier(nom,prenom,age,adresse,etat_civil,n_tel)
        self.matricule=matricule 
        self.role = role
        
    def __str__(self):
        ch=Dossier.__str__(self.dossier)+" " +str(self.matricule)+" " +str(self.role)
        return ch
        

eleve1=Eleve("Salmi","Siwar",22,"Kraainem","celib",4234567,"HE201969")
prof1=Professeur("MR","leProf",40,"Wavre","celib",999999)
eleve2=Eleve("Titi","Tata",24,"LLN","celib",222222,"HE201960")
classe1=Classe(eleve1,prof1)
classe1.add_eleves(eleve2)
print(classe1)
print(eleve1)
print(prof1)
