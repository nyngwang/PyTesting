import sys
from ..bot.sib1 import f_sib1


def hello():
    print("In module1.py, sys.path=", sys.path, end="\n\n")
    f_sib1()
    
