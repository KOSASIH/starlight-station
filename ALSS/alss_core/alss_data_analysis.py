import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ALSSDataAnalysis:
    def __init__(self, data):
        self.data = data

    def compute_statistics(self):
        # Compute statistics (mean, std, min, max) for each column
        stats = {}
        for col in self.data.columns:
            stats[col] = {
                'mean': self.data[col].mean(),
                'std': self.data[col].std(),
                'min': self.data[col].min(),
                'max': self.data[col].max()
            }
        return stats

    def plot_time_series(self, columns=None):
        # Plot time series data
        if columns is None:
            columns = self.data.columns
        plt.figure(figsize=(12, 6))
        for col in columns:
            plt.plot(self.data[col], label=col)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Time Series Data')
        plt.legend()
        plt.show()

    def plot_histograms(self, columns=None):
        # Plot histograms for each column
        if columns is None:
            columns = self.data.columns
        fig, axs = plt.subplots(nrows=len(columns), ncols=1, figsize=(6, 3*len(columns)))
        for i, col in enumerate(columns):
            axs[i].hist(self.data[col], bins=50)
            axs[i].set_title(f'Histogram of {col}')
            axs[i].set_xlabel('Value')
            axs[i].set_ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def compute_correlations(self):
        # Compute correlations between columns
        corr_matrix = self.data.corr()
        return corr_matrix

    def plot_correlation_matrix(self):
        # Plot correlation matrix
        corr_matrix = self.compute_correlations()
        plt.figure(figsize=(8, 8))
        plt.imshow(corr_matrix, interpolation='nearest')
        plt.title('Correlation Matrix')
        plt.colorbar()
        plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=45)
        plt.yticks(range(len(corr_matrix)), corr_matrix.columns)
        plt.show()

    def filter_data(self, column, threshold):
        # Filter data based on a threshold
        filtered_data = self.data[self.data[column] > threshold]
        return filtered_data

    def resample_data(self, freq):
        # Resample data at a specified frequency
        resampled_data = self.data.resample(freq).mean()
        return resampled_data
