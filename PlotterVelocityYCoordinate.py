
"""
This program reads a given CSV file in the /csvs/ folder and plots
velocity on the X and Y coordinate on the Y. This is most useful
for thr striaght section. 

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
    y_coordinates = []

    # Read data from CSV
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                velocities.append(float(row["Velocity (μm/ms)"]))
                velocity_errors.append(float(row["Uncertainty (μm/ms)"]))
                y_coordinates.append(float(row["Avg Y"]))
            except KeyError:
                print("Error: CSV file does not contain the required columns.")
                return
            except ValueError:
                print("Error: Could not convert data to float.")
                return

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.errorbar(
        velocities,
        y_coordinates,
        xerr=velocity_errors,
        fmt='o',
        color='blue',
        ecolor='red',
        elinewidth=1,
        capsize=3,
        label='Data points with error bars'
    )
    plt.xlabel('Velocity (μm/ms)', fontsize=14)
    plt.ylabel('Y Coordinate (pixels)', fontsize=14)
    plt.title('Velocity vs. Y Coordinate', fontsize=16)
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
