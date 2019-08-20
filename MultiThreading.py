import threading
import time


class Hello(threading.Thread):      # Inherit Thread Class

    def run(self):                  # Override run method
        for i in range(5):
            print("Hello...")
            time.sleep(1)           # Delaying print statement


class Hii(threading.Thread):         # Inherit Thread Class

    def run(self):                   # Override run method
        for i in range(5):
            print("Hii...")
            time.sleep(1)            # Delaying print statement


t1 = Hello()
t2 = Hii()

t1.start()          # run method called
time.sleep(0.5)     # to pause
t2.start()          # run method called

t1.join()           # To maintain order of execution, in order of
t2.join()           # t1 thread --> t2 thread --> Main thread

print("Bye")        # Main thread print statement


