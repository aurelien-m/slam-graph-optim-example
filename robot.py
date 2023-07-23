import math
import numpy as np
from random import random


class Robot:
    def __init__(self, environment: list):
        self.environment = environment
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

    def measurements(self, radius: float = 10.0, max_rangle: float = 45.0):
        measurements = []
        max_angle = math.radians(max_rangle)

        for i in range(len(self.trajectory)):
            position = self.trajectory[i]
            pos_x, pos_y, theta = position["x"], position["y"], position["theta_rad"]
            position = np.array([pos_x, pos_y])

            x_front = pos_x + 1 * math.cos(theta)
            y_front = pos_y + 1 * math.sin(theta)
            front = np.array([x_front, y_front])

            pos_front = front - position

            for landmark in self.environment:
                land_x = landmark["x"]
                land_y = landmark["y"]

                distance = math.sqrt((land_x - pos_x) ** 2 + (land_y - pos_y) ** 2)
                if distance > radius:
                    continue

                landmark = np.array([landmark["x"], landmark["y"]])
                pos_land = landmark - position

                div = np.dot(pos_front, pos_land) / (
                    np.linalg.norm(pos_front) * np.linalg.norm(pos_land)
                )
                angle = abs(math.acos(np.clip(div, -1.0, 1.0)))

                if abs(angle) > max_angle:
                    continue

                measurements.append(
                    {
                        "index": i,
                        "color": "measurement",
                        "theta_rad": angle,
                        "x": land_x,
                        "y": land_y,
                    }
                )

        return measurements
