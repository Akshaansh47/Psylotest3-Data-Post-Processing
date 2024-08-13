import matplotlib.pyplot as plt
import numpy as np


def read_notepad_file(file_path, encoding='latin-1'):
    # Open the file in read mode with specified encoding
    with open(file_path, 'r', encoding=encoding) as file:
        # Skip the first 16 lines
        for _ in range(16):
            next(file)
        # Read the remaining lines
        lines = file.readlines()

    # Create lists to store columnar data
    time = []
    primary_encoder_displacement = []
    secondary_encoder_displacement = []
    load_cell_full_scale = []

    # Iterate over each line in the remaining lines
    for line in lines:
        # Split the line by tab
        columns = line.strip().split('\t')
        # Convert each column to float and append to respective arrays
        time.append(float(columns[0]))
        primary_encoder_displacement.append(float(columns[1]))
        secondary_encoder_displacement.append(float(columns[2]))
        load_cell_full_scale.append(float(columns[3]))

    return time, primary_encoder_displacement, secondary_encoder_displacement, load_cell_full_scale


def psylo():
    option = input("\nWhich of the following would you like to see?"
                   "\n1. Primary Encoder Displacement vs. Time"
                   "\n2. Load vs. Time"
                   "\n3. Load vs. Primary Encoder Displacement (indicative of Stress-Strain for homogeneous materials)"
                   "\n4. Maximum Load,Maximum Primary Encoder Displacement\n")
    option = int(option)
    if option == 1:
        plt.plot(t, pri)
        plt.xlabel("Time(s)")
        plt.ylabel("Displacement(m)")
        plt.title("Axial Deformation vs. Time")
        plt.show()
    elif option == 2:
        plt.plot(t, load)
        plt.xlabel("Time(s)")
        plt.ylabel("Force(N)")
        plt.title("Axial Loading vs. Time")
        plt.show()
    elif option == 3:
        plt.plot(pri, load)
        plt.xlabel("Displacement(m)")
        plt.ylabel("Force(N)")
        plt.title("Axial Loading vs. Displacement")
        plt.show()
    elif option == 4:
        print("Maximum Axial Load (N) = ", max(abs(lnp(load))))
        print("Maximum Primary Encoder Displacement (m) = ", max(abs(lnp(pri))))
    else:
        print("\nInvalid")


def lnp(x):
    return np.array(x)


file_path = input("\nPlease enter your file path:\n")
q1,file_path,q2 = file_path.split('"')
t, pri, sec, load = read_notepad_file(file_path)


running = True
while running:
    psylo()
    q = input("\n Would you like to view something else?(Y/N)\n")
    if q == "Y" or q == "y" or q == "Yes" or q == "yes":
        running = True
    elif q == "N" or q == "n" or q == "No" or q == "no":
        running = False
    else:
        print("\n You deserve to start over.")
        running = False
