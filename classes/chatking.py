from tkinter import *
import tkinter
import customtkinter
from main import *

class ChatKing(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
        self.root.title("ChatKing - Channel by default")
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
        # Entry message
        self.message = customtkinter.CTkEntry(master=self.root, placeholder_text="Envoyer un message", width=180)
        self.message.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        # Bouton envoi message
        message_btn = customtkinter.CTkButton(master=self.root, width=80, height=32, border_width=0, corner_radius=8, text="Envoyer", command=self.send_message)
        message_btn.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)
        # Bouton Déconnexion
        disconnect_btn = customtkinter.CTkButton(master=self.root, width=80, height=32, border_width=0, corner_radius=8, text="Se déconnecter", fg_color="red", hover_color="red", command=self.disconnect)
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
        # Login.start()

# channel = ChatKing()
# channel.start()