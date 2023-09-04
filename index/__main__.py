

from main import Main
from modules.log.logging import *

if __name__ == "__main__":
    main = Main
    main.initialize(Main)
    print(main.parse())
    