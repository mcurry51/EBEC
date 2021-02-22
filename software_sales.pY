packages = int(input('Please input the number of packages to be purcharse: '))
per_package = 99
if packages <= 0:
    print('Invalid Input!')
elif packages < 10:
    print('No discount applied!')
    total_wo_dis_0 = int(packages * per_package)
    total_wo_dis_formatted_0 = f'{float(total_wo_dis_0):,.2f'
    print(f'The final price for purchasing {package} packages is ${total_wo_dis_formatted_0}')
elif packages >= 10 or packages <= 19:
    print('10 discount applied!')
    total_wo_dis_10 = int(packages * per_package)
    total_w_dis_10 = total_wo_dis_10 * 0.10
    total_w_dis_formatted_10 = f'{float(total_w_dis_10):,.2f}'
    print(f'The final price for purchasing {packages} packages is ${total_w_dis_formatted_10}')
elif packages >= 20 or packages <= 49:
    print('25 discount applied!')
    total_wo_dis_25 = int(packages * per_package)
    total_w_dis_25 = total_wo_dis_25 * 0.25
    total_w_dis_formatted_25 = f'{float(total_w_dis_25):,.2f}'
    print(f'The final price for purchasing {packages} packages is ${total_w_dis_formatted_25}')
elif package >= 50 or packages <= 99:
    print('25 discount applied!')
    total_wo_dis_35 = int(packages * per_package)
    total_w_dis_35 = total_wo_dis_35 * 0.25
    total_w_dis_formatted_35 = f'{float(total_w_dis_35):,.2f}'
    print(f'The final price for purchasing {packages} packages is ${total_w_dis_formatted_35}')
else:
    print('45 discount applied!')
    total_wo_dis_45 = int(packages * per_package)
    total_w_dis_45 = total_wo_dis_45 * 0.25
    total_w_dis_formatted_45 = f'{float(total_w_dis_45):,.2f}'
    print(f'The final price for purchasing {packages} packages is ${total_w_dis_formatted_45}')


    
