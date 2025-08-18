## 1. Loops with input
name = input("Enter your name:" )
print(name)

## 2. Loops with Input

# a. Multiplication Table(for loop)

num = int(input("Enter a number:"))
print(f"multiplication of a number: {num}:");
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

# b. Sum until N (while loop)

n = int (input("enter a number n: "))
total = 0
count = 1
while count <=n:
    total += count
    count += 1

print(f"sum of numbers from 1 to {n} is :{total}")\

# c. Print Numbers up to N

n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(i)