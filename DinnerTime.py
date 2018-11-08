from Philosopher import Philosopher
class DinnerTime: #change the name to something else
    def __init__(self, numP):
        self.philosophers = [] #fill with Philosopher objects
        self.chopsticks = [] #filled with strings for now. How do we know the order of the chopsticks?
        self.idCounter = 0
        if numP == 5:
            for x in range(numP):
                chopstick = x
                self.chopsticks.append(chopstick)
            for person in range(numP):
                self.addPerson()1
        #start thread execution on all philosophers

    def addPerson(self):
        person = Philosopher()
        person.id = self.idCounter
        person.state = "none"
        person.priority = self.idCounter
        person.lChopstick = self.chopsticks[(self.idCounter - 1) % len(self.chopsticks)]
        person.rChopstick = self.chopsticks[self.idCounter]
        self.philosophers.append(person)
        print ("New Person added to the dining table.")
        self.idCounter += 1

    def tableStatus(self):
        print("There are %s philosophers at the dining table." % len(self.philosophers))
        for person in self.philosophers:
            print("\nPhilosopher %s: \nstatus = %s\nleft chopstick = %s\nright chopstick = %s\npriority = %s"
            % (person.id, person.state, person.lChopstick, person.rChopstick,person.priority))
