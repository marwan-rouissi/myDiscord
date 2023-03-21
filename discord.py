from tkinter import *
import tkinter
import customtkinter

class Discord(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
        self.root.title("My Discord")
        customtkinter.set_appearance_mode("light")
        # Dimensions
        self.appwidth = 650
        self.appheight = 400
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.x = (self.screenwidth / 2) - (self.appwidth / 2)
        self.y = (self.screenheight / 2) - (self.appheight / 2)
        self.root.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')

    # Démarrer Discord
    def start(self):
        # Pseudo
        self.pseudo = customtkinter.CTkEntry(master=self.root, placeholder_text="Pseudo")
        self.pseudo.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        # Password
        self.password = customtkinter.CTkEntry(master=self.root, placeholder_text="Password")
        self.password.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        # Bouton Login
        login = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Login", command=self.login)
        login.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Bouton Register
        register = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Register")
        register.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.root.mainloop()

    # Se connecter
    def login(self):
        self.psd = self.pseudo.get() # pseudo
        self.pwd = self.password.get() # password
        
        if self.psd:
            if self.pwd:
                print('Valide')
                print(self.psd)
                print(self.pwd)
            else:
                print('Denied')
        else:
            print('Denied')

    # S'inscrire
    def register(self):
        pass

if __name__ == "__main__":
    app = Discord()
    app.start()