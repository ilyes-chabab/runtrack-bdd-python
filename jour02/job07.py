import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme',
)

cursor =mydb.cursor()

cursor.execute("SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom from employe inner join service on employe.id_service = service.id")
employer=cursor.fetchall()

class Employe:

    def create(self,nom,prenom,salaire,id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire=salaire
        self.id_service=id_service
        cursor.execute("insert into employe (nom,prenom,salaire,id_service) values ('{self.nom}','{self.prenom}',{self.salaire},{self.id_service})")

employe = Employe()
employe.create('wisley','ron',700,2)
print(employer)


        


mydb.close()
cursor.close()

