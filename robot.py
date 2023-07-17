import math

class Robot:
    def __init__(self, x: float, y: float, theta: float):
        self.theta = math.radians(theta)
        self.x = x
        self.y = y

    def as_list(self):
        return [
            {
                "x": self.x,
                "y": self.y,
                "theta": self.theta,
                "color": "robot",
            }
        ]
