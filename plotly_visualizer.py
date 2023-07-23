import math
import plotly.express as px
import plotly.graph_objects as go
from robot import Robot


class Visualizer:
    def __init__(self, env: list, robot: Robot):
        robot_positions = []
        annotations = []

        for ground_truth, odometry in zip(robot.trajectory, robot.odometry()):
            self.__append_plotly_data(robot_positions, annotations, ground_truth)
            self.__append_plotly_data(robot_positions, annotations, odometry)

        for measurement in robot.measurements():
            self.__append_plotly_data(
                robot_positions, annotations, measurement, arrow=False
            )

        self.fig = px.scatter(
            env + robot_positions, x="x", y="y", color="color", hover_data=["index"]
        )
        self.fig.update_yaxes(scaleanchor="x", scaleratio=1)
        self.fig.update_layout(annotations=annotations)

    def __append_plotly_data(self, all_data, annotations, data, arrow=True):
        theta = data["theta_rad"]
        x = data["x"]
        y = data["y"]
        x_arrow_end = x + 0.5 * math.cos(theta)
        y_arrow_end = y + 0.5 * math.sin(theta)

        all_data.append(data)
        if arrow:
            annotations.append(
                go.layout.Annotation(
                    dict(
                        x=x_arrow_end,
                        y=y_arrow_end,
                        xref="x",
                        yref="y",
                        text="",
                        showarrow=True,
                        axref="x",
                        ayref="y",
                        ax=x,
                        ay=y,
                        arrowhead=3,
                        arrowwidth=1.5,
                        arrowcolor="red",
                    )
                )
            )

    def show(self):
        self.fig.show()
