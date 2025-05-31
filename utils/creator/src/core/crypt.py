try: 
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
except:
    pass
try:
    import secrets
    import base64
except:
    pass


class Crypt:
    key = secrets.token_bytes(32)
    iv = secrets.token_bytes(16)
    
 
    @classmethod
    def encrypt(cls, data): 
        if isinstance(data, str):
            data = data.encode('utf-8')
 

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        cipher = Cipher(algorithms.AES(cls.key), modes.CBC(cls.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Retourne le texte chiffré encodé en base64
        return base64.b64encode(cls.iv + encrypted_data).decode('utf-8')
    
    @classmethod
    def decrypt(cls, data): 
        if cls.key is None or cls.iv is None:
            raise ValueError("La clé et l'IV doivent être générés ou définis avant le déchiffrement.")
        
        data = base64.b64decode(data)
        iv = data[:16]
        data = data[16:]

        cipher = Cipher(algorithms.AES(cls.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(data) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

        return decrypted_data.decode('utf-8')