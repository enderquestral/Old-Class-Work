import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') # Was 350 x 280
    c.grid()
    # Create the x-axis.
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    # Create the y-axis.
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    # Plot the points.
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

# Constants: setting these values controls the parameters of your experiment.
injurycost     = 10   # Cost of losing a fight  
displaycost    = 1   # Cost of displaying between two passive birds  
foodbenefit    = 8   # Value of the food being fought over   
init_hawk      = 0
init_dove      = 0
init_defensive = 0
init_evolving  = 150    #If the amount of evolving birds at the end is LESS than 100, after going though simulation, it tends to clump as more of a hawk?

########
# Your code here
class World():
    def __init__(self):
        self.listofexistingbirds = []
    def update(self):
        for i in self.listofexistingbirds: 
            i.update()
    def free_food(self, numfreefood):
        #awards out food, numfreefood times
        #Each award of free food is done by picking a random bird in the birdlist and having that bird eat
        #(Each choice of bird should be made independent of the others---it is possible a bird will get free food multiple times in a single free_food call if the bird is lucky.)
        i = 0
        while i < numfreefood:
            #pick out random number from 0 to length of list of existing birds -1. Bird at that index gets food.
            luckybird = random.randint(0, len(self.listofexistingbirds) -1)
            luckybird = self.listofexistingbirds[luckybird] 
            luckybird.eat()
            i +=1
    def conflict(self, numencounters):
        i = 0
        lenoflisttorandom = (len(self.listofexistingbirds) -1)
        while i < numencounters:
            birdfight1 = random.randint(0, lenoflisttorandom)
            birdfight2 = birdfight1
            while birdfight2 == birdfight1:
                birdfight2 = random.randint(0, lenoflisttorandom)
            birdfight1 = self.listofexistingbirds[birdfight1]
            birdfight2 = self.listofexistingbirds[birdfight2]
            birdfight1.encounter(birdfight2)
            i += 1
    def status(self):
        #count a number of birds of each species, print a summary of that info to terminal
        dictofbirds = {}
        i = 0
        while i < len(self.listofexistingbirds):
            birdtype = self.listofexistingbirds[i]
            birdtype = birdtype.species
            if birdtype in dictofbirds:
                dictofbirds[birdtype] = dictofbirds[birdtype] +1
            else:
                dictofbirds.update({birdtype : 1})
            i +=1
        print(str(dictofbirds))
    def evolvingPlot(self):
        #plot takes x,y vals, which are lists. 
        #x is the weight of a bird, y is aggressiveness of same bird
        xvals = []
        yvals = []
        
        for i in self.listofexistingbirds: #try while loop?
            if i.species == "Evolving":
        #i = 0
        #while i < len(self.listofexistingbirds):
        #    bird = self.listofexistingbirds[i]
        #    if bird.species == "Evolving":
                xvals.append(i.weight) 
                yvals.append(i.aggression)
        #    i +=1  

        plot(xvals, yvals)
    


class Bird():
    """docstring for Bird
    Each bird starts with 100 health
    If bird eats health goes up, injured health goes down
    Birds lose small amount of health per unit of time (normal rate of burning calories)
    Health == 0 > Death. Health >=200, bird reproduces, health goes down by 100, new bird is created

    """
    def __init__(self, worldarg):
        worldarg.listofexistingbirds.append(self) 
        self.health = 100
        self.currentworld = worldarg
    def eat(self):
        self.health += foodbenefit
    def injured(self):
        self.health -= injurycost
    def display(self):
        self.health -= displaycost
    def die(self):
        self.currentworld.listofexistingbirds.remove(self)
    def update(self):
        #represents one unit of time passing
        self.health -= 1 #calories being burned
        if self.health <= 0:
            self.die()

class Dove(Bird):
    species = "Dove"
    """docstring for Dove"""
    def update(self):
        Bird.update(self)
        if self.health >= 200:
            Dove(self.currentworld)
            self.health -= 100
    def defend_choice(self):
        #"Asks" the brid if it will defend itself if another bird finds it with Food
        #Doves never will
        return False
    def encounter(self, otherbird):
        #other bird is a bird that already found food
        #use otherbirds defend_choice to find out if the other bird will defend itself
        #If other bird defends, dove runs away, no effect on dove, other bird eats.
        #If other bird does not defend, both birds should desplay, random of the two should get food
        otherchoice = otherbird.defend_choice()
        if otherchoice: #if true
            #Dove runs
            otherbird.eat()
        else: #otherbird does not defend
            self.display()
            otherbird.display()
            coin = random.randint(0, 1) #0, other bird gets it. 1, this bird gets it.
            if coin == 0:
                otherbird.eat()
            else:
                self.eat()

class Hawk(Bird):
    species = "Hawk"
    """docstring for Hawk"""
    def update(self):
        Bird.update(self)
        if self.health >= 200:
            Hawk(self.currentworld)
            self.health -= 100
    def defend_choice(self):
        #"Asks" the brid if it will defend itself if another bird finds it with Food
        #Hawks always will
        return True
    def encounter(self, otherbird):
        #other bird is a bird that already found food
        #use otherbirds defend_choice to find out if the other bird will defend itself
        #If other bird does not defend, hawk will always eat. 
        #If other bird does defend, two fight with random winner. Winner eats, loser is injured.
        otherchoice = otherbird.defend_choice()
        if otherchoice: #would defend, two fight
            coin = random.randint(0, 1) #0, other bird gets it. 1, this bird gets it.
            if coin == 0:
                otherbird.eat()
                self.injured()
            else:
                self.eat()
                otherbird.injured()
        else:
            self.eat()

class Defensive(Bird):
    """docstring for Defensive Birds

    This type of bird is "defensive"---if it finds food first, it will fight to defend it from other birds, 
    but it will not attack other birds to take their food. (It will, however, display in the way doves do.) 
    It also of course creates additional defensive birds when it reproduces. 
    """
    species = "Defensive"
    def update(self):
        Bird.update(self)
        if self.health >= 200:
            Defensive(self.currentworld)
            self.health -= 100

    def defend_choice(self): #It has found food, will fight to defend
        return True

    def encounter(self, otherbird): #Other bird has food, will not attack to take their food, will display
        otherchoice = otherbird.defend_choice()
        if otherchoice: #otherbird would defend
            otherbird.eat()
        else: #otherbird would not defend
            self.display()
            otherbird.display()
            coin = random.randint(0, 1) #0, other bird gets it. 1, this bird gets it.
            if coin == 0:
                otherbird.eat()
            else:
                self.eat()
        
class Evolving(Bird):
    #Only sometimes seems to do the 2-clump thing? Only if it's greater than 100 birds, which. hm. 
    #Also somehow seems to get caught in processing/infinite loop hell?
    species = "Evolving"
    def __init__(self, worldarg, parentweight, parentrage):
        #worldarg.listofexistingbirds.append(self) 
        #self.health = 100.0
        #self.currentworld = worldarg
        Bird.__init__(self, worldarg) 
        if parentweight is None:
            self.weight = random.uniform(1,3)
        else:
            changefactor = random.uniform(-0.1, 0.1)
            if parentweight + changefactor > 3.0:
                self.weight = 3.0
            elif parentweight + changefactor < 1.0:
                self.weight = 1.0
            else:
                self.weight =  parentweight + changefactor

        if parentrage is None:
            #self.aggression = random.random()
            self.aggression  = random.uniform(0.0, 1.0)
        else:
            self.aggression = parentrage + random.uniform(-0.05, 0.05)
            if self.aggression > 1.0:
                self.aggression = 1.0
            elif self.aggression < 0.0:
                self.aggression = 0.0


    def defend_choice(self):
        if random.randint(0,100) <= (100* self.aggression): #Will fight
            return True
        else: #will not fight
            return False

    def encounter(self, otherbird): 
        """We want heavier birds to win fights more often, 
        so we will say that if the two birds have weights w1 and w2, 
        then the probability of first bird winning is w1/(w1+w2)."""
        probabilitywin = (self.weight / (self.weight + otherbird.weight))
        otherchoice = otherbird.defend_choice()

        if self.defend_choice(): #Bird 1 will fight
            if otherchoice: #if bird 1 and bird 2 will both fight
                if random.randint(0,100) <= (100*probabilitywin):
                    self.eat()
                    otherbird.injured()
                else:
                    otherbird.eat()
                    self.injured()
            else: #If bird 1 will fight, but not bird 2?
                self.eat()
                #otherbird.injured()
                
        else: #Bird 1 will not fight
            if otherchoice: #bird 1 will not fight, bird 2 will
                otherbird.eat()
                #self.injured()
            else: #neither bird 1 nor bird 2 will fight
                self.display()
                otherbird.display()
                if random.randint(0,100) <= (100*probabilitywin):
                    self.eat()
                else:
                    otherbird.eat()

    def update(self):
        self.health -= (0.4 + (0.6 * self.weight)) #calories being burned
        if self.health <= 0:
            self.die()

        if self.health >= 200:
            Evolving(self.currentworld, self.weight, self.aggression)
            self.health -= 100

########


########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w,None,None)

for t in range(10000):
    w.free_food(10)
    w.conflict(50)
    w.update()
w.status()
w.evolvingPlot()    # This line adds a plot of evolving birds. Uncomment it when needed.


