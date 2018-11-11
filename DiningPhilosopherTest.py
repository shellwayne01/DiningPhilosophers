import threading
import random
import time

class Philosopher(object):

    def __init__(self, leftChopStick, rightChopStick):
        self.leftChopStick = leftChopStick
        self.rightChopStick = rightChopStick

    def doAction(self, action, sleep):
        for i in range(sleep):
            print(f'{threading.current_thread().getName()} {action}')
            time.sleep(i)

    def run(self):
        try:
            while True:
                with self.leftChopStick:
                    self.doAction(f'{time.time()}: Picked up left chopstick', 1)
                    with self.rightChopStick:
                        self.doAction(f'{time.time()}: Picked up right chopstick', 1)
                        self.doAction(f'{time.time()}: Eating.', random.randint(5, 10))
                        self.doAction(f'{time.time()}: Put down right chopstick', 1)
                    self.doAction(f'{time.time()}: Put down left chopstick', 1)
                    self.doAction(f'{time.time()}: Is Full. Back to thinking', 1)
                    self.doAction(f'{time.time()}: Thinking', random.randint(1, 10))
        except Exception as E:
            print(E)

if __name__ == '__main__':

    philosophers = [0 for _ in range(5)]
    chopSticks = [0 for _ in range(5)]

    for i in range(len(chopSticks)):
        chopSticks[i] = threading.Lock()

    for i in range(len(philosophers)):
        leftChopStick = chopSticks[i]
        rightChopStick = chopSticks[(i+1) % len(chopSticks)]

        if i == len(philosophers) - 1:
            philosophers[i] = Philosopher(rightChopStick, leftChopStick)
        else:
            philosophers[i] = Philosopher(leftChopStick, rightChopStick)

        t = threading.Thread(target=philosophers[i].run, name=f'Philosopher {i+1}')
        t.start()
