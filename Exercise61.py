value = int(input("Enter a value (enter 0 to finish): "))
total = 0
count = 0
if value == 0:
    print("Error: The first value is 0.")
else:
    while value != 0:
        total += value
        count += 1
        value = int(input("Enter a value: "))
    if count > 0:
        average = total / count
        print("The average of the values is:", average)
    else:
        print("Error: No value other than 0 was entered.")

