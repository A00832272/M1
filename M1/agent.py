import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
"""
"""

class CleanerAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False, radius=1
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def cleanCell(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(self.pos) == 2:
            other_agent = self.random.choice(self.model.schedule.agents)
            if(other_agent == TrashAgent):
                other_agent.destroy += 1

    def step(self):
        self.cleanCell()
        self.move()


class TrashAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.destroy = 0

    def step(self):
        if (self.destroy >= 1):
            self.destroy(self)




class CleaningModel(mesa.Model):

    def __init__(self, NumCleaners, NumTrash, width, height):
        self.boxCoords = [] 
        self.num_agents = NumCleaners
        self.num_box = NumTrash
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        #setup agents on grid
        for i in range(self.num_agents):
            a = CleanerAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (1, 1))

        #setup boxes
        for i in range(self.num_box):
            b = TrashAgent(i + self.num_box, self)
            self.schedule.add(b)
            z = self.grid.find_empty()
            self.boxCoords.append(z)
            self.grid.place_agent(b, (z))

    def step(self):
        self.schedule.step()
