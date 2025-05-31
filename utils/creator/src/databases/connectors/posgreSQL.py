import psycopg2 
conn = psycopg2.connect(
    dbname="example",
    user="username",
    password="password",
    host="localhost"
)

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Création d'une table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    age INT)''')

# Insertion de données dans la table
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Bob', 25))

# Commit des modifications et fermeture de la connexion
conn.commit()
conn.close()
