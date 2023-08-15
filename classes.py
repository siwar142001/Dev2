import json
import shutil

class Vehicule:
    def __init__(self, type_vehicule, chassis, marque, modele, couleur, portes, kilometrage, carburant, prix, est_a_louer, prix_apres_promotion=None):
        self.type_vehicule = type_vehicule
        self.chassis = chassis
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.portes = portes
        self.kilometrage = kilometrage
        self.carburant = carburant
        self.prix = prix
        self.est_a_louer = est_a_louer
        self.prix_apres_promotion = prix_apres_promotion if prix_apres_promotion is not None else prix

class Parking:
    def __init__(self):
        self.voitures = []
        self.motos = []
    def vendre_vehicule(self, chassis):
        vehicule = self.chercher_vehicule_par_chassis(chassis)
        if vehicule:
            self.supprimer_vehicule(chassis)
            self.ajouter_vehicule_vendu(vehicule)
            print("Véhicule vendu.")
        else:
            print("Véhicule non trouvé.")

    def ajouter_vehicule_vendu(self, vehicule):
        try:
            with open("vendu.json", 'r') as fichier:
                vehicules_vendus = json.load(fichier)
        except (FileNotFoundError, json.JSONDecodeError):
            vehicules_vendus = {'voitures': [], 'motos': []}

        if vehicule.type_vehicule == 'voiture':
            vehicules_vendus['voitures'].append(vars(vehicule))
        elif vehicule.type_vehicule == 'moto':
            vehicules_vendus['motos'].append(vars(vehicule))

        with open("vendu.json", 'w') as fichier:
            json.dump(vehicules_vendus, fichier)
    def ajouter_vehicule(self, vehicule):
        if vehicule.type_vehicule == 'voiture':
            if len(self.voitures) < 30:
                self.voitures.append(vehicule)
                self.enregistrer_vehicules_json("stock.json")
            else:
                print("Pas de place pour une autre voiture.")
        elif vehicule.type_vehicule == 'moto':
            if len(self.motos) < 20:
                self.motos.append(vehicule)
                self.enregistrer_vehicules_json("stock.json")
            else:
                print("Pas de place pour une autre moto.")
        else:
            print("Type de véhicule non reconnu.")

    def supprimer_vehicule(self, chassis):
        for voiture in self.voitures:
            if voiture.chassis == chassis:
                self.voitures.remove(voiture)
                self.enregistrer_vehicules_json("stock.json")
                return
        for moto in self.motos:
            if moto.chassis == chassis:
                self.motos.remove(moto)
                self.enregistrer_vehicules_json("stock.json")
                return
        print("Véhicule non trouvé.")

    def afficher_stock(self, promotions):
        choix = input("Voulez-vous afficher tous les véhicules, les voitures, les motos, ou chercher par numéro de chassis? (tous/voitures/motos/chassis): ")

        if choix.lower() == 'tous':
            print("Voitures:")
            for voiture in self.voitures:
                self.afficher_vehicule(voiture, promotions)
            print("Motos:")
            for moto in self.motos:
                self.afficher_vehicule(moto, promotions)
        elif choix.lower() == 'voitures':
            print("Voitures:")
            for voiture in self.voitures:
                self.afficher_vehicule(voiture, promotions)
        elif choix.lower() == 'motos':
            print("Motos:")
            for moto in self.motos:
                self.afficher_vehicule(moto, promotions)
        elif choix.lower() == 'chassis':
            chassis = input("Entrez le numéro de chassis du véhicule: ")
            vehicule = self.chercher_vehicule_par_chassis(chassis)
            if vehicule:
                self.afficher_vehicule(vehicule, promotions)
            else:
                print("Véhicule non trouvé.")

    def chercher_vehicule_par_chassis(self, chassis):
        for voiture in self.voitures:
            if voiture.chassis == chassis:
                return voiture
        for moto in self.motos:
            if moto.chassis == chassis:
                return moto
        return None
    def modifier_vehicule(self, chassis):
        vehicule = self.chercher_vehicule_par_chassis(chassis)
        if vehicule:
            while True:
                print("Que voulez-vous modifier ?")
                print("1. Type")
                print("2. Marque")
                print("3. Modèle")
                print("4. Couleur")
                print("5. Portes (voiture seulement)")
                print("6. Kilométrage")
                print("7. Carburant")
                print("8. Prix")
                print("9. Status de location")
                print("10. Fin de la modification")

                choix = int(input("Votre choix: "))
                if choix == 1:
                    vehicule.type_vehicule = input("Nouveau type de véhicule (voiture/moto): ")
                elif choix == 2:
                    vehicule.marque = input("Nouvelle marque: ")
                elif choix == 3:
                    vehicule.modele = input("Nouveau modèle: ")
                elif choix == 4:
                    vehicule.couleur = input("Nouvelle couleur: ")
                elif choix == 5 and vehicule.type_vehicule == "voiture":
                    vehicule.portes = int(input("Nouveau nombre de portes: "))
                elif choix == 6:
                    vehicule.kilometrage = int(input("Nouveau kilométrage: "))
                elif choix == 7:
                    vehicule.carburant = input("Nouveau carburant: ")
                elif choix == 8:
                    vehicule.prix = int(input("Nouveau prix: "))
                elif choix == 9:
                    vehicule.est_a_louer = input("Est-ce à louer ? (oui/non): ").lower() == 'oui'
                elif choix == 10:
                    self.enregistrer_vehicules_json("stock.json")
                    break
    def afficher_vehicule(self, vehicule, promotions):
        print('- - - - - - - - - - - - - - - - - -')
        print(vehicule.marque, vehicule.modele, 'chassis:', vehicule.chassis, 'couleur:', vehicule.couleur)
        print('Prix avant réduction: euro', vehicule.prix)
        reduction = promotions.get((vehicule.marque, vehicule.modele), 0)
        prix_apres_reduction = vehicule.prix * (1 - reduction / 100)
        print('Prix après réduction: euro', prix_apres_reduction)
        print('- - - - - - - - - - - - - - - - - -')

    def enregistrer_vehicules_json(self, nom_fichier):
        vehicules = {'voitures': [vars(voiture) for voiture in self.voitures],
                    'motos': [vars(moto) for moto in self.motos]}
        with open(nom_fichier, 'w') as fichier:
            json.dump(vehicules, fichier)

    def importer_vehicules_json(self, nom_fichier):
        try:
            with open(nom_fichier, 'r') as fichier:
                vehicules = json.load(fichier)
        except FileNotFoundError:
            vehicules = {}
        except json.JSONDecodeError:
            vehicules = {}

        for voiture_data in vehicules.get('voitures', []):
            voiture = Vehicule(**voiture_data)
            self.voitures.append(voiture)
        for moto_data in vehicules.get('motos', []):
            moto = Vehicule(**moto_data)
            self.motos.append(moto)
    def appliquer_promotion(self, marque, modele, reduction):
        for voiture in self.voitures:
            if voiture.marque == marque and voiture.modele == modele:
                voiture.prix_apres_promotion = voiture.prix * (1 - reduction / 100)
        for moto in self.motos:
            if moto.marque == marque and moto.modele == modele:
                moto.prix_apres_promotion = moto.prix * (1 - reduction / 100)
        self.enregistrer_vehicules_json("stock.json")