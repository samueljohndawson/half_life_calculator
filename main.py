import numpy as np
import matplotlib.pyplot as plt
import math

isotopes = []


def get_user_input():
    # Ask the user for information about the isotope and covert numerical values into floating point numbers
    isotope = input('Please enter the name of the isotope: ')
    isotopes.append(isotope)
    half_life = float(input('Please enter the half-life of the isotope (in seconds): '))
    init_mass = float(input('Please enter the initial mass of the isotope (in grams): '))
    elapsed_time = float(input('Please enter the elapsed time (in seconds): '))
    return isotope, half_life, init_mass, elapsed_time


def calc_remaining_mass(isotope, half_life, init_mass, elapsed_time):
    # Calculate the remaining mass given the users input, and display the result in the console
    remaining_mass = init_mass * np.exp(-math.log(2) * (elapsed_time / half_life))
    print('After ' + str(elapsed_time) + ' s there will be ' + str(remaining_mass) + ' g of ' + isotope + ' remaining.')


def calc_init_mass_needed(isotope, half_life):
    # Calculate the initial mass of the isotope (in grams) necessary so that 5 grams remain after 30s
    remaining_mass = 5
    elapsed_time = 30
    init_mass_needed = remaining_mass / (np.exp(-math.log(2) * (elapsed_time / half_life)))
    print('In order for there to be ' + str(remaining_mass) + ' g of ' + isotope + ' remaining after ' + str(
        elapsed_time) + ' s, the initial mass of ' + isotope + ' must be ' + str(init_mass_needed) + ' g.')


def plot_decay(isotope, init_mass, half_life):
    # Generate values for the x-axis (time, in seconds)
    x_points = np.linspace(0, 10, 100, endpoint=True)

    # Calculate values for the y-axis (mass, in grams)
    y_points = init_mass * np.exp(-math.log(2) * (x_points / half_life))

    # Plot a graph of mass vs time
    plt.plot(x_points, y_points, label=isotope)


def display_graph():
    # Label and display a graph given the users input
    plt.title('Decay of isotopes over time')
    plt.xlabel('Time /s')
    plt.ylabel('Mass /g')
    plt.show()


def main_program():
    # Call the get_user_input function and assign variables to the results
    user_isotope, user_half_life, user_init_mass, user_elapsed_time = get_user_input()

    # Call the calc_remaining_mass function using the users input
    calc_remaining_mass(user_isotope, user_half_life, user_init_mass, user_elapsed_time)

    # Call the calc_init_mass_needed function using the users input
    calc_init_mass_needed(user_isotope, user_half_life)

    # Call the plot_decay function using the users input
    plot_decay(user_isotope, user_init_mass, user_half_life)

    # Call the add_another_isotope function
    add_another_isotope()


def add_another_isotope():
    # Ask the user if they would like to add another isotope (only accepts yes or no)
    while True:
        choice = input('Would you like to enter another isotope? (yes / no): ').lower()
        if choice == 'yes':
            main_program()
            break
        elif choice == 'no':
            break
        else:
            print('Please enter either yes or no.')


def print_isotopes():
    # Print a list of all the isotopes the user has entered
    print('Isotopes plotted:')
    for isotope in isotopes:
        print(isotope)


# Run the main program and display the graph once the user has inputted all isotopes
main_program()
display_graph()
print_isotopes()
