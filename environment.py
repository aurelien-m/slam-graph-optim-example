import numpy as np


def default_env(
    width: int = 20,
    height: int = 15,
    step: int = 0.5,
    circle_radius: int = 1,
    circle_points: int = 15,
    circle_center: tuple = (17, 3),
):
    landmarks = (
        [(0, i) for i in np.arange(0, height, step)]
        + [(width, i) for i in np.arange(0, height, step)]
        + [(i, 0) for i in np.arange(step, width, step)]
        + [(i, height - step) for i in np.arange(step, width, step)]
    )

    landmarks += [
        (
            circle_center[0] + circle_radius * np.cos(2 * np.pi * i / circle_points),
            circle_center[1] + circle_radius * np.sin(2 * np.pi * i / circle_points),
        )
        for i in range(circle_points)
    ]

    return [
        {
            "x": x,
            "y": y,
            "color": "landmark",
        }
        for x, y in landmarks
    ]
