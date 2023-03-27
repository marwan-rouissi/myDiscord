import mysql.connector
from tkinter import messagebox

class BDD:
    def __init__(self):
        # ma base de donnée
        self.bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "rootpwd",
            database = "mydiscord"
        )
        # création d'un curseur
        self.cursor = self.bd.cursor()
        # variables des tables à manipuler
        self.usersTable = "users"
        self.messagesTable = ""

    # méthode pour récupèrer les utilisateurs inscrits
    def getUsers(self):
        # requête
        req = f"""select * from {self.usersTable};"""

        # execution de ma requête
        self.cursor.execute(req)

        # récupération et stockage de mes données dans la suivante (self.data)
        self.data = self.cursor.fetchall()

        return self.data
    
    def getPseudo(self):
        # requête
        req = f"""select * from {self.usersTable};"""

        # execution de ma requête
        self.cursor.execute(req)

        # récupération et stockage de mes données dans la suivante (self.data)
        self.data = self.cursor.fetchall()

        pseudoList = []
        for row in self.data:
            pseudoList.append(row[4])

        return pseudoList


    # méthode pour ajouter un utilisateur
    def addUser(self, nom, prenom, email, pseudo, passwd, toplevel):
        # requête
        req = f"""insert into {self.usersTable} (nom, prenom, email, pseudo, mdp, id_status) \
            values \
            ("{nom}", "{prenom}", "{email}", "{pseudo}", "{passwd}", {1});"""
        print(f"{nom}", {prenom}, {email}, {pseudo}, {passwd}, {1})
        
        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout à la bd de manière permanente
        self.bd.commit()

        messagebox.showinfo("Info", message=f"Nouvel utilisateur ajouté.")
        toplevel.destroy()
        
        # except:
        #     messagebox.showerror("Error", message="Un (ou plusieurs) champs non renseigné(s).\nVeuillez réessayer.")

    def checkLogin(self, pseudo, passwd, main):
        users = self.getUsers()
        pseudoList = self.getPseudo()
        for user in users:
            if pseudo not in pseudoList:
                print("pseudo inconnu")
                print(user[4], "et", user[5])
                messagebox.showerror("Error", message=f"Utilisateur ou mdp incorect.")
                return
            else:
                if user[4] == pseudo and user[5] == passwd:
                    print("Log in..")
                    main()
                
                


# myDiscord = BDD()
# myDiscord.addUser("Wayne", "Bruce", "Brayne", "bruce.wayne@laplateforme.io", "imbatman")