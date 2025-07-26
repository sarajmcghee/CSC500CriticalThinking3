
#Part 1

try:
    food_amount = float(input("Enter the cost of your Meal: "))
    if food_amount < 0:
        print("Invalid input. Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

tip_percentage = 0.18
tax_percentage = 0.07

total_cost = food_amount + (food_amount * tip_percentage) + (food_amount * tax_percentage)

print(f"Tip Amount: {food_amount * tip_percentage:.2f}")
print(f"Tax Amount: {food_amount * tax_percentage:.2f}")
print(f"Total Cost: {total_cost:.2f}")


#Part 2
try:
    current_hour = int(input("Enter the current hour (0-23): "))
    if current_hour < 0 or current_hour > 23:
        print("Invalid hour. Please enter a number between 0 and 23.")
        exit()
    waiting_time = int(input("How many hours until your desired Alarm?: "))
    if waiting_time < 0:
        print("Invalid input. Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input. Please enter Integer values only.")
    exit()

alarm_hour = (current_hour + waiting_time) % 24
print(f"Your alarm will go off at {alarm_hour:02d}:00.")

