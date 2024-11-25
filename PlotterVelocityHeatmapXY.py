"""
This program reads a given CSV file in the /csvs/ folder and plots
a heatmap of velocity magnitudes on an X-Y coordinate system.

Input: CSV file name (e.g., genericname.csv)
Output: Heatmap with X-Y coordinates and velocity magnitudes.
"""

import matplotlib.pyplot as plt
import csv
import os

def plot_velocity_heatmap(csv_file):
    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found.")
        return

    # Initialize lists to store data
    x_coordinates = []
    y_coordinates = []
    velocities = []

    # Read data from CSV
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                x_coordinates.append(float(row["Avg X"]))
                y_coordinates.append(float(row["Avg Y"]))
                velocities.append(float(row["Velocity (μm/ms)"]))
            except KeyError:
                print("Error: CSV file does not contain the required columns.")
                return
            except ValueError:
                print("Error: Could not convert data to float.")
                return

    # Create the heatmap scatter plot
    plt.figure(figsize=(8, 6))
    sc = plt.scatter(
        x_coordinates, y_coordinates, c=velocities, cmap='viridis', s=50, edgecolor='k'
    )
    plt.xlabel('X Coordinate (pixels)', fontsize=14)
    plt.ylabel('Y Coordinate (pixels)', fontsize=14)
    plt.title('Velocity Heatmap (Magnitude as Color)', fontsize=16)
    cbar = plt.colorbar(sc, orientation='vertical')
    cbar.set_label('Velocity Magnitude (μm/ms)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Ask user for the CSV file path
    csv_file = "csvs/"
    csv_file += input("Enter CSV File name with .csv: ")  # e.g., genericname.csv
    plot_velocity_heatmap(csv_file)

if __name__ == "__main__":
    main()
