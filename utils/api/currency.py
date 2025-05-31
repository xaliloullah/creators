from utils.creator.src.app import Creator


# reponse = Creator.http(url="https://api.exchangerate-api.com/v4/latest/XOF").send()

# print(reponse.json())

import requests

class Currency:
    def __init__(self, base_code):
        self.base_code = base_code
        self.api_url = f"https://open.er-api.com/v6/latest/{self.base_code}"
        self.rates = {}

    def update(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            if "rates" in data:
                self.rates = data["rates"]
                return self.save()
        return False

    def save(self):
        # Implémentez ici la logique de sauvegarde (ex: enregistrement dans une base de données)
        print("Données mises à jour et sauvegardées :", self.rates)
        return True  # Retourne True si la sauvegarde réussit

# Exemple d'utilisation
updater = Currency("USD")
success = updater.update()
print("Mise à jour réussie:", success)
