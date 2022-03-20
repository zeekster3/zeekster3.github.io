import csv
print()

with open('W11life-expectancy.csv', 'r') as life_file:

    csvreader = csv.reader(life_file)

    next(csvreader)

    lowest = 100
    low = []
    highest = 0
    high = []
    average = 0
    average_list = []
    choice1 = int(input('Which year would you like to check the average for? '))
    user_lowest1 = 100
    user_low1 = []
    user_highest1 = 0
    user_high1 = []
    choice2 = input('Which country would you like to see statistics for? ')
    user_lowest2 = 100
    user_low2 = []
    user_highest2 = 0
    user_high2 = []
    user_average = 0
    user_avg_list = []

# Iterating through the file
    for row in life_file:
        row = row.strip()
        row = row.split(',')
        if float(row[3]) < lowest:
            lowest = float(row[3])
            low = row
        if float(row[3]) > highest:
            highest = float(row[3])
            high = row
        if float(row[2]) == choice1:
            average_list.append(float(row[3]))
            average = round(sum(average_list) / len(average_list), 2)
            if float(row[3]) < user_lowest1:
                user_lowest1 = float(row[3])
                user_low1 = row
            if float(row[3]) > user_highest1:
                user_highest1 = float(row[3])
                user_high1 = row
        if row[0] == choice2 and float(row[3]) < user_lowest2:
            user_lowest2 = float(row[3])
            user_low2 = row
        if row[0] == choice2 and float(row[3]) > user_highest2:
            user_highest2 = float(row[3])
            user_high2 = row
        if row[0] == choice2:
            user_avg_list.append(float(row[3]))
            user_average = round(sum(user_avg_list) / len(user_avg_list), 2)
            
# Display ing lowest and highest age
    print()
    print('The lowest life expectancy ever recorded worldwide was:')
    print(low)

    print()
    print('The highest life expectancy ever recorded worldwide was:')
    print(high)

    print()
    print(f'The average life expectacy recorded worldwide in the year {choice1} was {average} years old')

    print()
    print(f'The lowest life expectancy in {choice1} was:')
    print(user_low1)
    print()
    print(f'The highest life expectancy in {choice1} was:')
    print(user_high1)

    print()
    print(f'Statistics for {choice2}')
    
    print()
    print(f'The lowest life expectancy ever recorded in {choice2} was:')
    print(user_low2)

    print()
    print(f'The highest life expectancy ever recorded in {choice2} was:')
    print(user_high2)

    print()
    print(f'The average life expectancy throughout recorded history in {choice2} is {user_average} years old')

    print()