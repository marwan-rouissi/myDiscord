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
        customtkinter.set_appearance_mode("light")
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
        login_btn = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Login", command=self.login)
        login_btn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        # Bouton Register
        register = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Register", command=self.register)
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
        self.button_1 = customtkinter.CTkButton(master=window, text="open toplevel")
        self.button_1.pack(side="top", padx=20, pady=20)

if __name__ == "__main__":
    app = Login()
    app.start()