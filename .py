import random
import string
import time
import os
import csv
import json
import math
from datetime import datetime

# =================== 1. Password Generator ===================
def generate_password():
    length = int(input("Longueur du mot de passe : "))
    use_upper = input("Inclure des MAJUSCULES ? (o/n) ").lower() == 'o'
    use_digits = input("Inclure des CHIFFRES ? (o/n) ").lower() == 'o'
    use_symbols = input("Inclure des SYMBOLES ? (o/n) ").lower() == 'o'

    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        print("Erreur : aucun type de caractère sélectionné")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    print("Mot de passe généré :", password)

# =================== 2. Unit Converter ===================
def unit_converter():
    print("1. Km -> Miles\n2. Miles -> Km\n3. C -> F\n4. F -> C")
    choice = input("Choix : ")
    value = float(input("Valeur : "))

    if choice == '1':
        print(f"{value} km = {value * 0.621371:.2f} miles")
    elif choice == '2':
        print(f"{value} miles = {value / 0.621371:.2f} km")
    elif choice == '3':
        print(f"{value} C = {(value * 9/5) + 32:.2f} F")
    elif choice == '4':
        print(f"{value} F = {(value - 32) * 5/9:.2f} C")
    else:
        print("Choix invalide.")

# =================== 3. Notepad ===================
def simple_notepad():
    filename = input("Nom du fichier .txt : ")
    print("Écris ton texte (CTRL+C pour quitter):")
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            while True:
                line = input()
                f.write(line + '\n')
    except KeyboardInterrupt:
        print("\nNote sauvegardée dans", filename)

# =================== 4. Timer / Chrono ===================
def timer():
    sec = int(input("Durée en secondes : "))
    for i in range(sec, 0, -1):
        print(f"Temps restant : {i} sec", end='\r')
        time.sleep(1)
    print("\n⏰ Temps écoulé !")

# =================== 5. To-Do List ===================
def todo_list():
    tasks = []
    while True:
        print("\n1. Ajouter\n2. Supprimer\n3. Lister\n4. Quitter")
        choice = input("Choix : ")
        if choice == '1':
            task = input("Nouvelle tâche : ")
            tasks.append(task)
        elif choice == '2':
            idx = int(input("Indice à supprimer : "))
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        elif choice == '3':
            for i, t in enumerate(tasks):
                print(f"{i}. {t}")
        elif choice == '4':
            break
        else:
            print("Choix invalide")

# =================== Menu Principal ===================
def main():
    tools = {
        '1': ("Générateur de mot de passe", generate_password),
        '2': ("Convertisseur d'unités", unit_converter),
        '3': ("Bloc-notes", simple_notepad),
        '4': ("Minuteur / Chrono", timer),
        '5': ("To-Do List", todo_list),
    }

    while True:
        print("\n=== Mini Outils Python ===")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")
        print("0. Quitter")

        choice = input("Choisissez un outil : ")
        if choice == '0':
            break
        elif choice in tools:
            tools[choice][1]()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
