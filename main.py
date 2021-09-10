# type: ignore
import sys
from src.bot import main


if __name__ == '__main__':
    print("In test_py/main.py", sys.path, end="\n\n")
    main.hello()

