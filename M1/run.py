from agent import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
import mesa


def agent_portrayal(agent):

    portrayal = {"Filled": "true"}
    if agent.unique_id < 5:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    else:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "red"
        portrayal["Layer"] = "1"
        portrayal["w"] = 0.2
        portrayal["h"] = 0.2
        portrayal["xAlign"] = 0.5
        portrayal["yAlign"] = 0.5
    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    CleaningModel, [grid], "Box Model", {"NumCleaners": 5, "NumTrash": 15, "width": 10, "height": 15}
)
server = ModularServer(CleaningModel,
                       [grid],
                       "Box Model",
                       {"NumCleaners": 5, "NumTrash": 15, "width": 10, "height": 15})
server.port = 8520 # The default
server.launch()
