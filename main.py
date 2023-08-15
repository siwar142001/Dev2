from classes import *

class Systeme:
    def __init__(self):
        self.parking = Parking()
        self.promotions = {}  
        self.parking.importer_vehicules_json("stock.json")

    def ajouter_promotion(self):
        marque = input("Marque de voiture pour la promotion: ")
        modele = input("Modèle de voiture pour la promotion: ")
        reduction = float(input("Réduction en pourcentage (%): "))
        self.promotions[(marque, modele)] = reduction
        self.parking.appliquer_promotion(marque, modele, reduction) 
        print(f"Promotion ajoutée: {reduction}% de réduction sur {marque} {modele}")

    def menu(self, est_patron):
        while True:
            print("\nMenu:")
            print("1. Afficher le stock")
            if est_patron:
                print("2. Ajouter véhicule")
                print("3. Supprimer véhicule")
                print("4. Modifier véhicule")
                print("5. Vendre véhicule")
                print("6. Ajouter promotion")
                print("0. Quitter")
            else:
                print("2. Quitter")

            choix = int(input("Votre choix: "))
            if choix == 1:
                self.parking.afficher_stock(self.promotions)
            elif choix == 2 and est_patron:
                self.ajouter_vehicule()
            elif choix == 3 and est_patron:
                chassis = input("Numéro de chassis du véhicule à supprimer: ")
                self.parking.supprimer_vehicule(chassis)
            elif choix == 4 and est_patron:
                chassis = input("Numéro de chassis du véhicule à modifier: ")
                self.parking.modifier_vehicule(chassis)
            elif choix == 5 and est_patron:
                chassis = input("Numéro de chassis du véhicule à vendre: ")
                self.parking.vendre_vehicule(chassis)
            elif choix == 6 and est_patron:
                self.ajouter_promotion()
            elif (choix == 0 and est_patron) or (choix == 2 and not est_patron):
                break
    def ajouter_promotion(self):
        marque = input("Marque de voiture pour la promotion: ")
        modele = input("Modèle de voiture pour la promotion: ")
        reduction = float(input("Réduction en pourcentage (%): "))
        self.promotions[(marque, modele)] = reduction
        self.parking.appliquer_promotion(marque, modele, reduction) 
        print(f"Promotion ajoutée: {reduction}% de réduction sur {marque} {modele}")
    def ajouter_vehicule(self):
        type_vehicule = input("Type de véhicule (voiture/moto): ").lower()
        chassis = input("Numéro de chassis: ")
        marque = input("Marque: ")
        modele = input("Modèle: ")
        couleur = input("Couleur: ")
        
        if type_vehicule == 'voiture':
            while True:
                try:
                    portes = int(input("Nombre de portes: "))
                    break
                except ValueError:
                    print("Saisie incorrecte. Veuillez entrer un nombre entier.")
        elif type_vehicule == 'moto':
            portes = 0
        else:
            print("Type de véhicule non reconnu.")
            return

        kilometrage = int(input("Kilométrage: "))
        carburant = input("Carburant: ")
        prix = int(input("Prix en euro: "))
        est_a_louer = input("Est-ce à louer ? (oui/non): ").lower() == 'oui'

        vehicule = Vehicule(type_vehicule, chassis, marque, modele, couleur, portes, kilometrage, carburant, prix, est_a_louer)
        self.parking.ajouter_vehicule(vehicule)

def demander_identifiants():
    with open("credentials.json", "r") as file:
        credentials = json.load(file)
    while True:
        login = input("Login: ")
        mot_de_passe = input("Mot de passe: ")
        for user_type, user_credentials in credentials.items():
            if user_credentials["login"] == login and user_credentials["password"] == mot_de_passe:
                return user_type == "patron"
        print("Identifiants incorrects. Veuillez réessayer.")

if __name__ == "__main__":
    est_patron = demander_identifiants()
    systeme = Systeme()
    systeme.menu(est_patron)
