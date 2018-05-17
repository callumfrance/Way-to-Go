import threading

def f(id):
    print("thread function {}".format(id))
    return

if __name__ == '__main__':
    for i in range(3):
        print(str(i) + " 1")
        t = threading.Thread(target=f, args=(i,))
        # t = threading.Thread(f, i) # This does not work
        print(str(i) + " 2")
        t.start()
        print(str(i) + " 3")
