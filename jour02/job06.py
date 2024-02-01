import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme',
)

cursor =mydb.cursor()

cursor.execute("SELECT capacite FROM salle")
capacite_totale=0
for capacite  in cursor: 
    capacite_totale += capacite[0]

print(f"La capacité de toute les salles est de {capacite_totale} ")


cursor.close()
mydb.close()
