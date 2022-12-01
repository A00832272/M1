import mesa
import math
import random
from agent import RobotAgent
from box import BoxAgent


class BoxModel(mesa.Model):

    def __init__(self, N, width, height, K):
        self.boxCoords = [] 
        self.num_agents = N
        self.num_box = K
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        #setup agents on grid
        for i in range(self.num_agents):
            a = RobotAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (0,i))

        #setup boxes
        for i in range(self.num_box):
            
            b = BoxAgent(i + self.num_box, self)
            self.schedule.add(b)
            z = self.grid.find_empty()
            self.boxCoords.append(z)
            self.grid.place_agent(b, (z))

    def step(self):
        self.schedule.step()
