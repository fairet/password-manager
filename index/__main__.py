import getpass as gp
from main import Main
# from modules.log.logging import *

if __name__ == "__main__":
    main = Main
    main.initialize(main)
    
    for i in range(4):
        if i == 2:
            print(f"You have {i} attemps left")
        elif i == 3:
            print(f"You have {i - 2} attempts left")
        master = gp.getpass("Master: ")
        username = gp.getpass("Username: ")
        print(main.main(main, master, username))

    print("\nYou have been blocked")
    exit()
    
    