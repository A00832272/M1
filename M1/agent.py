import mesa
import math

class RobotAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.carrying = 0
        self.stackCount = 0
        self.tempClosest = 100
        self.point = 0,0
        self.movingToX = 0
        self.movingToY = 0
        self.new_pos = (0,0)
        self.foundBox = False

    def step(self):
        j = len(self.model.boxCoords)
        temp = 0

        print("j: ",j)
        if(j == 0 and (self.pos[0] == 0 and self.pos[1] == 0)):
            print("1ST")
            self.stay()
        else:
            if (self.carrying == 0):
                print("2ND")
                if(self.foundBox == False and j > 0):
                    for i in range(j):
                        print(self.model.boxCoords)
                        if((math.dist(self.pos, self.model.boxCoords[i])) < self.tempClosest):
                            print(self.tempClosest)
                            self.tempClosest = math.dist(self.pos, self.model.boxCoords[i])

                            self.point = self.model.boxCoords[i]
                            temp = i
                            self.movingToX = self.point[0]
                            self.movingToY = self.point[1]
            
                    print("3rd")
                    self.foundBox = True
                    print(temp)
                    self.model.boxCoords.pop(temp)

            if(self.pos == (self.movingToX, self.movingToY)):
                print("4TH")
                self.foundBox = True
                #self.dropOff()
        if(self.pos == (0,0)):
            self.dropOff()
            self.foundBox =False
        

        self.move()
        
        

    def move(self):

        #move until you find a box
        new_pos = 0
        if(self.carrying == 0):

            if(self.pos[0] != self.movingToX):
                
                if(self.pos[0] <= self.movingToX):
                    new_pos = (self.pos[0] + 1, self.pos[1])

                else:

                    new_pos = (self.pos[0] - 1, self.pos[1])

            if(self.pos[1] != self.movingToY):

                if(self.pos[1] <= self.movingToY):

                    new_pos = (self.pos[0], self.pos[1] + 1)

                else:

                    new_pos = (self.pos[0], self.pos[1] + -1)

            if(self.pos[1] == self.movingToY and self.pos[0] == self.movingToX):
                self.carrying = 1
                self.pickUp()

        #carry the box back to the stack
        if(self.carrying == 1):

            if(self.pos[0] != 0):

                new_pos = (self.pos[0] - 1, self.pos[1])

            else:

                if(self.pos[1] != 0):

                    new_pos = (self.pos[0], self.pos[1] - 1)

        self.model.grid.move_agent(self,new_pos)


    def pickUp(self):
        if(self.carrying == 0):
            print()

    def dropOff(self):
        self.carrying = 0

    def stay(self):
        print("Staying")

