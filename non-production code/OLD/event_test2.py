import threading
import time

def hello():
    print("hello, Timer")

if __name__ == '__main__':
    print("1")
    t = threading.Timer(3.0, hello)
    print("2")
    t.start()
    print("3")

""" OUTPUT:
1
2
3
hello, Timer

"""
