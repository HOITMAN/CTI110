#Tristan Beaty
#6/20/2024
#P1HW2
#Calculating a budget

print('Please enter your name:', end = ' ')
name = input()
print()

print('Hello', name+ ', let us calculate your travel expenses \n')

print('First, can you tell me what the budget for your trip is:', end = ' ')
budget = int(input())
print()

print('Where are you planning on going:', end = ' ')
location = input()
print()

print('How much do you plan on spending on gas:', end = ' ')
gas = int(input())
print()

print('What will be the total cost of housing/hotels:', end = ' ')
housing = int(input())
print()

print('Lastly, combining both groceries and resturants, how much do you plan on spending for food:', end = ' ')
food = int(input())
print('\n')

print('--------Travel Summary--------')
print('Location:', location)
print('Initial Budget:', budget, '\n')

print('Gas:', gas)
print('Accomodations:', housing)
print('Food:', food, '\n')

rem_budget = budget - gas - housing - food 
print('Budget Remaining:', rem_budget, '\n')

if rem_budget >= 0:
    print('Alright', name+ ', it seems like your budget allows for your trip to go as planned\n\n')
else:
    print('Sorry', name+ ', it seems like what you have planned is over budget.')
    print('Either increase your budget or try to cut down on some expenses.\n\n')

input('Press ENTER to close')


