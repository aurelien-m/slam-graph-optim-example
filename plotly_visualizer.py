import math
import plotly.express as px
import plotly.graph_objects as go
from robot import Robot


class Visualizer:
    def __init__(self, env: list, robot: Robot):
        robot_positions = []
        annotations = []

        for position in robot.as_list():
            theta = position["theta"]
            x = position["x"]
            y = position["y"]
            x_arrow_end = x + 0.5 * math.cos(theta)
            y_arrow_end = y + 0.5 * math.sin(theta)

            robot_positions.append(position)
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

        self.fig = px.scatter(env + robot_positions, x="x", y="y", color="color")
        self.fig.update_yaxes(scaleanchor="x", scaleratio=1)
        self.fig.update_layout(annotations=annotations)

    def show(self):
        self.fig.show()
