try: 
    import requests
except:
    pass

class Http:
    """
    Cette classe étend les fonctionnalités de `requests.Request` en ajoutant une gestion plus flexible des requêtes HTTP.
    Elle permet l'envoi de requêtes avec des méthodes HTTP spécifiques tout en encapsulant une session `requests.Session` pour améliorer la réutilisation des connexions.
    """

    def __init__(self, data=None, **kwargs):
        """
        Initialisation de la requête HTTP avec des paramètres optionnels.
        """
        self.data = data or {}
        self.method = kwargs.get("method", "GET")
        self.url = kwargs.get("url", None)
        self.headers = kwargs.get("headers", {})
        self.files = kwargs.get("files", None)
        self.params = kwargs.get("params", None)
        self.auth = kwargs.get("auth", None)
        self.cookies = kwargs.get("cookies", None)
        self.hooks = kwargs.get("hooks", None)
        self.json = kwargs.get("json", None)
        self.session = requests.Session()
        self.request = requests.Request

    def _prepare_request(self):
        """
        Prépare la requête HTTP pour l'envoi.
        """
        return self.session.prepare_request(self._build_request())

    def _build_request(self):
        """
        Construit l'objet `requests.Request` avec les paramètres actuels.
        """
        return self.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            files=self.files,
            data=self.data,
            params=self.params,
            auth=self.auth,
            cookies=self.cookies,
            hooks=self.hooks,
            json=self.json
        )

    def send(self):
        """
        Envoie la requête HTTP via une session et renvoie la réponse.
        """
        prepared_request = self._prepare_request()
        try:
            response = self.session.send(prepared_request)
            response.raise_for_status()  
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erreur de requête : {e}")
            return None

    def _send_request(self, method, url, **kwargs):
        """
        Méthode interne pour envoyer une requête HTTP avec la méthode et l'URL spécifiées.
        """
        self.method = method
        self.url = url
        self.data = kwargs.get("data", None)
        self.headers = kwargs.get("headers", {})
        self.files = kwargs.get("files", None)
        self.params = kwargs.get("params", None)
        self.auth = kwargs.get("auth", None)
        self.cookies = kwargs.get("cookies", None)
        self.hooks = kwargs.get("hooks", None)
        self.json = kwargs.get("json", None)
        
        return self.send()
    
    def capture(self):
        """
        Capture les informations de la requête actuelle (URL, méthode, en-têtes, données, etc.)
        et retourne un dictionnaire avec ces informations.
        """
        return {
            "method": self.method,
            "url": self.url,
            "headers": self.headers,
            "data": self.data,
            "files": self.files,
            "params": self.params,
            "auth": self.auth,
            "cookies": self.cookies,
            "json": self.json
        }