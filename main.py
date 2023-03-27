from tkinter import *
import customtkinter
import tkinter.scrolledtext
from database import *
# from classes.server import *
# from classes.client import *

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
        self.root.mainloop()
        # fermeture du curseur utilisé depuis la bdd
        self.database.cursor.close()
    
    # méthode pour ouvrir la fenêtre principale de l'app myDiscord
    def main(self):
        self.gui = customtkinter.CTk()
        self.gui.geometry("600x600")
        self.gui.iconbitmap("img/chatking.ico")
        self.gui.title(f"ChatKing - logged in as {self.pseudo}")
        self.gui._set_appearance_mode("dark")

        # # instancier un objet server
        # self.client = Client(self.pseudo)

        # receive_thread = Thread(target=self.client.receive)
        # receive_thread.start()

        msg_frame = Frame(self.gui)
        my_msg = StringVar()
        my_msg.set("Type here.")
        # scrollbar = Scrollbar(msg_frame)

        msg_field = tkinter.scrolledtext.ScrolledText(msg_frame, height=25, width=50, bg="grey")
        # scrollbar.pack(side=RIGHT, fill=Y)
        # msg_field.pack(side=LEFT, fill=BOTH)
        msg_field.config(state="disabled")
        msg_field.pack()
        msg_frame.pack()

        msg_entry = Entry(self.gui, textvariable=my_msg)
        # msg_entry.bind("<Return>", "send")
        msg_entry.pack()
        send_btn = Button(self.gui, text="Send", command="send")
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
        register_top = Toplevel()
        register_top.geometry("300x300")
        register_top.title("Register")
        # Définition de la compostion de la fenête register 
        #
        name_label = Label(register_top, text="Name:")
        name_label.pack()
        name_entry = Entry(register_top, justify="center")
        name_entry.pack()
        fname_label = Label(register_top, text="Firstname:")
        fname_label.pack()
        fname_entry = Entry(register_top, justify="center")
        fname_entry.pack()
        email_label = Label(register_top, text="Email:")
        email_label.pack()
        email_entry = Entry(register_top, justify="center")
        email_entry.pack()
        pseudo_label = Label(register_top, text="Pseudo:")
        pseudo_label.pack()
        pseudo_entry = Entry(register_top, justify="center")
        pseudo_entry.pack()
        passwd_label = Label(register_top, text="Password:")
        passwd_label.pack()
        passwd_entry = Entry(register_top, justify="center")
        passwd_entry.pack()
        submit_btn = Button(register_top, text="Submit", command=lambda : self.database.addUser(name_entry.get(), fname_entry.get(), pseudo_entry.get(), email_entry.get(), passwd_entry.get(), register_top))
        submit_btn.pack()

    def send(self):
        pass

if __name__ == "__main__":
    app = App()
    
# revoir et finaliser les threading 
# classes client et server 