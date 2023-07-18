import math
from random import random


class Robot:
    def __init__(self):
        self.trajectory = []

    def add_trajectory(self, trajectory: list):
        trajectory_length = len(self.trajectory)
        self.trajectory += [
            {
                "index": trajectory_length + i,
                "color": "robot",
                "theta_rad": math.radians(position["theta"]),
                "x": position["x"],
                "y": position["y"],
            }
            for i, position in enumerate(trajectory)
        ]

    def odometry(self, trans_noise: float = 1.0, theta_noise: float = 45) -> list:
        odometry = self.trajectory[0].copy()
        odometry["color"] = "odometry"
        odometries = [odometry]

        for i in range(len(self.trajectory[:-1])):
            t_x = self.trajectory[i + 1]["x"] - self.trajectory[i]["x"]
            t_y = self.trajectory[i + 1]["y"] - self.trajectory[i]["y"]

            odometry = {
                "index": i,
                "color": "odometry",
                "theta_rad": self.trajectory[i + 1]["theta_rad"]
                + random() * math.radians(theta_noise),
                "x": odometry["x"] + t_x + random() * trans_noise,
                "y": odometry["y"] + t_y + random() * trans_noise,
            }

            odometries.append(odometry)

        return odometries
