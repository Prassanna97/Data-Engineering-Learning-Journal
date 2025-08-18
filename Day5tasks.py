## 1.Multiplication table

num = int(input("Enter a number:"))
for i in range(1,11):
    print(f" {num} * {i}= {num *i}")

## Sum until N

n = int(input("Enter the number: "))
total =0
count = 1

while count <= n:
    total += count 
    count += 1
print(f"sum of number {n} is: {total} ")


## 3.Print numbers

n= int(input("Enter a number:"))

for i in range(1,n+1):
    print(i)

## 4.Print even numbers

n= int(input("Enter a number:"))

for i  in range(1,n+1):
    if i % 2 == 0:
        print(i)

## 5.Print reverse number

n = int(input("Enter a number: "))


for i in range(n, 0, -1):
    print(i)




