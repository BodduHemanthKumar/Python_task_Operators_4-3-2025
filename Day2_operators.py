#Operators in Python
#let see some examples on Operators in Python.

# Arithmetic Operators
a = 10
b = 5
result = a + b  # 10 + 5 = 15
print(result)
result = a - b  # 10 - 5 = 5
print(result)
result = a * b  # 10 * 5 = 50
print(result)
result = a / b  # 10 / 5 = 2.0
print(result)
result = a % b  # 10 % 5 = 0
print(result)
result = a ** b  # 10 ** 5 = 100000
print(result)
result = a // b  # 10 // 5 = 2
print(result)


#Comparison Operators
result = a == b  # 10 == 5 -> False
print(result)
result = a != b  # 10 != 5 -> True
print(result)
result = a > b  # 10 > 5 -> True
print(result)
result = a < b  # 10 < 5 -> False
print(result)
result = a >= b  # 10 >= 5 -> True
print(result)
result = a <= b  # 10 <= 5 -> False
print(result)


#Logical Operators
result = (a > 5) and (b < 10)  # True and True -> True
print(result)
result = (a > 5) or (b > 10)  # True or False -> True
print(result)
result = not(a > 5)  # not(True) -> False
print(result)


#Assignment Operators
a = 10  # Assigns 10 to variable a
print(a)
a += 5  # a = a + 5 -> 10 + 5 = 15
print(a)
a -= 3  # a = a - 3 -> 15 - 3 = 12
print(a)
a *= 2  # a = a * 2 -> 12 * 2 = 24
print(a)
a /= 4  # a = a / 4 -> 24 / 4 = 6.0
print(a)

#Bitwise Operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b  # 0001 -> 1
print(result)
result = a | b  # 0111 -> 7
print(result)
result = a ^ b  # 0110 -> 6
print(result)


#Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
result = a is b  # False, because they point to different objects
print(result)
result = a is not b  # True, because a and b are different objects
print(result)


#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grapes" not in fruits)  # Output: True