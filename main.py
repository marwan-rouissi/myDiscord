from tkinter import *
import customtkinter
import tkinter.scrolledtext
from classes.database import *
from time import strftime
import socket
import threading

PORT = 33000
# SERVER = "192.168.1.60"
# SERVER = "127.0.0.1"
SERVER = "10.10.0.166"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
client.connect(ADDRESS)

class App():
    # création d'un objet App (interface graphique)
    def __init__(self):
        self.root = customtkinter.CTk()
        # Dimensions
        self.appwidth = 650
        self.appheight = 400
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.x = (self.screenwidth / 2) - (self.appwidth / 2)
        self.y = (self.screenheight / 2) - (self.appheight / 2)
        self.root.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')
        self.root.title("ChatKing - Login")
        self.root.iconbitmap("img/chatking.ico")
        customtkinter.set_appearance_mode("dark")
        # instancier un objet bdd
        self.database = BDD()
        # Définition de la compostion de la fenête de log 
        framelogin = customtkinter.CTkFrame(master=self.root, height=250)
        framelogin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Pseudo
        self.pseudo_entry = customtkinter.CTkEntry(master=framelogin, placeholder_text="Pseudonym", justify="center")
        self.pseudo_entry.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # Password
        self.passwd_entry = customtkinter.CTkEntry(master=framelogin, placeholder_text="Password", justify="center", show="*")
        self.passwd_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        # Bouton Login
        login_btn = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Login", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.login)
        login_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Bouton Register
        register = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Register", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.register)
        register.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        self.var = IntVar()
        self.readable_checkbox = customtkinter.CTkCheckBox(master=framelogin, text="Show password", variable=self.var, onvalue=1, offvalue=0, command=self.readable)
        self.readable_checkbox.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        self.passwd_entry.bind("<Return>", (lambda event: self.login()))
        self.root.mainloop()
        # fermeture du curseur utilisé depuis la bdd
        self.database.cursor.close()
    
    # méthode pour ouvrir la fenêtre principale de l'app ChatKing
    def main(self):
        self.gui = customtkinter.CTk()
        self.gui.geometry("600x550")
        self.gui.iconbitmap("img/chatking.ico")
        self.gui.title(f"ChatKing - logged in as {self.pseudo}")
        self.gui._set_appearance_mode("dark")

        # thread pour la reception de messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

        self.msg_frame = customtkinter.CTkFrame(self.gui)

        self.listbox = Listbox(self.msg_frame, width=50, height=10, bg="#2A2A2A", fg="#fff")
        self.listbox.pack()
        self.msg_frame.pack()
        self.msg_field = tkinter.scrolledtext.ScrolledText(self.msg_frame, height=15, width=50)
        self.msg_field.config(state="normal", bg="#2A2A2A", fg="#fff")
        self.msg_field.pack()

        self.my_msg = StringVar()
        self.msg_entry = Entry(self.gui, textvariable=self.my_msg)
        # appuyer sur entrer pour envoyer un message
        self.msg_entry.bind("<Return>", (lambda event: self.send()))
        self.msg_entry.pack()
        send_btn = Button(self.gui, text="Send", command=self.send)
        send_btn.pack()

        self.logout_btn = Button(self.gui, text="Log out", command=self.logout)
        self.logout_btn.pack()

        # Fermeture de la fenêtre de log avant d'ouvrir la fenêtre main
        self.root.destroy()
        self.gui.mainloop()
    
    # fonction pour afficher ou masquer le mdp selon si la case dédiée est selectionnée ou pas 
    def readable(self):
        if self.var.get() == 1 :
            self.passwd_entry.configure(show="")
        else:
            self.passwd_entry.configure(show="*")

    # méthode pour se déconnecter
    def logout(self):
        # Fermeture de la fenêtre de main avant d'ouvrir la fenêtre log
        self.gui.destroy()
        App()

    def login(self):
        self.pseudo = self.pseudo_entry.get()
        passwd = self.passwd_entry.get()
        self.database.checkLogin(self.pseudo, passwd, self.main)
        # self.main()

    def register(self):
        window = customtkinter.CTkToplevel()
        window.attributes('-topmost', 'true')
        window.title("ChatKing - Register")
        window.iconbitmap("img/chatking.ico")
        appwidth = 650
        appheight = 400
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        x = (screenwidth / 2) - (appwidth / 2)
        y = (screenheight / 2) - (appheight / 2)
        window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')
        frameregister = customtkinter.CTkFrame(master=window, height=280)
        frameregister.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Nom
        name_entry = customtkinter.CTkEntry(master=frameregister, placeholder_text="Name")
        name_entry.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # Prénom
        fname_entry = customtkinter.CTkEntry(master=frameregister, placeholder_text="Firstname")
        fname_entry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        # Email
        email_entry = customtkinter.CTkEntry(master=frameregister, placeholder_text="Email")
        email_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        # Pseudo
        pseudo_entry = customtkinter.CTkEntry(master=frameregister, placeholder_text="Pseudonym")
        pseudo_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
        # Mot de passe
        passwd_entry = customtkinter.CTkEntry(master=frameregister, placeholder_text="Password")
        passwd_entry.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)
        # Bouton d'inscription
        register_btn = customtkinter.CTkButton(master=frameregister, text="Register", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=lambda : self.database.addUser(name_entry.get(), fname_entry.get(), email_entry.get(), pseudo_entry.get(), passwd_entry.get(), window))
        register_btn.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def send(self):
        self.msg_to_send = f"{self.msg_entry.get()}\n"
        self.listbox.insert(END, self.msg_to_send)
        # self.msg_field.insert(INSERT, self.msg_to_send)
        self.msg_entry.delete("0", "end")
        self.msg_field.config(state="normal")
        self.msg_field.config(state="disabled")
        self.msg_field.yview("end")

        # thread pour l'envoi de messages
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

        # print(self.msg_entry.get())
    
    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.pseudo.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.listbox.config(state=NORMAL)
                    self.listbox.insert(END,
                                        message+"\n\n")
                    
                    # inserer le message dans le champs dédié
                    self.msg_field.config(state="normal")
                    self.msg_field.insert(INSERT, message)

                    self.listbox.config(state=DISABLED)
                    self.listbox.see(END)

                    self.msg_field.config(state="disabled")
                    self.msg_field.yview("end")
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occurred!")
                # client.close()
                break
# function to send messages
    def sendMessage(self):
        # self.msg_field.config(state="disabled")
        # self.listbox.config(state=DISABLED)
        sent_time = strftime("%d/%m/%Y %H:%M")
        while True:
            message = (f"{self.pseudo}  {sent_time}:\n{self.msg_to_send}")
            self.listbox.insert(END, message)
            client.send(message.encode(FORMAT))
            # client.send(message.encode(FORMAT))
            break

if __name__ == "__main__":
    app = App()
    
# revoir et finaliser les threading 
# classes client et server 