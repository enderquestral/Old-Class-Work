#when you're testing for objects, make some complicated multi-line tests

class Car:
#Somewhere during testing your car was .001 or more miles out of the expected location.
    def __init__(self, mpg, tank, money):
#    The constructor should initialize instance variables to carry these values, 
#along with the x and y position where the car sits (initially at the origin), 
#along with how much fuel is in the tank (initially, make it a full tank).
        self.money = money
        self.mpg = mpg
        self.tanksize = tank
        self.fuelleft = tank
        self.xpos = 0.0
        self.ypos = 0.0

    def driveTo(self, newxpos, newypos):
        #make it so that even if you go back you spend gas...
        newspot = ((self.xpos-newxpos)**2 + (self.ypos - newypos)**2)**0.5
        # newspot / miles per gallon, to see how much of a gallon was used?
        #drove 2 miles, 5 miles per gallon, 3 gallons in tank...


        if (newspot / self.mpg) < self.fuelleft:
            self.fuelleft -= abs(newspot / self.mpg)
            self.xpos = newxpos
            self.ypos = newypos
            return True
        else:
            return False

    def getGas(self):
        return self.fuelleft

    def getLocation(self):
        return [self.xpos, self.ypos]

    def getToFill(self):
        return self.tanksize - self.fuelleft
    def getMoney(self):
        return self.money
    def pay(self, owed):
        self.money = self.money - owed
    def refill(self):
        self.fuelleft =  self.tanksize

class GasStation:
    def __init__(self, xpos, ypos, dpg): #dpg is dollars per gallon of gas
        self.xpos = xpos
        self.ypos = ypos
        self.dollarspergallon = dpg

    def refillCar(self, car):
        #checks to make sure car is at gas station
        #checks to see if car has enough money to fill the tank
        #if those checks fail, return false. Else, it should fill up the cars tank, updating the 
        #amount of money the car has and the amount of gas accordingly and return True
        #The method should fill cars that are very close to the gas station, 
        #not just exactly at the gas station. 
        #Consider a car to be close enough to the gas station to refuel if the distance between them 
        #is no more than .001 mile

        stationspot =((self.xpos)**2 + (self.ypos)**2)**0.5
        carspot = car.getLocation()
        carspot = ((carspot[0])**2 + (carspot[1])**2)**0.5
        if abs(stationspot-carspot) <= 0.001:
            if car.getMoney() > (car.tanksize - car.fuelleft)*self.dollarspergallon:
                car.pay((car.tanksize - car.fuelleft)*self.dollarspergallon)
                car.refill()
            else:
                return False
        else:
            return False

class Taxi(Car):
    def __init__(self, mpg, tank, money):
        self.money = money
        self.mpg = mpg
        self.tanksize = tank
        self.fuelleft = tank
        self.xpos = 0.0
        self.ypos = 0.0
        self.haspassanger = False
        self.mileswithpassanger = 0

    def pickup(self):
        if self.haspassanger is False:
            self.haspassanger = True
            #from here on, track how many miles until dropoff
        else:
            return False

    def driveTo(self, newxpos, newypos): 
         #IMPORTANT
        #distance = 0. for i in oberved,
        if self.haspassanger:

            #self.mileswithpassanger += abs((self.xpos-newxpos)+ (self.ypos - newypos))
            self.mileswithpassanger += abs(((self.xpos-newxpos)**2 + (self.ypos - newypos)**2)**0.5)
            Car.driveTo(self, newxpos, newypos)
        else:
            Car.driveTo(self, newxpos, newypos)

        self.xpos, self.ypos = newxpos, newypos

    def dropoff(self):
        if self.haspassanger:
            #taxi ending with wrong amount of money???
            self.money += (2 + (3*self.mileswithpassanger))
            self.haspassanger = False
            self.mileswithpassanger = 0
        else:
            return False

class Dispatcher:
    """docstring for Dispatcher"""
    def __init__(self):
        #Constructor takes in no information?
        self.taxilist = []
    
    def hire(self, Taxi):
        self.taxilist.append(Taxi) 

    def hail(self, xpospass, ypospass): #xpos and ypos of passanger

#    Running the code led to this error: 
#Traceback (most recent call last): File "test_Dispatcher.py", line 89, in <module> hw3 = hw_disp.hail(0,0) 
#File "/home/autograde/autolab/hw6.py", line 137, in hail lowestdistance = ((listofpossibletaxis[0].xpos - xpospass)**2 + (listofpossibletaxis[0].ypos - ypospass)**2 )**0.5 
#IndexError: list index out of range
        listofpossibletaxis = []
        i = 0
        while i < len(self.taxilist):
            potentialcab = self.taxilist[i] #Error: list indices must be integers or slices, not Taxi
            if potentialcab.haspassanger == False:#check if a cab does not already have a passanger
                #Check if the cab has enough gas to get to the place
                newspot = ((potentialcab.xpos-xpospass)**2 + (potentialcab.ypos - ypospass)**2)**0.5
                if (newspot / potentialcab.mpg) < potentialcab.fuelleft:
                    listofpossibletaxis.append(potentialcab)
            i+=1
        
        i=0
        if len(listofpossibletaxis) <1:
            return None
        #Of those taxis in its fleet that can perform the pick-up, the dispatcher should choose the one that's closest to the passenger, ask it to driveTo that passenger's location, and then have it perform the pickup.
        else:
            lowestdistance = ((listofpossibletaxis[0].xpos - xpospass)**2 + (listofpossibletaxis[0].ypos - ypospass)**2 )**0.5
            chosencab = listofpossibletaxis[0]
            while i < len(listofpossibletaxis):
                potentialcab = listofpossibletaxis[i]
                newspot = ((potentialcab.xpos-xpospass)**2 + (potentialcab.ypos - ypospass)**2)**0.5
                if newspot < lowestdistance:
                    chosencab = listofpossibletaxis[i]
                i +=1

            chosencab.driveTo(xpospass, ypospass)
            chosencab.pickup()
            return chosencab
        #If a taxi meets all criteria, return which taxi was chosen. Else, return None

        
