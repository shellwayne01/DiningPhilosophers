import threading
import random
import time

#Latest Version of Philosopher class
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
