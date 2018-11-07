from Philosopher import Philosopher
class DinnerTime: #change the name to something else
    def __init__(self, numP):
        self.philosophers = [] #fill with Philosopher objects
        self.forks = [] #filled with strings for now. How do we know the order of the forks?
        self.idCounter = 0
        if numP == 5:
            for x in range(numP):
                fork = x
                self.forks.append(fork)
            for person in range(numP):
                self.addPerson()
        #start thread execution on all philosophers

    def addPerson(self):
        person = Philosopher()
        person.id = self.idCounter
        person.state = "none"
        person.priority = self.idCounter
        person.lFork = self.forks[(self.idCounter - 1) % len(self.forks)]
        person.rFork = self.forks[self.idCounter]
        self.philosophers.append(person)
        print ("New Person added to the dining table.")
        self.idCounter += 1

    def tableStatus(self):
        print("There are %s philosophers at the dining table." % len(self.philosophers))
        for person in self.philosophers:
            print("\nPhilosopher %s: \nstatus = %s\nleft fork = %s\nright fork = %s\npriority = %s"
            % (person.id, person.state, person.lFork, person.rFork,person.priority))
