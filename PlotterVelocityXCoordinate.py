
"""
This program reads a given CSV file in the /csvs/ folder and plots
velocity on the Y and X coordinate on the X. This is most useful
for the abrupt sections. 

Input: csv file name ex: aer210.csv
Output: Plot inlc uncertainties no trendline.
"""

import matplotlib.pyplot as plt
import csv
import os

def plot_velocity_vs_y(csv_file):
    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found.")
        return

    # Initialize lists to store data
    velocities = []
    velocity_errors = []
    x_coordinates = []

    # Read data from CSV
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                velocities.append(float(row["Velocity (μm/ms)"]))
                velocity_errors.append(float(row["Uncertainty (μm/ms)"]))
                x_coordinates.append(float(row["Avg X"]))
            except KeyError:
                print("Error: CSV file does not contain the required columns.")
                return
            except ValueError:
                print("Error: Could not convert data to float.")
                return

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.errorbar(
        x_coordinates,
        velocities,
        yerr=velocity_errors,
        fmt='o',
        color='blue',
        ecolor='red',
        elinewidth=1,
        capsize=3,
        label='Data points with error bars'
    )
    plt.ylabel('Velocity (μm/ms)', fontsize=14)
    plt.xlabel('X Coordinate (pixels)', fontsize=14)
    plt.title('Velocity vs. X Coordinate', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Ask user for the CSV file path
    csv_file = "csvs/"
    csv_file += input("Enter CSV File name with .csv: ")  # e.g., genericname.csv
    plot_velocity_vs_y(csv_file)

if __name__ == "__main__":
    main()
