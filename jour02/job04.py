import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme',
)

cursor =mydb.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

etudiants = cursor.fetchall()
print(etudiants)

cursor.close()
mydb.close()


