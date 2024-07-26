# main.py
import os
import sys
from utils.math_utils import calculate_distance
from utils.data_utils import load_csv, split_data
from image_processing_utils import load_image, convert_to_grayscale
from signal_processing_utils import filter_signal, calculate_power_spectrum

def main():
    # Load data from a CSV file
    data = load_csv('data.csv')

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)

    # Load an image
    image = load_image('image.jpg')

    # Convert the image to grayscale
    grayscale_image = convert_to_grayscale(image)

    # Load a signal from a file
    signal = np.loadtxt('signal.txt')

    # Filter the signal
    filtered_signal, f, Pxx_den = filter_signal(signal, 10, 100)

    # Calculate the power spectrum of the filtered signal
    f, Pxx_den = calculate_power_spectrum(filtered_signal, 100)

    # Calculate the distance between two points
    point1 = (1, 2)
    point2 = (4, 6)
    distance = calculate_distance(point1, point2)

    print(f'The distance between the two points is {distance:.2f}')

if __name__ == '__main__':
    main()
