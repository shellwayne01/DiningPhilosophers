import threading
# from DinnerTime import DinnerTime
from PhilosopherV0 import Philosopher

if __name__ == '__main__':

    philosophers = [0 for _ in range(5)]
    chopSticks = [0 for _ in range(5)]
    threadData = threading.local()
    threadData.threadsStatus = {}


    for i in range(len(chopSticks)):
        chopSticks[i] = threading.Lock() # lock ensures that no two threads will use the same chopstick

    for i in range(len(philosophers)):
        leftChopStick = chopSticks[i]
        rightChopStick = chopSticks[(i+1) % len(chopSticks)]

        if i == len(philosophers) - 1:
            philosophers[i] = Philosopher(rightChopStick, leftChopStick)
        else:
            philosophers[i] = Philosopher(leftChopStick, rightChopStick)  #Can use a circular array to optimize this

        t = threading.Thread(target=philosophers[i].run, name=f'Philosopher {i+1}') #target here is a runnable class
        # name = "Philosopher %s" % (i+1)
        # t = threading.Thread(target=philosophers[i].run, name=name)
        t.start()

        if t.isAlive():
            t.state = "new"
            threadData.threadsStatus[f'{t.name}'] = t.state

        print(threadData.threadsStatus)

        # Control + C to quit and end threads
