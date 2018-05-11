from event_test import perpetualTimer

class x(perpetualTimer):

    def __init__(self, t, hFunction):
        perpetualTimer.__init__(self, t, hFunction)

    def x_meth():
        print("this is the x_method")

print("x.py name is {}".format(__name__))

# def printer():
#    print("ipsem lorem")

# t = x(1,printer)
# t.start()
