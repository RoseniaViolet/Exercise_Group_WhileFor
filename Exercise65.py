import math

x_first = float(input("Enter the initial x coordinate: "))
y_first = float(input("Enter the initial y coordinate: "))
x_end = x_first
y_end = y_first
perimeter = 0

x_next_input = input("Enter the x part of the coordinate: (blank to quit): ")

while x_next_input:
    x_next = float(x_next_input)
    y_next = float(input("Enter the y part of the coordinate: "))
    
    distance = math.sqrt((x_end - x_next)**2 + (y_end - y_next)**2)
    perimeter += distance

    x_end = x_next
    y_end = y_next

    x_next_input = input("Enter the x part of the coordinate: (blank to quit): ")

distance_total = math.sqrt((x_end - x_first)**2 + (y_end - y_first)**2)
perimeter += distance_total

print('The perimeter of the polygon is', perimeter)
