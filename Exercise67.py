total_cost = 0
age_input = input('Enter the age of the guest (press Enter to finish): ')
while age_input != '':
    age = int(age_input)
    if age <= 2:
        cost = 0.00
    elif 3 <= age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00
    total_cost += cost
    age_input = input('Enter the age of the guest (press Enter to finish): ')
print(f"The total admission cost for the group is: ${total_cost:.2f}")
