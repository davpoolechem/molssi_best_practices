import numpy as np

# %matplotlib notebook


def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
    """
    Calculate the distance between two points A and B.

    Parameters
    ----------
    rA : np.ndarray
        Coordinates of point A.
    rB : np.ndarray
        Coordinates of point B.

    Returns
    -------
    dist : float
        Distance between A and B.

    Examples
    --------
    ```
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    ```
    """
    d = rA - rB
    dist = np.linalg.norm(d)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(
        np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC))
    )

    if degrees:
        return np.degrees(theta)
    else:
        return theta
