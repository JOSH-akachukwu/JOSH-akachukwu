# program to Add and Multiply numbers

# making my add_numbers function
def add_numbers(n1, n2):
    sum_of_numbers = n1 + n2
    return sum_of_numbers

# making my multiply_numbers function
def multiply_numbers(n1, n2):
    multiple_of_numbers = n1 * n2
    return multiple_of_numbers

n1 =int(input("Enter first number:"))
n2 =int(input("Enter second number:"))

# program to add the two numbers
add = add_numbers(n1, n2)
print("The sum of", n1,"and", n2, "is", add)

#program to multiply the two numbers
multiple = multiply_numbers(n1, n2)
print("The multiplication of", n1, "and", n2, "is", multiple)


# BY O.J.A