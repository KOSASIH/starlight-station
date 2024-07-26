# utils/math_utils.py
import math
import numpy as np

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_angle(point1, point2):
    """Calculate the angle between two points in radians."""
    return math.atan2(point2[1] - point1[1], point2[0] - point1[0])

def rotate_point(point, angle, center=(0, 0)):
    """Rotate a point around a center point by a given angle in radians."""
    x, y = point
    cx, cy = center
    s = math.sin(angle)
    c = math.cos(angle)
    x -= cx
    y -= cy
    new_x = x * c - y * s
    new_y = x * s + y * c
    x = new_x + cx
    y = new_y + cy
    return (x, y)

def normalize_vector(vector):
    """Normalize a vector to have a length of 1."""
    magnitude = np.linalg.norm(vector)
    return vector / magnitude
