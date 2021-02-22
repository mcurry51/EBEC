################################################################################
# Author: Michael Curry
# Date: 02/21/2021
# This program calculates the total cost 
# of purchasing packages and administering discounts
# if needed.
################################################################################
packages = int(input('Please input the number of packages to be purchased: '))
per_package = 99
if packages < 0:
    print('  Invalid Input!')
elif packages in range(0,10): # Packages between the range of 0 and 10
    print('  No discount applied.')
    total_wo_dis_0 = int(packages * per_package)
    total_wo_dis_formatted_0 = f'{float(total_wo_dis_0):,.2f}'
    print(f'  The final price for purchasing {packages} packages is ${total_wo_dis_formatted_0}.')
elif packages in range(10,20): # Packages between the range of 10 and 20
    print('  10% discount applied.')
    total_wo_dis_10 = int(packages * per_package)
    total_w_dis_10 = total_wo_dis_10 * 0.10
    total_w_dis_10_final = total_wo_dis_10 - total_w_dis_10
    total_w_dis_formatted_10 = f'{float(total_w_dis_10_final):,.2f}'
    print(f'  The final price for purchasing {packages} packages is ${total_w_dis_formatted_10}.')
elif packages in range(20,50): # Packages between the range of 20 and 50
    print('  25% discount applied.')
    total_wo_dis_25 = int(packages * per_package)
    total_w_dis_25 = total_wo_dis_25 * 0.25
    total_w_dis_25_final = total_wo_dis_25 - total_w_dis_25
    total_w_dis_formatted_25 = f'{float(total_w_dis_25_final):,.2f}'
    print(f'  The final price for purchasing {packages} packages is ${total_w_dis_formatted_25}.')
elif packages in range(50,100): # Packages between the range of 50 and 99
    print('  35% discount applied.')
    total_wo_dis_35 = int(packages * per_package)
    total_w_dis_35 = total_wo_dis_35 * 0.35
    total_w_dis_35_final = total_wo_dis_35 - total_w_dis_35
    total_w_dis_formatted_35 = f'{float(total_w_dis_35_final):,.2f}'
    print(f'  The final price for purchasing {packages} packages is ${total_w_dis_formatted_35}.')
else:  # Packages between the range of 100 and etc
    print('  45% discount applied.')
    total_wo_dis_45 = int(packages * per_package)
    total_w_dis_45 = total_wo_dis_45 * 0.45
    total_w_dis_45_final = total_wo_dis_45 - total_w_dis_45
    total_w_dis_formatted_45 = f'{float(total_w_dis_45_final):,.2f}'
    print(f'  The final price for purchasing {packages} packages is ${total_w_dis_formatted_45}.')


    
