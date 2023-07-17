from environment import default_env
from plotly_visualizer import Visualizer
from robot import Robot

if __name__ == "__main__":
    env = default_env()
    robot = Robot(x=13, y=5, theta=90)

    vis = Visualizer(env, robot)
    vis.show()
