from math import exp
from os.path import join
from pathlib import Path


def calculate_percentage_distance(distance):
    """
    Obtains the percentage corresponding to the given distance
        :param distance(float): Distance
    """
    return round(100/(1 + exp(4*distance - 29.0)), 2)
