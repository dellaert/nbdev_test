# AUTOGENERATED! DO NOT EDIT! File to edit: ../highway.ipynb.

# %% auto 0
__all__ = ['Lane', 'Highway']

# %% ../highway.ipynb 3
import numpy as np
from dataclasses import dataclass, field

import matplotlib.pyplot as plt


# %% ../highway.ipynb 5
@dataclass
class Lane:

    speed: float  # Speed of the vehicles
    arrival_rate: float  # Rate of vehicle arrivals (Poisson process)
    minimum_distance: float  # Minimum distance required between vehicles
    vehicles: list = field(default_factory=list)
    L : float = 1000  # Length of the road

    def step(self, dt):
        """Advance the simulation by one time step."""
        # Generate at most one new vehicle if it satisfies minimum distance
        if np.random.poisson(self.arrival_rate * dt) > 0:
            if not self.vehicles or (self.vehicles[-1] + self.L / 2>= self.minimum_distance):
                self.vehicles.append(-self.L / 2)
        
        # Update vehicle positions
        self.vehicles = [pos + self.speed * dt for pos in self.vehicles if pos + self.speed * dt <= self.L / 2]

# %% ../highway.ipynb 8
class Highway:
    def __init__(self):
        self.slow_lane = Lane(speed=25, arrival_rate=0.15, minimum_distance=32)
        self.middle_lane = Lane(speed=29, arrival_rate=0.15, minimum_distance=43)
        self.fast_lane = Lane(speed=34, arrival_rate=0.15, minimum_distance=59)

    def step(self, dt):
        """Advance the simulation by one time step for all lanes."""
        self.slow_lane.step(dt)
        self.middle_lane.step(dt)
        self.fast_lane.step(dt)
