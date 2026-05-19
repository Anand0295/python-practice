# 1.wap to check whether a number is positive and even using nested if.
# n = int(input("enter a number: "))

# if n > 0:
#     if n % 2 == 0:
#         print(f"{n} is positive and even")
#     else:
#         print(f"{n} is positive but odd")
# else:
#     print(f"{n} is not positive")

"""
enter a number: 8
8 is positive and even

enter a number: 5
5 is positive but odd

enter a number: -2
-2 is not positive
"""

# 2.wap to check whether a person is eligible for voting and has voter id using nested if.
# age = int(input("enter your age: "))

# if age >= 18:
#     voter_id = input("do you have voter id (yes/no): ")

#     if voter_id == "yes":
#         print("eligible for voting")
#     else:
#         print("voter id required")
# else:
#     print("not eligible for voting")

"""
enter your age: 20
do you have voter id (yes/no): yes
eligible for voting
"""

# 3.wap to check whether a student passed and scored distinction using nested if.
# marks = int(input("enter marks: "))

# if marks >= 35:
#     if marks >= 75:
#         print("student passed with distinction")
#     else:
#         print("student passed")
# else:
#     print("student failed")

"""
enter marks: 85
student passed with distinction

enter marks: 50
student passed

enter marks: 20
student failed
"""

# 4.wap to check whether a character is alphabet and uppercase using nested if.
# ch = input("enter a character: ")

# if ch.isalpha():
#     if ch.isupper():
#         print(f"{ch} is uppercase alphabet")
#     else:
#         print(f"{ch} is lowercase alphabet")
# else:
#     print(f"{ch} is not an alphabet")

"""
enter a character: A
A is uppercase alphabet

enter a character: b
b is lowercase alphabet

enter a character: 5
5 is not an alphabet
"""

# 5.wap to check whether a number is divisible by 2 and 5 using nested if.
# n = int(input("enter a number: "))

# if n % 2 == 0:
#     if n % 5 == 0:
#         print(f"{n} is divisible by 2 and 5")
#     else:
#         print(f"{n} is divisible by 2 but not by 5")
# else:
#     print(f"{n} is not divisible by 2")

"""
enter a number: 20
20 is divisible by 2 and 5

enter a number: 8
8 is divisible by 2 but not by 5

enter a number: 7
7 is not divisible by 2
"""

# 6.wap to check whether a person is adult and eligible for driving license using nested if.
# age = int(input("enter your age: "))

# if age >= 18:
#     if age >= 21:
#         print("eligible for driving license")
#     else:
#         print("adult but not eligible for driving license")
# else:
#     print("minor")

"""
enter your age: 25
eligible for driving license

enter your age: 18
adult but not eligible for driving license

enter your age: 15
minor
"""

# 7.wap to check whether a password length is valid and contains digit using nested if.
# password = input("enter password: ")

# if len(password) >= 6:
#     if any(ch.isdigit() for ch in password):
#         print("valid password")
#     else:
#         print("password must contain digit")
# else:
#     print("password length is too short")

"""
enter password: abc123
valid password

enter password: abcdef
password must contain digit

enter password: abc
password length is too short
"""

# 8.wap to check whether a number is positive and divisible by 3 using nested if.
# n = int(input("enter a number: "))

# if n > 0:
#     if n % 3 == 0:
#         print(f"{n} is positive and divisible by 3")
#     else:
#         print(f"{n} is positive but not divisible by 3")
# else:
#     print(f"{n} is not positive")

"""
enter a number: 9
9 is positive and divisible by 3

enter a number: 10
10 is positive but not divisible by 3

enter a number: -6
-6 is not positive
"""

# 9.wap to check whether a student attendance is above 75 and marks above 50 using nested if.
# attendance = int(input("enter attendance percentage: "))

# if attendance > 75:
#     marks = int(input("enter marks: "))

#     if marks > 50:
#         print("student is eligible")
#     else:
#         print("marks are below 50")
# else:
#     print("attendance is below 75")

"""
enter attendance percentage: 80
enter marks: 70
student is eligible
"""

# 10.wap to check whether a year is leap year and century year using nested if.
# year = int(input("enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         print(f"{year} is leap year and century year")
#     else:
#         print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

"""
enter a year: 2000
2000 is leap year and century year

enter a year: 2024
2024 is leap year

enter a year: 2023
2023 is not leap year
"""

# 11.wap to check whether a person is employee and salary is above 50000 using nested if.
# role = input("enter role: ")

# if role == "employee":
#     salary = int(input("enter salary: "))

#     if salary > 50000:
#         print("employee salary is above 50000")
#     else:
#         print("employee salary is below 50000")
# else:
#     print("not an employee")

"""
enter role: employee
enter salary: 70000
employee salary is above 50000
"""

# 12.wap to check whether a character is vowel and lowercase using nested if.
# ch = input("enter a character: ")

# if ch in "aeiouAEIOU":
#     if ch.islower():
#         print(f"{ch} is lowercase vowel")
#     else:
#         print(f"{ch} is uppercase vowel")
# else:
#     print(f"{ch} is not a vowel")

"""
enter a character: a
a is lowercase vowel

enter a character: A
A is uppercase vowel

enter a character: b
b is not a vowel
"""

# 13.wap to check whether a number is even and greater than 100 using nested if.
# n = int(input("enter a number: "))

# if n % 2 == 0:
#     if n > 100:
#         print(f"{n} is even and greater than 100")
#     else:
#         print(f"{n} is even but less than 100")
# else:
#     print(f"{n} is odd")

"""
enter a number: 120
120 is even and greater than 100

enter a number: 80
80 is even but less than 100

enter a number: 15
15 is odd
"""

# 14.wap to check whether a person is eligible for gym membership and senior citizen discount using nested if.
# age = int(input("enter your age: "))

# if age >= 18:
#     if age >= 60:
#         print("eligible for gym and senior citizen discount")
#     else:
#         print("eligible for gym membership")
# else:
#     print("not eligible for gym membership")

"""
enter your age: 65
eligible for gym and senior citizen discount

enter your age: 25
eligible for gym membership

enter your age: 15
not eligible for gym membership
"""

# 15.wap to check whether internet is connected and speed is fast using nested if.
# status = input("is internet connected (yes/no): ")

# if status == "yes":
#     speed = int(input("enter internet speed: "))

#     if speed > 100:
#         print("internet speed is fast")
#     else:
#         print("internet speed is slow")
# else:
#     print("internet not connected")

"""
is internet connected (yes/no): yes
enter internet speed: 150
internet speed is fast

is internet connected (yes/no): no
internet not connected
"""
