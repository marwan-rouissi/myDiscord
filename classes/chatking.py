from tkinter import *
import tkinter
import customtkinter
from main import *

class ChatKing(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
    # Démarrer ChatKing
    def start(self):
        self.root.title("ChatKing - Channel by default")
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
        # Entry message
        self.message = customtkinter.CTkEntry(master=self.root, placeholder_text="Envoyer un message", width=180)
        self.message.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        # Bouton envoi message
        message_btn = customtkinter.CTkButton(master=self.root, width=80, height=32, border_width=0, corner_radius=8, text="Envoyer", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.send_message)
        message_btn.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)
        # Bouton Déconnexion
        disconnect_btn = customtkinter.CTkButton(master=self.root, width=80, height=32, border_width=0, corner_radius=8, text="Se déconnecter", fg_color="#5700C8", hover_color="#5700C8", text_color="#FFE23F", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.disconnect)
        disconnect_btn.place(relx=0.88, rely=0.07, anchor=tkinter.CENTER)
        self.root.mainloop()

    # Canal par défaut
    # def chanel(self):
    #     test = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Test")
    #     test.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    # Envoi message
    def send_message(self):
        pass

    # Déconnexion
    def disconnect(self):
        self.root.destroy()
        new_window = customtkinter.CTk()
        new_window.iconbitmap("img/chatking.ico")
        framelogin = customtkinter.CTkFrame(master=new_window)
        framelogin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Pseudo
        pseudo = customtkinter.CTkEntry(master=framelogin, placeholder_text="Pseudo")
        pseudo.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        # Password
        password = customtkinter.CTkEntry(master=framelogin, placeholder_text="Password")
        password.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        # Bouton Login
        login_btn = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Login")
        login_btn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        # Bouton Register
        register = customtkinter.CTkButton(master=framelogin, width=120, height=32, border_width=0, corner_radius=8, text="Register", command=self.register)
        register.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        new_window.mainloop()
        # Login.start()

# channel = ChatKing()
# channel.start()