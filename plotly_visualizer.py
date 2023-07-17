import plotly.express as px


class Visualizer:
    def __init__(self, env):
        self.fig = px.scatter(env, x="x", y="y", color="color")
        self.fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
        )

    def show(self):
        self.fig.show()
