# Inputs
print('Enter the following quantities in feet.')
row_size = (input('How long is this row? '))
end_post = (input('How wide is the end-post assembly? '))
vine_space = (input('How much space should be between the vines? '))

# Calculation

vines_number = (row_size-(2*end_post)) / vine_space
                       
# Print Statement
print(' ')
print(f'This row has enough space for {int(vines_number)} vine(s)')