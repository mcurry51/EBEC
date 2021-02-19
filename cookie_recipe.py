num_cookies = int(input('How many cookies do you want to make? '))
print(f'To make {num_cookies} cookies, you will need:')
sugar = num_cookies * (1.5 / 48)
formatted_sugar = f'{float(sugar):7,.2f}'
butter = num_cookies * (1 / 48)
formatted_butter = f'{float(butter):7,.2f}'
flour = num_cookies * (2.75 / 48)
formatted_flour = f'{float(flour):7,.2f}'
print(f'{formatted_sugar} cups of sugar')
print(f'{formatted_butter} cups of butter')
print(f'{formatted_flour} cups of flour')
