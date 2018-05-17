x = dict()
y = set()
z = list()

x1 = "12.2,13.3,14.4"
x2 = "12.2,13.3,14.4,descriptive"
x3 = "12.2,13.3,14.4,descriptive, description, by the way"
x1 = x1.split(",")
x2 = x2.split(",")
x3 = x3.split(",")
x4 = list([x3[0], x3[1], x3[2]])
x4.append(''.join(x3[3:]))

if __name__ == '__main__':
    print("length of dict() x is " + str(len(x)))
    print("length of set() y is " + str(len(y)))
    print("length of list() z is " + str(len(z)))
    print("len(x1) is " + str(len(x1)))
    print("len(x2) is " + str(len(x2)))
    print("len(x3) is " + str(len(x3)))
    print("len(x4) is " + str(len(x4)))
    print("x2[3:] is " + str(x2[3:]))
    print("x3[3:] is " + str(x3[3:]))
    print("x4[3] is " + str(x4[3]))

"""OUTPUT

length of dict() x is 0
length of set() y is 0
length of list() z is 0

"""
