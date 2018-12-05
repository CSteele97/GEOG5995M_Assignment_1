import random

# Create a new class called Agent
class Agent:
    def __init__(self,environment,agents):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.environment = environment
        self.store = 0
        self.agents = agents

# This function makes each x and y coordinate move either +1 or -1 based on a 
# random number        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

# This function makes the agents eat the environment around them by 10 if the 
# coordinates are greater than 10            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        if self.store >= 5000:
            self.move = 0

# This function makes agents search for close neighbours and share resources 
# with them         
            
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                average = sum / 2
                self.store = average
                agent.store = average

    def distance_between(self, agents):
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5
        