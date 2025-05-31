class Middleware:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        # Avant la requête
        print(f"Middleware: Requête reçue: {request}")

        # Passe la requête au prochain gestionnaire si disponible
        if self.next_handler:
            response = self.next_handler.handle(request)
        else:
            # Si aucun gestionnaire suivant, on traite la réponse directement ici
            response = f"Traitement par défaut pour {request}"

        # Après la requête
        print(f"Middleware: Réponse générée: {response}")
        return response


class FinalHandler:
    def handle(self, request):
        # Traitement final de la requête
        return f"Réponse finale pour {request}"


# Exemple d'utilisation
if __name__ == "__main__":
    # Crée une chaîne de gestionnaires (middleware -> gestionnaire final)
    final_handler = FinalHandler()
    middleware = Middleware(next_handler=final_handler)

    # Simule une requête
    request = "Exemple de requête"
    response = middleware.handle(request)

    print(f"Résultat final: {response}")
