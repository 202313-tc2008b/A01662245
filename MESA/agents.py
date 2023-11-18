import mesa
import numpy as np

class Buildings(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

class ParkingSpots(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

class RoundAbout(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

class Stop(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

class Go(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

class Car(mesa.Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

    def step(self):
        # Get the current position
        x, y = self.pos

        # Check if the next position is within the grid
        if x + 1 < self.model.width:
            new_x = x + 1
            new_y = y
        else:
            # If at the end of the road, wrap around to the beginning
            new_x = 0
            new_y = y

        # Check if the next position is not blocked by another agent
        if self.model.grid.is_cell_empty((new_x, new_y)):
            # Move the car to the new position
            self.model.grid.move_agent(self, (new_x, new_y))