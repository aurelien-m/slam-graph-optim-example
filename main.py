from environment import default_env
from plotly_visualizer import Visualizer
from robot import Robot

robot_trajectory = [
    {"x": 13, "y": 5, "theta": 315},
    {"x": 9, "y": 3, "theta": 270},
    {"x": 5, "y": 5, "theta": 225},
    {"x": 5, "y": 9, "theta": 135},
    {"x": 9, "y": 11, "theta": 90},
    {"x": 13, "y": 9, "theta": 45},
    {"x": 14, "y": 6, "theta": 300},
]

if __name__ == "__main__":
    env = default_env()

    robot = Robot()
    robot.add_trajectory(robot_trajectory)

    vis = Visualizer(env, robot)
    vis.show()
