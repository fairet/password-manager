import json
import os
import hashlib

import tkinter as tk
import customtkinter as ctk

from modules.encryption import *
from datetime import datetime as dt

class Main:
    # def parse(self, username: str):
    #     #TODO: Encryption, file_to: str, master_key
        
    #     try:
    #         with open('passwords/usernames.json', 'r') as file_with_usernames:
    #             usernames_as_data = json.load(file_with_usernames)
        
    #         return usernames_as_data['usernames'][username]
    #     except KeyError:
    #         print("[INFO] There's no such username")
    def __init__(self):
        pass

    # def parse(self, website: str):
    #     #TODO: Encryption, file_to: str, master_key
        
    #     try:
    #         with open('passwords/usernames.json', 'r') as file_with_usernames:
    #             usernames_as_data = json.load(file_with_usernames)
        
    #         return usernames_as_data['usernames'][username]
    #     except KeyError:
    #         print("[INFO] There's no such username")
    # def parse_data(self):
    #     main = Main()
    #     website = self._entry_website.get()  # Получите введенный веб-сайт

    #     credentials = main.get_credentials(website)

    #     # Обновите self._label с данными
    #     self._label.configure(text=credentials)

    def get_credentials(self, website):
        try:
            with open('data/hashed_passwords.json', 'r') as hashed_passwords_file:
                hashed_passwords_data = json.load(hashed_passwords_file)

            if website in hashed_passwords_data.get("websites", {}):
                login_password_hash = hashed_passwords_data["websites"][website]
                login, password_hash = login_password_hash.split(':')

                password = self.decrypt_sha1(password_hash)

                return f"Login: {login}, Password: {password} for {website}"
            else:
                return "Website not found"
            
        except Exception as e:
            return str(e)
        
    def decrypt_sha1(self, sha1_hash):
        
        hashed = hashlib.sha1_hash.encode()
        # Допишите код для расшифровки хэша SHA-1 (ваша логика расшифровки)
        # В этом примере предполагается, что пароль хранится в открытом виде
        return sha1_hash
    
    def master_parse(self):
        try:
            with open('data/master_key.json', 'r') as file_with_master:
                master_key = json.load(file_with_master)
            return master_key["master_key"]["hex"]
        
        except KeyError:
            with open(f'logging/error.log', 'a') as file:
                    file.write(f"\n[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] Succesful Login")
                    print(f"[FAIL] Master Key is wrong: logging/error.log")

    def initialize(self):
        try:
            os.makedirs(name="passwords", exist_ok=True)
            
        except Exception as e:
        # TODO: logging
            return(str(e))

            # now = dt.now().strftime("%H_%M_%S")

            # try:
                
            #     os.makedirs(name=f"{now}")
    
            #     with open(f'{now}/logging.log', 'w') as file:
            #         file.write(f"[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] File is exists, all is ok")
            #         print(f"[INFO] A log file was created: {now}/logging.log")
            
            # except Exception as e:
            #     return(str(e))
        
    
    def check_master(self, master_key):
        
        hash_object = hashlib.sha1(master_key.encode()) 
        inputed_master_hex = hash_object.hexdigest()

        master_key_hex = self.master_parse()
        
        return master_key_hex == inputed_master_hex


class LoginApp(ctk.CTk):

    def __init__(self):
        #TODO: self.iconbitmap(/path/to/ico.ico)
        super().__init__()

        self.title("Login to Password-Manager")
        self.geometry("700x650")
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(self,
                                  height=600, 
                                  width=500,
                                  corner_radius=10)
        self.frame.pack(pady=40,
                        padx=20)
        frame = self.frame

        self.input_master = ctk.CTkEntry(frame,
                                         width=385,
                                         height=56,
                                         
                                         state="readonly",
                                         placeholder_text="Enter the master",
                                         corner_radius=10
                                         )
        self.input_master.place(rely=0.425,
                                relx=0.125)

        
        self.button = ctk.CTkButton(frame,
                                    width=385,
                                    height=56,

                                    command=lambda: self.check_master_ui(self.input_master.get()),

                                    text="Login",
                                    font=("Century Gothic", 28),
                                    corner_radius=10,
                                    anchor=tk.CENTER)
        
        self.button.place(rely=0.55,
                          relx=0.125)
        
        self.label_info = ctk.CTkLabel(frame,
                                       width=140,
                                       height=56,

                                       text="Master Password",
                                       font=("Century Gothic", 32),
                                       text_color=None,
                                       corner_radius=10,
                                       anchor=tk.CENTER)
        self.label_info.place(rely=0.25,
                              relx=0.25)
    
    def check_master_ui(self, master_key):

        main = Main()

        
        if main.check_master(master_key) == True:

            with open(f'logging/logging.log', 'a') as file:
                    file.write(f"\n[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] Succesful Login")
                    print(f"[SUCCESS] User with succesful Master Key: logging/success.log")

            self.withdraw()
            main_app = MainApp()
            main_app.mainloop()
        else:

            # now = dt.now().strftime("%H_%M_%S")
            self.label_info.configure(text="Wrong Master", text_color="red")
            self.label_info.place_configure(relx=0.255)
            with open(f'logging/errors.log', 'a') as file:
                    file.write(f"\n[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] Wrong Master")
                    print(f"[FAIL] User with wrong Master_Key: logging/errors.log")




class MainApp(ctk.CTk):
    def __init__(self):
        """
        Initialization MainApp
        :type ctk.CTk
        :rtype None
        """
        super().__init__()

        self.geometry("700x650")
        self.resizable(False, False)
        self.title("Password Manager")

        self._frame = ctk.CTkFrame(self,
                                  height=600, 
                                  width=500,
                                  corner_radius=10)
        self._frame.pack(pady=40,
                        padx=20)
        frame = self._frame

        self._label = ctk.CTkLabel(frame,
                                   width=140,
                                   height=56,
                                   
                                   text="Take a Website",
                                   font=("Century Gothic", 32),
                                   corner_radius=10,
                                   anchor=tk.CENTER
                                   )
        self._label.place(rely=0.125,
                          relx=0.25)
        
        self._button = ctk.CTkButton(frame,
                                     width=140,
                                     height=56,
                                     
                                     text="Username and Password",
                                     command=lambda: self.parse_data(),
                                     font=("Century Gothic", 32),
                                     anchor=tk.CENTER)
        self._entry_website = ctk.CTkEntry(frame,
                                           width=385,
                                           height=56,

                                           placeholder_text="Enter the master",
                                           corner_radius=10)
        self._entry_website.place(rely=0.2,
                                  relx=0.25)

    def parse_data(self):
        #TODO: Another output credentials
        main = Main()
        website = self._entry_website.get() 

        credentials = main.get_credentials(website)

        self._label.configure(text=credentials)


    # def parse_data(self, website):
    #     main = Main()