import math

class Calculator:
    def __init__(self):
        self.history = []
        self.variables = {}
        self.result = 0
        self.allowed = {
            'abs': abs,
            'round': round,
            'sqrt': math.sqrt,
            'log': math.log,
            'log10': math.log10,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'pi': math.pi,
            'e': math.e,
            'pow': pow,
            'factorial': math.factorial,
            'floor': math.floor,
            'ceil': math.ceil,
        }

    def calculate(self, expression: str):
        try:
            expression = expression.strip()

            context = {**self.allowed, **self.variables, 'ans': self.result}

            # Affectation de variable : ex "x = 2 + 3"
            if '=' in expression:
                var, expr = map(str.strip, expression.split('=', 1))
                if not var.isidentifier():
                    return f"Nom de variable invalide : {var}"
                result = eval(expr, {"__builtins__": {}}, context)
                self.variables[var] = result
                self.result = result
                self.history.append((expression, result))
                return f"{var} = {result}"

            # Calcul normal
            result = eval(expression, {"__builtins__": {}}, context)
            self.result = result
            self.history.append((expression, result))
            return result

        except ZeroDivisionError:
            return "Erreur : Division par zéro"
        except Exception as e:
            return f"Erreur : Expression invalide ({e})"

    def get_history(self):
        return self.history
    
    def set_history(self, history):
        self.history = history

    def clear_history(self):
        self.set_history([])

    def clear_variables(self):
        self.variables = {}
        self.result = 0


# Interface utilisateur
calc = Calculator()

print("=== Calculatrice Scientifique ===")
print("Tapez 'exit' pour quitter, 'history' pour l'historique, 'clear' pour tout effacer.\n")
print("Utilisez 'ans' pour réutiliser le dernier résultat.\n")

while True:
    user_input = input(">> ").strip()

    if user_input.lower() in ('exit', 'quit'):
        print("Fermeture de la calculatrice.")
        break
    elif user_input.lower() == 'history':
        if not calc.get_history():
            print("Aucun calcul effectué.")
        else:
            for expr, res in calc.get_history():
                print(f"{expr} = {res}")
    elif user_input.lower() == 'clear':
        calc.clear_history()
        calc.clear_variables()
        print("Historique et variables effacés.")
    elif not user_input:
        continue
    else:
        print(calc.calculate(user_input))
