# 1. Even or Odd Function
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))  # Expected: Even

# 2. Square Calculator
def square(num):
    return num * num

print(square(5))  # Expected: 25

# 3. Greeting Based on Time
def time_greeting(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")

time_greeting("Vahini", "morning")  # Expected: Good morning, Vahini!
