# image_processing_utils.py
import cv2
import numpy as np

def load_image(file_path):
    """Load an image from a file path."""
    return cv2.imread(file_path)

def resize_image(image, width, height):
    """Resize an image to a specified width and height."""
    return cv2.resize(image, (width, height))

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_threshold(image, threshold_value):
    """Apply a threshold to an image."""
    _, thresh = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh

def detect_edges(image):
    """Detect edges in an image using the Canny edge detection algorithm."""
    return cv2.Canny(image, 50, 150)

def find_contours(image):
    """Find contours in an image."""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    """Draw contours on an image."""
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    return image
