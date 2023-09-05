import hashlib

from main import Main, LoginApp

main = Main
main.initialize(main)

if __name__ == "__main__":
    """7c4a8d09ca3762af61e59520943dc26494f8941b = 123456"""
    """cee98381dae85d39442876b94bb4453374270176 = mysuperpassword"""
    
    # hashed = hashlib.sha1(b'mysuperpassword')
    # print(hashed.hexdigest())
    login_app = LoginApp()
    login_app.mainloop()
    

    
    
    # for i in range(4):
    #     if i == 2:
    #         print(f"You have {i} attemps left")
    #     elif i == 3:
    #         print(f"You have {i - 2} attempts left")
    #     master = gp.getpass("Master: ")
    #     username = gp.getpass("Username: ")
    #     print(main.main(main, master, username))

    # print("\n[-] You have been blocked")
    # exit()
    
    