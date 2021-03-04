################################################################################
# Author: Michael Curry
# Date: 02/21/2021
# This program asks the user for the velocity of thewater flowing through a pipe
# (V), for the pipe’s diameter (d), and to select the water’s tem-perature (T) 
# from 5C,10C,and 15C
################################################################################
velocity = float(input('Enter the velocity of water in the pipe: ')) # Velocity of water
pipe_diameter = float(input('Enter the pipe\'s diameter: ')) # Diameter of pipe
pipe_temperature = float(input('Enter the temperature in °C as 5, 10, or 15: ')) # Temperature of water
if pipe_temperature == 5: # Condition 1
    viscocity = 1.49 / 1000000
    reynolds_number = (velocity * pipe_diameter) / viscocity
    rey_sci_not = f'{reynolds_number:.2e}'
    print(f'The Reynolds number for flow at {velocity} m/s '
          f'in a {pipe_diameter} m diameter pipe at {pipe_temperature}°C is {rey_sci_not}.')
elif pipe_temperature == 10: # Condition 2
    viscocity = 1.31 / 1000000
    reynolds_number = (velocity * pipe_diameter) / viscocity
    rey_sci_not = f'{reynolds_number:.2e}'
    print(f'The Reynolds number for flow at {velocity} m/s '
          f'in a {pipe_diameter} m diameter pipe at {pipe_temperature}°C is {rey_sci_not}.')
else: # Condition 3
    viscocity = 1.15 / 1000000
    reynolds_number = (velocity * pipe_diameter) / viscocity
    rey_sci_not = f'{reynolds_number:.2e}'
    print(f'The Reynolds number for flow at {velocity} m/s '
          f'in a {pipe_diameter} m diameter pipe at {pipe_temperature}°C is {rey_sci_not}.')
