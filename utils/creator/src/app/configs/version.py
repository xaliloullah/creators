class Version:
    def __init__(self, version: str= None):
        try:
            major, minor, patch = version.split(".")
            if "-" in patch:
                patch, suffix = patch.split("-")
                self._suffix_ = suffix
            else:
                self._suffix_ = ""
            self._major_ = int(major)
            self._minor_ = int(minor)
            self._patch_ = int(patch)
        except ValueError as e:
            raise ValueError(e)

    def __str__(self): 
        return f"{self._major_}.{self._minor_}.{self._patch_}{f"-{self._suffix_}" if self._suffix_ else ""}"

    def major(self): 
        self._major_ += 1
        self._minor_ = 0
        self._patch_ = 0
        self._suffix_ = ''
        return self

    def minor(self): 
        self._minor_ += 1
        self._patch_ = 0
        self._suffix_ = ''
        return self

    def patch(self): 
        self._patch_ += 1
        self._suffix_ = ''
        return self
        
    def suffix(self, suffix): 
        self._suffix_ = suffix
        return self
     
    def get(self): 
        return str(self)
     
    def set(self, version:str): 
        self(version)

# # Exemple d'utilisation
# if __name__ == "__main__":
#     version = Version("1.5.2")
#     print("Version initiale:", version)

#     version.patch()
#     print("Après un correctif:", version)

#     version.minor()
#     print("Après une nouvelle fonctionnalité:", version)

#     version.major()
#     print("Après un changement majeur:", version)

#     version_with_suffix_ = Version("2.3.4-beta")
#     print("Version initiale avec suffixe:", version_with_suffix_)



# Alpha : Premières versions instables, généralement pour tests internes.
# Beta : Version fonctionnelle, mais qui peut contenir des bugs, destinée aux tests externes.
# RC (Release Candidate) : Version proche de la finale, avec des ajustements mineurs possibles.
# Stable : Version prête pour la production.

# Changelog

# Version 1.2.0 :
# - Ajout de l’authentification à deux facteurs.
# - Amélioration des performances pour les gros fichiers.
# - Correction d’un bug affectant l’envoi d’emails.
