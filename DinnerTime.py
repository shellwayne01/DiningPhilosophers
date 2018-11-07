class DinnerTime(object): #change the name to something else
    """docstring for ."""
    #Variables
    philosophers = [] #fill with Philosopher objects
    forks = []  #filled with string for now. How do we know the order of the forks?
    idCounter = 0

    def __init__(self, numP):
        if numP == 5:
            for person in range(numP):
                addPerson()
                fork = "fork"
                fork.append(forks)
        #start thread execution on all philosophers

    def addPerson():
        idCounter = idCounter+1
        person = Philosopher()
        person.id = idCounter
        person.lFork = forks[ ((idCounter*2) - 1) % forks.count()]
        person.rFork = forks[idCounter] #modulus
        print ("New Person added to the dining table person" %(person))
        philosophers.append(person)

    def tableStatus():
        print("There are %s philosophers at the dining table." % (philosophers.count())
        for person in philosophers:
            print("\nPhilosopher %s: \nstatus = %s\nleft fork= %s\nright fork = %s" % (person.id, person.state, person.lFork, person.rFork))
