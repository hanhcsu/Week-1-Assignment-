#Part 1: find the sum and difference of two numbers

#Define a function to get rid of trailing zeroes
def remove(x):
    if x % 1 == 0:
        return int(x)
    else:
        return x

# First input from user:
num1 = remove(float(input("Please enter the first number: ")))

# Second input from user:
num2 = remove(float(input("Please enter the second number: ")))

# Compute the sum of two numbers:
sum = remove(num1 + num2)

# Output the addition:
print("The sum of two number",num1,"and",num2,"is:",sum)

# Compute the difference of two numbers:
difference = remove(num1 - num2)

# Output the subtraction:
print("The difference of two number",num1,"and",num2,"is:",difference)