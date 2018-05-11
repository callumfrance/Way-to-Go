import threading
import itertools
import time
import sys

class Signal:
    go = True

    def supervisor(self):
        spinner = threading.Thread(target=spin,
                                args=('thinking!', self))
        print('spinner object:', spinner)
        spinner.start()
        result = slow_function()
        self.go = False
        spinner.join()
        return result

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(0.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))

def slow_function():
    time.sleep(3)
    return 42


def main():
    signal = Signal()
    result = signal.supervisor()
    print('Answer:', result)

if __name__ == '__main__':
    main()
