bill = 0
print('*------Meghanas Biryani--------*')
print('----MENU----\n1-Chicken Biryani=400Rs\n2-Mutton Biryani=450Rs\n3-Hyderbadi Dum Biryani=500Rs')
while True:
    ch = int(input('Enter your choice : '))
    if ch == 0:
        break
    elif ch == 1:
        q = int(input('Enter the quantity: '))
        bill += 400 * q
    elif ch == 2:
        q = int(input('Enter the quantity: '))
        bill += 450 * q
    elif ch == 3:
        q = int(input('Enter the quantity: '))
        bill += 500 * q
    else:
        print('Invalid choice, please try again.')
print('Total bill is:', bill)
print('Thank you for dining with us!')