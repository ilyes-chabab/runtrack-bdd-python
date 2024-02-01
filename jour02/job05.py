import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme',
)

cursor =mydb.cursor()

cursor.execute("SELECT superficie FROM etage")
superficie_totale=0
for superficie in cursor: 
    superficie_totale += superficie[0]

print(f"La superficie de la plateforme est de {superficie_totale} m²")


cursor.close()
mydb.close()
