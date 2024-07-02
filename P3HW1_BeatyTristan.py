# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
length = len(grades)
average = total/length

print()
print("------------Results------------")
print(f'{"Lowest Grade":<20}{low}')
print(f'{"Highest Grade":<20}{high}')
print(f'{"Sum of Grades":<20}{total}')
print(f'{"Average":<20}{average:.2f}')
print("----------------------------------------")
print()

# determine letter grade for average


if average >= 90:
    print('Your grade is: A')
else:
    if average >= 80:
         print('Your grade is: B')
    else:
        if average >= 70:
         print('Your grade is: C')
        else:
            if average >= 60:
                print('Your grade is: D')
            else:
                    print('Your grade is: F') # TO DO: finish this





