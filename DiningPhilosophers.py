import threading
from Philosopher import Philosopher

if __name__ == '__main__':

    philosophers = [0 for _ in range(5)] #fills array with five 0s as placeholders
    chopSticks = [0 for _ in range(5)]

    for i in range(len(chopSticks)): #sets up locking ability for threads when they use chopsticks
        chopSticks[i] = threading.Lock()

    for i in range(len(philosophers)):
        leftChopStick = chopSticks[i]
        rightChopStick = chopSticks[(i+1) % len(chopSticks)]

        if i == len(philosophers) - 1:
            philosophers[i] = Philosopher(rightChopStick, leftChopStick)
        else:
            philosophers[i] = Philosopher(leftChopStick, rightChopStick)

        t = threading.Thread(target=philosophers[i].run, name=f'Philosopher {i+1}') #creates thread of runnable class
        t.start()
