from decimal import *

x = Decimal('3.3')
y = Decimal(4.4)
z = Decimal("3.3")

print("x is {} of type {}".format(x, type(x)))
print("y is {} of type {}".format(y, type(y)))
print("z is {} of type {}".format(z, type(z)))

if 3.2 < x:
    print("3.2 < x")

if isinstance(x, Decimal):
    print("x is a Decimal")

if isinstance(y, Decimal):
    print("y is a Decimal")

if isinstance(x, float):
    print("x is a float")

if isinstance(y, float):
    print("y is a float")

print("{}".format(3.3+(10/3)))
print("{}".format(x+y))
print("{}".format(x+z))
