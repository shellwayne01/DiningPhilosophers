import threading
import random
import time
# from DinnerTime import DinnerTime
from Philosopher import Philosopher

# test = DinnerTime(5)
# test.tableStatus()

# test = Philosopher(4,0)
# test.run()

if __name__ == '__main__':

    philosophers = [0 for _ in range(5)]
    chopSticks = [0 for _ in range(5)]

    for i in range(len(chopSticks)):
        chopSticks[i] = threading.Lock()

    for i in range(len(philosophers)):
        leftChopStick = chopSticks[i]
        rightChopStick = chopSticks[(i+1) % len(chopSticks)]

        if i == len(philosophers) - 1:
            philosophers[i] = Philosopher(rightChopStick, leftChopStick) #review. Circular array is better
        else:
            philosophers[i] = Philosopher(leftChopStick, rightChopStick)

        # t = threading.Thread(target=philosophers[i].run, name=f'Philosopher {i+1}') #target here is a runnable class
        name = "Philosopher %s" % (i+1)
        t = threading.Thread(target=philosophers[i].run, name=name)
        t.start()
