import threading
import random
import time
#class Philosopher:
    # def Philosopher(self, arg):
    #     self.id = 0
    #     self.state = "none"
    #     self.priority = 0
    #     self.lChopstick = "none"
    #     self.rChopstick = "none"
    #
    # def getLChop():
    #     #how to access table Chopsticks
    #     print(lChopstick)
    #
    # def getRChop():
    #     #how to access table Chopsticks
    #     print(rChopstick)
    #
    # def eat():
    #     #how to access table Chopsticks
    #     print("eating")
#Commented syntax only works in python v.3.6
class Philosopher(object):

    def __init__(self, leftChopStick, rightChopStick):
        self.leftChopStick = leftChopStick  #what data type are these? I was using int
        self.rightChopStick = rightChopStick

    def doAction(self, action):
        # print(f'{threading.current_thread().getName()} {action}')
        print("Thread:%s\n%s" % (threading.current_thread().getName(), action))
        time.sleep(random.randint(1, 5)) #why random sleep time for various actions?

    def run(self):
        try:
            while True: #whats true? self?
                # self.doAction(f'{time.time()}: Thinking')
                self.doAction("%s: Thinking" % (time.time()))
                with self.leftChopStick:
                    # self.doAction(f'{time.time()}: Picked up left chopstick')
                    self.doAction("%s: Picked up left chopstick" %(time.time()))
                    with self.rightChopStick:
                        # self.doAction(f'{time.time()}: Picked up right chopstick - eating')
                        # self.doAction(f'{time.time()}: Put down right chopstick')
                        self.doAction("%s: Picked up right chopstick - eating" %(time.time()))
                        self.doAction("%s: Put down right chopstick" % (time.time()))
                    # self.doAction(f'{time.time()}: Put down left chopstick. Back to thinking')
                    self.doAction("%s: Put down left chopstick. Back to thinking" %(time.time()))
        except Exception as E:
            print(E)
