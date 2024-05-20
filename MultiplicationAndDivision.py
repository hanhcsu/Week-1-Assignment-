#Part 2: find the product and quotient of two numbers

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

# Compute the product of two numbers:
product = remove(num1 * num2)

# Output the product:
print("The product of two number",num1,"and",num2,"is:",product)

# Compute the quotient of two numbers:
# Require a different input if second number is zero:
while num2 == 0:
    print("Please enter a number that is different than zero to proceed with the division.")
    num2 = float (input("Please enter the second number: "))
quotient = remove(num1 / num2)

# Output the quotient:
print("The quotient of two number",num1,"and",num2,"is:",quotient)