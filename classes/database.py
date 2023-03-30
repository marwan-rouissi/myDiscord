import mysql.connector
from tkinter import messagebox

class BDD:

    def __init__(self) -> None:
        # ma base de donnée
        self.bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Bl@ckbird772",
            database = "mydiscord"
        )
        # création d'un curseur
        self.cursor = self.bd.cursor()
        # variables des tables à manipuler
        self.usersTable = "users"
        self.messagesTable = "messages"


    # méthode pour récupèrer les utilisateurs inscrits
    def getUsers(self):
        # requête
        req = f"""select * from {self.usersTable};"""

        # execution de ma requête
        self.cursor.execute(req)

        # récupération et stockage de mes données dans la suivante (self.data)
        self.data = self.cursor.fetchall()

        return self.data
    

    # méthode pour récupèrer les pseudo inscrits
    def getPseudo(self):
        # requête
        req = f"""select * from {self.usersTable};"""

        # execution de ma requête
        self.cursor.execute(req)

        # récupération et stockage de mes données dans la suivante (self.data)
        self.data = self.cursor.fetchall()

        pseudoList = []
        for row in self.data:
            pseudoList.append(row[3])

        return pseudoList


    # méthode pour ajouter un utilisateur
    def addUser(self, nom, prenom, pseudo, email, passwd, toplevel):
        # requête
        req = f"""insert into {self.usersTable} (nom, prenom, email, pseudo, passwd, id_status) \
            values \
            ("{nom}", "{prenom}", "{pseudo}", "{email}", "{passwd}", {1});"""
        
        try:
            # execution de ma requête
            self.cursor.execute(req)

            # appliquer l'ajout à la bd de manière permanente
            self.bd.commit()

            messagebox.showinfo("Info", message=f"Nouvel utilisateur ajouté.")
            toplevel.destroy()
        
        except:
            messagebox.showerror("Error", message="Un (ou plusieurs) champs non renseigné(s).\nVeuillez réessayer.")


    # méthode pour vérifier si l'utilisateur existe déjà 
    def checkLogin(self, pseudo, passwd, main):
        users = self.getUsers()
        pseudoList = self.getPseudo()
       
        for user in users:
            if pseudo not in pseudoList:
                print("pseudo inconnu")
                print(user)
                messagebox.showerror("Error", message=f"Utilisateur ou mdp incorecte.")
                return
            else:
                if user[3] == pseudo and user[5] == passwd:
                        print("Log in..")
                        main()


    # méthode pour sauvegarder les msg
    def saveMSG(self, pseudo, message, date, id_chanel):
        # requête
        req = f"""insert into {self.messagesTable} (pseudo, message, date, id_chanel) \
            values \
            ("{pseudo}", "{message}", "{date}", {id_chanel});"""
        
        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout à la bd de manière permanente
        self.bd.commit()

    # méthode pour récupérer la dernière conversation
    def getHistory(self):
        # requête
        req = f"""select * from {self.messagesTable};"""

        # execution de ma requête
        self.cursor.execute(req)

        # récupération et stockage de mes données dans la suivante (self.data)
        self.data = self.cursor.fetchall()

        return self.data