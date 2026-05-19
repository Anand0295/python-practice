# if condition:
#     |----------|
#     |   TSB    |
#     |----------|
#  else:
#     |----------|
#     |   FSB    |
#     |----------|

# 1.wap to check whether a number is even or odd.
# n = int(input("enter a number: "))
# if n % 2 == 0:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")

"""
enter a number: 1
1 is odd

enter a number: 6
6 is even
"""

# 2.wap to check whether a person is eligible for driving.
# age = int(input("enter your age: "))
# if age >= 18:
#     print(f"{age} is eligible for driving")
# else:
#     print(f"{age} is not eligible for driving")

"""
enter your age: 20
20 is eligible for driving

enter your age: 15
15 is not eligible for driving
"""

# 3.wap to find the greater number between two numbers.
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")

"""
enter a number: 12
enter a number: 25
25 is greater than 12
"""
# 4.wap to check whether a character is vowel or consonant.
# ch = input("enter a character: ")
# if ch in "aeiouAEIOU":
#     print(f"{ch} is a vowel")
# else:
#     print(f"{ch} is a consonant")

"""
enter a character: a
a is a vowel


enter a character: b
b is a consonant
"""

# 5.wap to check whether a student is pass or fail.
# marks = int(input("enter your marks: "))
# if marks >= 35:
#     print(f"{marks} is pass")
# else:
#     print(f"{marks} is fail")

"""
enter your marks: 80
80 is pass

enter your marks: 20
20 is fail
"""

# 6.wap to check whether a number is positive or negative.
# n = int(input("enter a number: "))
# if n > 0:
#     print(f"{n} is positive")
# else:
#     print(f"{n} is negative")

"""
enter a number: 10
10 is positive

enter a number: -5
-5 is negative
"""

# 7.wap to check whether a number is divisible by 2 or not.
# n = int(input("enter a number: "))
# if n % 2 == 0:
#     print(f"{n} is divisible by 2")
# else:
#     print(f"{n} is not divisible by 2")

"""
enter a number: 8
8 is divisible by 2

enter a number: 7
7 is not divisible by 2
"""

# 8.wap to check whether a number is divisible by both 5 and 11.
# n = int(input("enter a number: "))
# if n % 5 == 0 and n % 11 == 0:
#     print(f"{n} is divisible by both 5 and 11")
# else:
#     print(f"{n} is not divisible by both 5 and 11")

"""
enter a number: 55
55 is divisible by both 5 and 11

enter a number: 20
20 is not divisible by both 5 and 11
"""

# 9.wap to check whether a year is leap year or not.
year = int(input("enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

"""
enter a year: 2024
2024 is leap year

enter a year: 2023
2023 is not leap year
"""

# 10.wap to check whether a character is uppercase or lowercase.
# ch = input("enter a character: ")
# if ch.isupper():
#     print(f"{ch} is uppercase")
# else:
#     print(f"{ch} is lowercase")

"""
enter a character: A
A is uppercase

enter a character: b
b is lowercase
"""

# 11.wap to find the smallest among two numbers.
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# if a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print(f"{b} is smaller than {a}")

"""
enter a number: 10
enter a number: 20
10 is smaller than 20
"""

# 12.wap to check whether a person is senior citizen or not.
# age = int(input("enter your age: "))
# if age >= 60:
#     print(f"{age} is a senior citizen")
# else:
#     print(f"{age} is not a senior citizen")

"""
enter your age: 65
65 is a senior citizen

enter your age: 40
40 is not a senior citizen
"""

# 13.wap to check whether temperature is hot or cold.
# temp = int(input("enter temperature: "))
# if temp > 30:
#     print(f"{temp}°C is hot")
# else:
#     print(f"{temp}°C is cold")

"""
enter temperature: 36
36°C is hot

enter temperature: 20
20°C is cold
"""

# 14.wap to check whether a number is multiple of 3 or not.
# n = int(input("enter a number: "))
# if n % 3 == 0:
#     print(f"{n} is multiple of 3")
# else:
#     print(f"{n} is not multiple of 3")

"""
enter a number: 9
9 is multiple of 3

enter a number: 10
10 is not multiple of 3
"""

# 15.wap to check whether a password is correct or wrong.
# password = input("enter password: ")
# if password == "python123":
#     print("correct password")
# else:
#     print("wrong password")

"""
enter password: python123
correct password

enter password: hello
wrong password
"""

# 16.wap to check whether a number is zero or non-zero.
# n = int(input("enter a number: "))
# if n == 0:
#     print(f"{n} is zero")
# else:
#     print(f"{n} is non-zero")

"""
enter a number: 0
0 is zero

enter a number: 5
5 is non-zero
"""

# 17.wap to check whether a person is child or adult.
# age = int(input("enter your age: "))
# if age < 18:
#     print(f"{age} is a child")
# else:
#     print(f"{age} is an adult")

"""
enter your age: 10
10 is a child

enter your age: 25
25 is an adult
"""

# 18.wap to check whether entered fruit is mango or not.
# fruit = input("enter a fruit name: ")
# if fruit == "mango":
#     print(f"{fruit} is mango")
# else:
#     print(f"{fruit} is not mango")

"""
enter a fruit name: mango
mango is mango

enter a fruit name: apple
apple is not mango
"""

# 19.wap to check whether a number is greater than 500 or not.
# n = int(input("enter a number: "))
# if n > 500:
#     print(f"{n} is greater than 500")
# else:
#     print(f"{n} is not greater than 500")

"""
enter a number: 700
700 is greater than 500

enter a number: 200
200 is not greater than 500
"""

# 20.wap to compare two strings and check whether they are equal or not.
# a = input("enter first string: ")
# b = input("enter second string: ")
# if a == b:
#     print("both strings are equal")
# else:
#     print("both strings are not equal")

"""
enter first string: hello
enter second string: hello
both strings are equal

enter first string: hi
enter second string: hello
both strings are not equal
"""

# 21.wap to check whether marks are distinction or not.
# marks = int(input("enter your marks: "))
# if marks >= 75:
#     print(f"{marks} is distinction")
# else:
#     print(f"{marks} is not distinction")

"""
enter your marks: 85
85 is distinction

enter your marks: 60
60 is not distinction
"""

# 22.wap to check whether a number is a 2-digit or 3-digit number.
# n = int(input("enter a number: "))
# if 10 <= n <= 99:
#     print(f"{n} is a 2-digit number")
# else:
#     print(f"{n} is a 3-digit number")

"""
enter a number: 45
45 is a 2-digit number

enter a number: 456
456 is a 3-digit number
"""

# 23.wap to check whether a character is alphabet or digit.
# ch = input("enter a character: ")
# if ch.isalpha():
#     print(f"{ch} is an alphabet")
# else:
#     print(f"{ch} is a digit")

"""
enter a character: a
a is an alphabet

enter a character: 7
7 is a digit
"""

# 24.wap to check whether internet speed is fast or slow.
# speed = int(input("enter internet speed: "))
# if speed > 100:
#     print(f"{speed} Mbps is fast")
# else:
#     print(f"{speed} Mbps is slow")

"""
enter internet speed: 150
150 Mbps is fast

enter internet speed: 50
50 Mbps is slow
"""
