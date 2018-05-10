from decimal import *

x = Decimal('3.3') # converts a perfect string to a decimal
y = Decimal(4.4) # converts a 'non-perfect' (binary) float to decimal
z = Decimal("3.3") # also converts a perfect string to a decimal

"""All x, y, z, are valid Decimals"""
print("x is {} of type {}".format(x, type(x)))
print("y is {} of type {}".format(y, type(y)))
print("z is {} of type {}".format(z, type(z)))

"""Decimals are seamless with floats."""
if 3.2 < x:
    print("3.2 < x")

"""Decimals are not floats."""
if isinstance(x, float):
    print("x is a float")

if isinstance(y, float):
    print("y is a float")

"""An example of regular float arithmetic in Python"""
print("3.3+(10/3) = {}".format(3.3+(10/3)))

"""Rounding can solve this... but it leaves trailing zeros"""
print("round(3.3, 2)+round((10/3), 2) = {}"
      .format(round(3.3, 2)+round((10/3), 2)))

"""Decimals produce perfect results..."""
print("x+z = {}".format(x+z))

"""... but only if the Decimal was made from a string, not from floats"""
print("x+y = {}".format(x+y))
print("round(x+y, 2) = {}".format(round(x+y, 2)))
