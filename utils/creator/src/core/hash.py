try: 
    import bcrypt
except:
    pass

try: 
    import hashlib
    import secrets
    import base64 
except:
    pass

class Hash:
    def __init__(self, rounds=12):
        """
        Initialise la classe Hash.
        :param rounds: Nombre de tours de salage (facteur de coût), par défaut 12.
        """
        self.rounds = rounds

    def make(self, password: str) -> str:
        """
        Hache un mot de passe en utilisant bcrypt avec un sel unique.
        :param password: Mot de passe à hacher.
        :return: Mot de passe haché (en format string).
        """
        # Convertir le mot de passe en bytes (bcrypt attend des bytes)
        password_bytes = password.encode('utf-8')

        # Générer un sel avec le facteur de coût spécifié
        salt = bcrypt.gensalt(rounds=self.rounds)

        # Hacher le mot de passe avec le sel
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        # Retourner le mot de passe haché
        return hashed_password.decode('utf-8')

    def check(self, password: str, hashed_password: str) -> bool:
        """
        Vérifie si un mot de passe donné correspond à un mot de passe haché.
        :param password: Le mot de passe à vérifier.
        :param hashed_password: Le mot de passe haché à comparer.
        :return: True si le mot de passe correspond, False sinon.
        """
        # Convertir le mot de passe et le haché en bytes
        password_bytes = password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')

        # Vérifier si le mot de passe correspond au haché
        return bcrypt.checkpw(password_bytes, hashed_password_bytes)

    def get_salt(self, hashed_password: str) -> str:
        """
        Récupère le sel d'un mot de passe haché bcrypt.
        :param hashed_password: Le mot de passe haché.
        :return: Le sel utilisé dans le hachage.
        """
        # Extraire le sel du mot de passe haché (il est encodé dans la première partie)
        return hashed_password[:29]  # Les 29 premiers caractères représentent le sel

    def generate_secure_random_password(self, length=16) -> str:
        """
        Génère un mot de passe aléatoire sécurisé.
        :param length: La longueur du mot de passe à générer.
        :return: Un mot de passe aléatoire sécurisé.
        """ 
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'
        password = ''.join(secrets.token_bytes(1).decode('latin-1') for _ in range(length))
        return password

    def hash_with_custom_salt(self, password: str, salt: str) -> str:
        """
        Hache un mot de passe avec un sel personnalisé.
        :param password: Mot de passe à hacher.
        :param salt: Sel personnalisé.
        :return: Mot de passe haché (en format string).
        """
        # Convertir le mot de passe et le sel en bytes
        password_bytes = password.encode('utf-8')
        salt_bytes = salt.encode('utf-8')

        # Hacher le mot de passe avec le sel fourni
        hashed_password = bcrypt.hashpw(password_bytes, salt_bytes)

        # Retourner le mot de passe haché
        return hashed_password.decode('utf-8')

    def compare_hashes(self, hash1: str, hash2: str) -> bool:
        """
        Compare deux hachages pour savoir s'ils sont identiques.
        :param hash1: Premier hachage à comparer.
        :param hash2: Deuxième hachage à comparer.
        :return: True si les hachages sont identiques, False sinon.
        """
        return hash1 == hash2

    def decode_salt(self, hashed_password: str) -> str:
        """
        Décoder le sel (base64) d'un mot de passe haché bcrypt.
        :param hashed_password: Le mot de passe haché.
        :return: Sel décodé en base64.
        """
        salt = self.get_salt(hashed_password)
        return base64.b64encode(salt.encode('utf-8')).decode('utf-8')

 
class Hash2:
    def __init__(self, algorithm="sha3_256"):
        """
        Initialise une instance avec un algorithme de hachage.
        """
        self.algorithm = algorithm.lower()

    def method(self):
        """Retourne la méthode de hachage associée à l'algorithme."""
        return getattr(hashlib, self.algorithm, None)

    def generate_salt(self, length=16):
        """Génère un sel cryptographique."""
        return secrets.token_bytes(length)

    def hash(self, password):
        """
        Hache un mot de passe avec un sel.
        Retourne le hachage au format "salt:hashed_password".
        """
        if isinstance(password, str):
            password = password.encode('utf-8')
 
        salt = self.generate_salt()
 
        hash_method = self.method()
        if hash_method:
            hash_object = hash_method()
            hash_object.update(salt + password) 
            return f"{salt.hex()}:{hash_object.hexdigest()}"
        else:
            raise ValueError(f"Algorithm '{self.algorithm}' not supported.")

    def verify(self, password, stored_hash):
        """
        Vérifie si un mot de passe correspond au hachage stocké.
        """
        try: 
            salt_hex, hashed_password = stored_hash.split(":")
            salt = bytes.fromhex(salt_hex)

            if isinstance(password, str):
                password = password.encode('utf-8')
 
            hash_method = self.method()
            if hash_method:
                hash_object = hash_method()
                hash_object.update(salt + password) 
                return hash_object.hexdigest() == hashed_password
            else:
                raise ValueError(f"Algorithm '{self.algorithm}' not supported.")
        except Exception as e: 
            print(f"Erreur : {e}")
            return False

# # Exemple d'utilisation
# if __name__ == "__main__":
#     hasher = Hash()

#     # Mot de passe à hacher
#     password = "MotDePasseSuperSecret"

#     # # Hachage et stockage
#     # stored_hash = hasher.hash(password)
#     # print(f"Hachage stocké : {stored_hash}")

#     # Vérification du mot de passe
#     is_verified = hasher.verify(password, "ecb531338bcfdc504f0e94e46a9b9f36:dcd37e254c0471f42ae1f7294c5a5f1b929f1454e08b8d6929a0e93494667539")
#     print(f"Vérification réussie : {is_verified}")

#     # Vérification avec un mot de passe incorrect
#     is_verified_incorrect = hasher.verify("MauvaisMotDePasse", "ecb531338bcfdc504f0e94e46a9b9f36:dcd37e254c0471f42ae1f7294c5a5f1b929f1454e08b8d6929a0e93494667539")
#     print(f"Vérification échouée : {is_verified_incorrect}")
