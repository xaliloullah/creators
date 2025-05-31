 
def debug(*args, **kwargs):
    """
    Fonction de débogage qui retourne les arguments passés sous forme de tuple et de dictionnaire.
    Utilisée pour afficher facilement les valeurs des arguments pendant le débogage.
    """
    # Retourne les arguments positionnels et nommés
    return args, kwargs

def print_debug(*args, **kwargs):
    """
    Fonction d'affichage de débogage pour imprimer les arguments passés sous forme lisible.
    Utilise `debug()` en interne pour formater les arguments.
    """
    args, kwargs = debug(*args, **kwargs)
    print("Arguments positionnels:", args)
    print("Arguments nommés:", kwargs)

def log_debug(*args, **kwargs):
    """
    Fonction pour enregistrer les arguments dans un fichier de log pour un suivi plus permanent.
    """
    args, kwargs = debug(*args, **kwargs)
    
    with open("debug_log.txt", "a") as log_file:
        log_file.write("Arguments positionnels: {}\n".format(args))
        log_file.write("Arguments nommés: {}\n".format(kwargs))
        log_file.write("-" * 40 + "\n")

def debug_function(func):
    """
    Un décorateur de débogage pour enregistrer les arguments et le résultat d'une fonction.
    """
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec :")
        print_debug(*args, **kwargs)  # Imprime les arguments de la fonction
        result = func(*args, **kwargs)
        print(f"Résultat de {func.__name__} : {result}")
        return result
    return wrapper

# Exemple d'utilisation d'un décorateur de débogage

@debug_function
def adebugition(a, b):
    return a + b

@debug_function
def concatenation(string1, string2, sep="-"):
    return string1 + sep + string2

if __name__ == "__main__":
    # Tester la fonction debug avec différents types d'arguments
    print_debug(1, 2, 3, a=10, b=20)

    # Tester les fonctions décorées
    adebugition(5, 3)
    concatenation("hello", "world", sep=" ")

    # Enregistrer dans un fichier de log
    log_debug(1, 2, 3, a=10, b=20)
