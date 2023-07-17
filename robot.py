import math


class Robot:
    def __init__(self, x: float = None, y: float = None, theta: float = None):
        self.positions = []
        if x is not None and y is not None and theta is not None:
            self.positions.append({"x": x, "y": y, "theta_rad": math.radians(theta)})
        elif x is not None or y is not None or theta is not None:
            raise ValueError("x, y, and theta must be specified together")

    def update_positions(self, positions: list):
        self.positions += [
            {
                "theta_rad": math.radians(position["theta"]),
                "color": "robot",
                "x": position["x"],
                "y": position["y"],
            }
            for position in positions
        ]
