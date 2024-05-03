#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program



def average(numbers): 
    total = sum(numbers) 
    avg = total / 5 
    return avg 
 
numbers = [] 
for i in range(5): 
    num = int(input("Enter a number")) 
    numbers.append(num) 
result = average(numbers) 
print(result)