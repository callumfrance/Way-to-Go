from x import x

def printer():
   print("ipsem lorem")

print("runthis.py name is {}".format(__name__))

print("code begins when you say so")

# t = x(1,printer)
t = x(1, x.x_meth, args=(perpetualTimer,))
t.start()
