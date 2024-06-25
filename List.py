#lists
num_list = []
num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
num3 = float(input('Enter a number: '))
num4 = float(input('Enter a number: '))
num5 = float(input('Enter a number: '))
num_list = [num1, num2, num3, num4, num5]
print(num_list)

lowest = min(num_list)
print(lowest)

highest = max(num_list)
print(highest)

total = sum(num_list)
print(total)

length = len(num_list)
print(length)

average = total/length
print(average)
