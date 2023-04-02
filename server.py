import socket
import threading
from classes.database import *


## Variables constantes
#
# Choix d'un port libre
PORT = 33000
#
# Définition de l'ip du serveur
SERVER = "127.0.0.1"
#
# Stockage de l'adresse sous forme d'un tuple
ADDRESS = (SERVER, PORT)
#
# FORMAT pour l'encodage et de décodage des messages envoyés et reçus
FORMAT = "utf-8"
#
# instancier un objet base de donnée
database = BDD()


class Server:
	# création d'un objet Server

	def __init__(self) -> None:
		# Création d'un socket serveur
		self.server = socket.socket(socket.AF_INET,
							socket.SOCK_STREAM)

		# Lier l'adresse du serveur à son socket
		self.server.bind(ADDRESS)

		# Listes contenants les clients connectés au serveur ainsi que leur nom
		self.clients, self.names = [], []


	# Fonction pour commencer la communication
	def startChat(self):

		print("server is working on " + SERVER)

		# écouter toute connexion entrante
		self.server.listen()

		while True:

			# accepter les connexions et retourner une nouvelle connexion au client et à l'adresse à laquelle il est lié
			conn, addr = self.server.accept()
			conn.send("NAME".encode(FORMAT))

			# 1024 represente le nombre max de data (bytes) pouvant être recu
			self.name = conn.recv(1024).decode(FORMAT)

			# ajouter le client et son pseudo aux listes dédiées
			self.names.append(self.name)
			self.clients.append(conn)

			print(f"Name is :{self.name}")

			# diffuser l'historique à tout les clients connectés 
			self.broadcastMessage(self.displayHistory())

			# broadcast message
			self.broadcastMessage(f"\n{self.name} has joined the chat!\n\n".encode(FORMAT))

			# initialisation et lancement du thread de gestion des msgs entrants
			thread = threading.Thread(target=self.handle,
									args=(conn, addr))
			thread.start()

			# nombre de clients connectés au serveur
			print(f"active connections {threading.active_count()-1}\n")



	# methode pour gérer les messages entrants
	def handle(self, conn, addr):

		print(f"new connection {addr}")
		connected = True
		try:
			while connected:
				# reception du msg
				message = conn.recv(1024)
				# diffusion du msg
				self.broadcastMessage(message)
				# sauvegarde du msg dans la BDD
				self.saveHistory(message)

		except:
			# print(f"erreur co de {self.name}")
			self.broadcastMessage(f"\n{self.name} has left the chat!\n\n".encode(FORMAT))
			client_index = self.clients.index(conn)

			self.names.pop(client_index)
			# supprimer le client déconnecté depuis de la liste à l'aide de son index
			self.clients.pop(client_index)

			# fermer la connexion
			conn.close()


	# méthode pour sauvegarder les messages échangés dans la BDD
	def saveHistory(self, message):
		# Convertion du msg de bytes en str et recupération des éléments importants
		info = message.split()
		pseudo = str(info[0], FORMAT)
		time = (info[1] + b" " + info[2])
		sent_time = "".join(map(chr, time))
		msgList = info[3:]
		msg = ""
		
		# convertir les msg récupérés sous forme de liste en chaine de caractères
		for i in msgList:
			msg += (str(i, FORMAT) + " ")
		
		# Sauvegarde du msg dans la BDD
		database.saveMSG(pseudo, msg, sent_time, 1)

	
	# méthode pour afficher l'historique après l'avoir récupéré 
	def displayHistory(self):
		historique = database.getHistory()
		H = ""
		for row in historique:

			history = f"{row[1]}    {row[3]}:\n{row[2]}\n"
			H += history
		
		encodedHistory = H.encode(FORMAT)
		return encodedHistory

	# methode pour diffuser le msg à chacun des clients du serveur
	def broadcastMessage(self, message):
		try:
			for client in self.clients:
				client.send(message)
		except:
			print("Un client vient de se déconnecter.")

if __name__ == "__main__":
	serv = Server()
	serv.startChat()