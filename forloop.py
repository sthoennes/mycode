#!/usr/bin/env python3

fruits = ["apple","banana","cherry"]

print(fruits)

print("iterating through fruits list knowing it has 3 items")
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("Using a for loop now!")
for fruit in fruits:
    print(fruit)
    if fruit.startswith("b"):
        print(f"{fruit}s are not for me")

my_nums = [1,2,3,"a","b","c"]
for num in my_nums:
    print(num)

#one way to increment through a range of numbers
print(range(1,10))
for number in range(1,11):
    print(number)

#another way to increment through a range of numbers
i = 1
while i < 101:
    print(i)
    i += 1

