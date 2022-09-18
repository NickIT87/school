
from ctypes import cast
from distutils.log import error



def convert(n):
    try:
        return int(n)
    except:
        #raise ValueError("Invalid number")
        print("cannot convert n to int")
    finally:
        print("do something")


convert('12')