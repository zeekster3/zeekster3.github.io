print("Enter a list of numbers, type 0 when finished.")
numbers = []
number = -1
while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")
count = len(numbers)
average = sum / count

print(f"The average is: {average}")
best_number = -1

for number in numbers:
    if number > best_number:
        best_number = number


print(f"The largest number is: {best_number}")