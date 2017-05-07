import random 
from matplotlib import pyplot as plt
import numpy as np
import time

class Horse( object ):
    def __init__(self, name, probForward, position=0):
        self.name = name
        self.probForward = probForward
        self.position = position
    
    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position
    
    def getProbForward(self):
        return self.probForward
        
    def move(self, dist):
        self.position += dist
        
    def takeStep(self):
        if random.random() < self.getProbForward():
            self.move(1)
        else:
            self.move(-1)

def createHorses(numHorses):
    horses = []
    for i in range(1,numHorses+1):
        name = 'Horse {:02d}'
        
        # Calculate the probability of moving forward
        probForward = .5 + .02*i
        
        # Create Horse
        horse = Horse(name.format(i), probForward)
        
        horses.append(horse)
    return horses

class Race( object ):
    
    def __init__(self, numHorses, finishPosition):
        self.horses = createHorses(numHorses)
        self.finish = finishPosition
    
    def getNumHorses(self):
        return len(self.horses)
    
    def getHorses(self):
        return self.horses
        
    def getHorseNames(self):
        names = []
        for horse in self.getHorses():
            names.append( horse.getName() )
            
        return names
    
    def getHorsePositions(self):
        positions = []
        for horse in self.getHorses():
            positions.append( horse.getPosition() )
        
        return positions
    
    def oneSecond(self):
        for horse in self.getHorses():
            horse.takeStep()
        
        return self.getHorses
    
    def raceFinished(self):
        for horse in self.getHorses():
            if horse.getPosition() >= self.finish:
                return True
            else:
                continue
    
    def showRace(self, ind, names, ax):
        ax.clear()
        ax.set_xticks(ind)
        ax.set_xticklabels(names, rotation='vertical')
        ax.set_ylim(-25,200)
        dep = self.getHorsePositions()
        
        ax.bar(ind, dep)
        ax.set_xlabel('Horse')
        ax.set_ylabel('Position (m)')
        plt.draw()
        plt.pause(.001)
        
    def simulateAndShow(self):
        # Set up plot objects
        plt.locator_params(axis='x', nticks=self.getNumHorses() )
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        names = self.getHorseNames()
        numHorses = self.getNumHorses()
        
        ind = np.arange(numHorses)
        
        # Show and simulate race
        self.showRace(ind, names, ax)
        while not self.raceFinished():
            self.oneSecond()
            self.showRace(ind, names, ax)
        
        # Determine winner
        for horse in self.getHorses():
            if horse.getPosition() == self.finish:
                print(horse.getName() + " won!")
                return horse
    
    def simulate(self):
        while not self.raceFinished():
            self.oneSecond()
        
        # Determine winner
        for horse in self.getHorses():
            if horse.getPosition() == self.finish:
                # print(horse.getName() + " won!")
                return horse

def calcProb(numHorses, finishPosition, numTrials):
    results = {}
    race = Race(numHorses, finishPosition)
    # Populate dictionary of results
    for name in race.getHorseNames():
        results[name] = 0
    
    # Run simulations
    for i in range( numTrials ):
        race = Race(numHorses, finishPosition)
        winner = race.simulate()
        results[winner.getName()] += 1
    
    # See results of races
    # for horse in sorted(results):
    #     print("%s: %s" % (horse, results[horse]) )
    
    payouts = {}
    for horse in results.keys():
        try:
            payouts[horse] = numTrials/results[horse]
        except ZeroDivisionError:
            payouts[horse] = float('inf')
    
    return payouts
    
### Main Body

numHorses = 20
finishPosition = 200
numTrials = 1000000

# Show race
race = Race(numHorses, finishPosition)
race.simulateAndShow()

# Calculate betting
# payouts = calcProb(numHorses,finishPosition,numTrials)
# 
# for horse in sorted(bets):
#     print("%s: %s" % (horse, payouts[horse]) )

