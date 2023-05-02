#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to Find LCM?

# In[1]:


import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = math.gcd(num1, num2)
lcm = (num1 * num2) // gcd
print("LCM of", num1, "and", num2, "is", lcm)


# 2.Write a Python Program to Find HCF?

# In[2]:


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
while smaller > 0:
    if num1 % smaller == 0 and num2 % smaller == 0:
        hcf = smaller
        break
    smaller -= 1
print("HCF of", num1, "and", num2, "is", hcf)


# 3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[4]:


decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print("Binary representation of", decimal, "is", binary)
print("Octal representation of", decimal, "is", octal)
print("Hexadecimal representation of", decimal, "is", hexadecimal)


# 4.Write a Python Program To Find ASCII value of a character?

# In[12]:


char = input("Enter a character: ")
ascii_value = ord(char)
print("The ASCII value of", char, "is", ascii_value)


# 5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[13]:


def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")


# In[ ]:




