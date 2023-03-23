from tkinter import *
import tkinter
import customtkinter
from classes.chatking import *

class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
        self.root.title("ChatKing - Login")
        self.root.iconbitmap("img/chatking.ico")
        customtkinter.set_appearance_mode("dark")
        # Dimensions
        self.appwidth = 650
        self.appheight = 400
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.x = (self.screenwidth / 2) - (self.appwidth / 2)
        self.y = (self.screenheight / 2) - (self.appheight / 2)
        self.root.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')

    # Démarrer ChatKing
    def start(self):
        framelogin = customtkinter.CTkFrame(master=self.root)
        framelogin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Pseudo
        self.pseudo = customtkinter.CTkEntry(master=framelogin, placeholder_text="Pseudo")
        self.pseudo.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        # Password
        self.password = customtkinter.CTkEntry(master=framelogin, placeholder_text="Password")
        self.password.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        # Bouton Login
        login_btn = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Login", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.login)
        login_btn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        # Bouton Register
        register = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Register", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.register)
        register.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.root.mainloop()
        
    # Canal par défaut
    # def chanel(self):
    #     test = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Test")
    #     test.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    # Se connecter
    def login(self):
        self.psd = self.pseudo.get() # pseudo
        self.pwd = self.password.get() # password
        if self.psd:
            if self.pwd:
                print('Valide')
                print(self.psd)
                print(self.pwd)
                # Supprime la fenêtre de Login
                self.root.destroy() 
                # Affiche le canal par défaut après connexion
                server = ChatKing()
                server.start()
            else:
                print('Denied')
        else:
            print('Denied')

    # S'inscrire
    def register(self):
        window = customtkinter.CTkToplevel(self)
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
        name = customtkinter.CTkEntry(master=frameregister, placeholder_text="Name")
        name.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # Prénom
        firstname = customtkinter.CTkEntry(master=frameregister, placeholder_text="Firstname")
        firstname.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        # Email
        email = customtkinter.CTkEntry(master=frameregister, placeholder_text="Email")
        email.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Mot de passe
        password = customtkinter.CTkEntry(master=frameregister, placeholder_text="Password")
        password.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        # Bouton d'inscription
        register_btn = customtkinter.CTkButton(master=frameregister, text="Register", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"))
        register_btn.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

if __name__ == "__main__":
    chatking = Login()
    chatking.start()