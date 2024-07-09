#Tristan Beaty
#7-9-2024
#P3HW2
#calculate how much an employee is to be payed

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Eter employee's pay rate: "))

if hours > 40:
        ovt = hours - 40
        ovtpay = ovt * (rate * 1.5)
        regpay = 40 * rate
        gross = regpay + ovtpay
else:
        ovt = 0
        ovtpay = 0
        regpay = rate * hours
        gross = regpay


print("-"*37)
print("Employee name: ",name,"\n")

print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print("-"*98)

print(f'{hours:<15}{rate:<15}{ovt:<15}{ovtpay:<20.2f}{"$"}{regpay:<20.2f}{"$"}{gross:.2f}')

