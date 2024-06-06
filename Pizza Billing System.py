bill = 0
print('-----Pizza Hut-----')

while True:
    print('------MENU-----\n1-Pizza\n2-Desserts\n3-Beverages\n4-Burger\n0-Finish Order')
    choice = int(input('Enter your choice: '))
    if choice == 0:
        break

    elif choice == 1:
        print('----Pizza Menu-----\n1-Corn Pizza=99\n2-Panner Pizza=129\n3-Chicken Pizza=159')
        pizza_choice = int(input('Enter your pizza choice: '))
        if pizza_choice == 1:
            pizza_cost = 99
        elif pizza_choice == 2:
            pizza_cost = 129
        elif pizza_choice == 3:
            pizza_cost = 159
        else:
            print('Invalid pizza choice')
            pizza_cost = 0

        print('----Size----\n1-Small=80\n2-Medium=90\n3-Large=100')
        size_choice = int(input('Enter your size choice: '))
        if size_choice == 1:
            size_cost = 80
        elif size_choice == 2:
            size_cost = 90
        elif size_choice == 3:
            size_cost = 100
        else:
            print('Invalid size choice')
            size_cost = 0

        print('-----Toppings----\n1-Olive=20\n2-Onion=35\n3-Capsicum=40')
        topping_choice = int(input('Enter your topping choice: '))
        if topping_choice == 1:
            topping_cost = 20
        elif topping_choice == 2:
            topping_cost = 35
        elif topping_choice == 3:
            topping_cost = 40
        else:
            print('Invalid topping choice')
            topping_cost = 0

        pizza_total = pizza_cost + size_cost + topping_cost
        bill += pizza_total
        print(f'Pizza total is: {pizza_total} Rs')

    elif choice == 2:
        print('---Desserts Menu----\n1-Ice Cream=50\n2-Brownie=80\n3-Cake=70')
        dessert_choice = int(input('Enter your dessert choice: '))
        if dessert_choice == 1:
            dessert_cost = 50
        elif dessert_choice == 2:
            dessert_cost = 80
        elif dessert_choice == 3:
            dessert_cost = 70
        else:
            print('Invalid dessert choice')
            dessert_cost = 0

        bill += dessert_cost
        print(f'Dessert total is: {dessert_cost} Rs')

    elif choice == 3:
        print('---Beverages----\n1-Coke=20\n2-Pepsi=20\n3-7UP=20')
        beverage_choice = int(input('Enter your beverage choice: '))
        if beverage_choice in [1, 2, 3]:
            beverage_cost = 20
        else:
            print('Invalid beverage choice')
            beverage_cost = 0

        bill += beverage_cost
        print(f'Beverage total is: {beverage_cost} Rs')

    elif choice == 4:
        print('---Burger Menu----\n1-Veg Burger=50\n2-Chicken Burger=70\n3-Cheese Burger=90')
        burger_choice = int(input('Enter your burger choice: '))
        if burger_choice == 1:
            burger_cost = 50
        elif burger_choice == 2:
            burger_cost = 70
        elif burger_choice == 3:
            burger_cost = 90
        else:
            print('Invalid burger choice')
            burger_cost = 0

        bill += burger_cost
        print(f'Burger total is: {burger_cost} Rs')

    else:
        print('Invalid choice, please select from the menu.')

print('Total bill is:', bill, 'Rs')
print('Thank you for dining with us!')
