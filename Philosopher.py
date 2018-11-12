import threading
import random
import time

#Older version of Philosopher class
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
    #     print("Now eating")
    # def think():
    #     #how to access table Chopsticks
    #     print("Now thinking")

#Improved version of Philosopher class
#Commented syntax is the same code in Python v.2.7
class Philosopher(object):

    def __init__(self, leftChopStick, rightChopStick):
        self.leftChopStick = leftChopStick
        self.rightChopStick = rightChopStick

        #Thread gets a random time to complete their actions after getting both chopsticks
    def doAction(self, action):
        print(f'{threading.current_thread().getName()} {action}')
        # print("Thread:%s\n%s" % (threading.current_thread().getName(), action))
        time.sleep(random.randint(1, 2))

    def run(self):
        try: #context manager -- "with"
            while True:
                self.doAction(f'{time.time()}: Thinking')
                # self.doAction("%s: Thinking" % (time.time()))
                with self.leftChopStick:
                    self.doAction(f'{time.time()}: Picked up left chopstick')
                    # self.doAction("%s: Picked up left chopstick" %(time.time()))
                    with self.rightChopStick:
                        self.doAction(f'{time.time()}: Picked up right chopstick - eating') #can break this up
                        self.doAction(f'{time.time()}: Put down right chopstick')
                        # self.doAction("%s: Picked up right chopstick - eating" %(time.time()))
                        # self.doAction("%s: Put down right chopstick" % (time.time()))
                    self.doAction(f'{time.time()}: Put down left chopstick. Back to thinking')
                    # self.doAction("%s: Put down left chopstick. Back to thinking" %(time.time()))
        except Exception as E:
            print(E)
