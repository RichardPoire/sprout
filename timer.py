import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + "started")

    tLock.acquire()
    print(name + " has the lock", threading.current_thread())

    while repeat>0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1

    tLock.release()
    print(name + ' released the lock')

    print("Timer: " + name + " completed")

def Main():
    t1 = threading.Thread(target = timer, args = ("Timer1", 1, 5))
    t2 = threading.Thread(target = timer, args = ("Timer2", 2, 5))

    t1.start()
    t2.start()

    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == '__main__':
    Main()
