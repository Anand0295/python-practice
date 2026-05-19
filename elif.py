# if condition:
#     |----------|
#     |   TSB    |
#     |----------|
# elif condition:
#     |----------|
#     |   TSB    |
#     |----------|
#  else:
#     |----------|
#     |   FSB    |
#     |----------|

# 1.wap to check whether a number is positive, negative, or zero using elif.
# n = int(input("enter a number: "))
# if n > 0:
#     print(f"{n} is positive")
# elif n < 0:
#     print(f"{n} is negative")
# else:
#     print(f"{n} is zero")

"""
enter a number: 5
5 is positive

enter a number: -10
-10 is negative

enter a number: 0
0 is zero
"""

# 2.wap to check whether a student got pass, fail, or distinction using elif.
# marks = int(input("enter your marks: "))
# if marks >= 75:
#     print(f"{marks} is distinction")
# elif marks >= 35:
#     print(f"{marks} is pass")
# else:
#     print(f"{marks} is fail")

"""
enter your marks: 90
90 is distinction

enter your marks: 50
50 is pass

enter your marks: 20
20 is fail
"""

# 3.wap to find the greatest among two numbers or equal using elif.
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# if a > b:
#     print(f"{a} is greater")
# elif b > a:
#     print(f"{b} is greater")
# else:
#     print("both numbers are equal")

"""
enter first number: 20
enter second number: 10
20 is greater

enter first number: 10
enter second number: 30
30 is greater

enter first number: 5
enter second number: 5
both numbers are equal
"""

# 4.wap to check whether a character is vowel, consonant, or digit using elif.
# ch = input("enter a character: ")
# if ch in "aeiouAEIOU":
#     print(f"{ch} is vowel")
# elif ch.isalpha():
#     print(f"{ch} is consonant")
# else:
#     print(f"{ch} is digit")

"""
enter a character: a
a is vowel

enter a character: b
b is consonant

enter a character: 7
7 is digit
"""

# 5.wap to check whether a number is divisible by 2, 3, or 5 using elif.
# n = int(input("enter a number: "))
# if n % 2 == 0:
#     print(f"{n} is divisible by 2")
# elif n % 3 == 0:
#     print(f"{n} is divisible by 3")
# elif n % 5 == 0:
#     print(f"{n} is divisible by 5")
# else:
#     print(f"{n} is not divisible by 2, 3, or 5")

"""
enter a number: 8
8 is divisible by 2

enter a number: 9
9 is divisible by 3

enter a number: 25
25 is divisible by 5

enter a number: 7
7 is not divisible by 2, 3, or 5
"""

# 6.wap to assign grades A, B, C, or Fail based on marks using elif.
# marks = int(input("enter your marks: "))
# if marks >= 90:
#     print("grade A")
# elif marks >= 70:
#     print("grade B")
# elif marks >= 35:
#     print("grade C")
# else:
#     print("fail")

"""
enter your marks: 95
grade A

enter your marks: 75
grade B

enter your marks: 50
grade C

enter your marks: 20
fail
"""

# 7.wap to check whether a person is child, teenager, adult, or senior citizen using elif.
# age = int(input("enter your age: "))
# if age < 13:
#     print("child")
# elif age < 20:
#     print("teenager")
# elif age < 60:
#     print("adult")
# else:
#     print("senior citizen")

"""
enter your age: 10
child

enter your age: 16
teenager

enter your age: 35
adult

enter your age: 70
senior citizen
"""

# 8.wap to check whether temperature is cold, warm, or hot using elif.
# temp = int(input("enter temperature: "))
# if temp < 20:
#     print("cold")
# elif temp <= 30:
#     print("warm")
# else:
#     print("hot")

"""
enter temperature: 15
cold

enter temperature: 28
warm

enter temperature: 40
hot
"""

# 9.wap to check whether a number is single-digit, double-digit, or three-digit using elif.
# n = int(input("enter a number: "))
# if 0 <= n <= 9:
#     print(f"{n} is single-digit")
# elif 10 <= n <= 99:
#     print(f"{n} is double-digit")
# else:
#     print(f"{n} is three-digit")

"""
enter a number: 5
5 is single-digit

enter a number: 45
45 is double-digit

enter a number: 456
456 is three-digit
"""

# 10.wap to create a simple calculator for +, -, *, / using elif.
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# op = input("enter operator: ")

# if op == "+":
#     print(f"sum is {a+b}")
# elif op == "-":
#     print(f"difference is {a-b}")
# elif op == "*":
#     print(f"product is {a*b}")
# elif op == "/":
#     print(f"division is {a/b}")
# else:
#     print("invalid operator")

"""
enter first number: 10
enter second number: 20
enter operator: +
sum is 30

enter first number: 20
enter second number: 10
enter operator: -
difference is 10

enter first number: 5
enter second number: 4
enter operator: *
product is 20

enter first number: 20
enter second number: 5
enter operator: /
division is 4.0
"""


# 11.wap to check whether a day is weekday or weekend using elif.
# day = input("enter a day: ")

# if day in ["Saturday", "Sunday"]:
#     print(f"{day} is weekend")
# elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
#     print(f"{day} is weekday")
# else:
#     print("invalid day")

"""
enter a day: Sunday
Sunday is weekend

enter a day: Monday
Monday is weekday
"""

# 12.wap to check whether a month has 28, 30, or 31 days using elif.
# month = input("enter month name: ")

# if month == "February":
#     print(f"{month} has 28 days")
# elif month in ["April", "June", "September", "November"]:
#     print(f"{month} has 30 days")
# elif month in ["January", "March", "May", "July", "August", "October", "December"]:
#     print(f"{month} has 31 days")
# else:
#     print("invalid month")

"""
enter month name: February
February has 28 days

enter month name: April
April has 30 days

enter month name: May
May has 31 days
"""

# 13.wap to check whether a character is uppercase, lowercase, digit, or special character using elif.
# ch = input("enter a character: ")

# if ch.isupper():
#     print(f"{ch} is uppercase")
# elif ch.islower():
#     print(f"{ch} is lowercase")
# elif ch.isdigit():
#     print(f"{ch} is digit")
# else:
#     print(f"{ch} is special character")

"""
enter a character: A
A is uppercase

enter a character: b
b is lowercase

enter a character: 7
7 is digit

enter a character: @
@ is special character
"""

# 14.wap to check whether a person is eligible for school, college, or job using elif.
# age = int(input("enter your age: "))

# if age < 5:
#     print("not eligible for school")
# elif age < 18:
#     print("eligible for school")
# elif age < 23:
#     print("eligible for college")
# else:
#     print("eligible for job")

"""
enter your age: 10
eligible for school

enter your age: 20
eligible for college

enter your age: 25
eligible for job
"""

# 15.wap to classify BMI as underweight, normal, overweight, or obese using elif.
# bmi = float(input("enter BMI value: "))

# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal")
# elif bmi < 30:
#     print("overweight")
# else:
#     print("obese")

"""
enter BMI value: 17
underweight

enter BMI value: 22
normal

enter BMI value: 28
overweight

enter BMI value: 35
obese
"""

# 16.wap to check whether a number belongs to range 1-10, 11-50, or above 50 using elif.
# n = int(input("enter a number: "))

# if 1 <= n <= 10:
#     print(f"{n} belongs to range 1-10")
# elif 11 <= n <= 50:
#     print(f"{n} belongs to range 11-50")
# else:
#     print(f"{n} is above 50")

"""
enter a number: 5
5 belongs to range 1-10

enter a number: 25
25 belongs to range 11-50

enter a number: 80
80 is above 50
"""

# 17.wap to check whether internet speed is slow, medium, or fast using elif.
# speed = int(input("enter internet speed: "))

# if speed < 10:
#     print("slow")
# elif speed <= 50:
#     print("medium")
# else:
#     print("fast")

"""
enter internet speed: 5
slow

enter internet speed: 30
medium

enter internet speed: 100
fast
"""

# 18.wap to assign movie category based on rating using elif.
# rating = float(input("enter movie rating: "))

# if rating >= 8:
#     print("blockbuster")
# elif rating >= 6:
#     print("hit")
# elif rating >= 4:
#     print("average")
# else:
#     print("flop")

"""
enter movie rating: 9
blockbuster

enter movie rating: 7
hit

enter movie rating: 5
average

enter movie rating: 2
flop
"""

# 19.wap to check whether battery percentage is low, medium, or full using elif.
# battery = int(input("enter battery percentage: "))

# if battery < 20:
#     print("low battery")
# elif battery <= 80:
#     print("medium battery")
# else:
#     print("full battery")

"""
enter battery percentage: 10
low battery

enter battery percentage: 50
medium battery

enter battery percentage: 95
full battery
"""

# 20.wap to check whether a train is early, on time, or delayed using elif.
# status = input("enter train status: ")

# if status == "early":
#     print("train is early")
# elif status == "ontime":
#     print("train is on time")
# else:
#     print("train is delayed")

"""
enter train status: early
train is early

enter train status: ontime
train is on time

enter train status: delayed
train is delayed
"""

# 21.wap to create a traffic signal action checker using elif.

# 22.wap to create a menu-driven hotel ordering system using elif.

# 23.wap to check whether a given year is leap year or century year using elif.

# 24.wap to classify angles as acute, right, obtuse, or straight using elif.

# 25.wap to check whether a shape is square, rectangle, or invalid using elif.

# 26.wap to classify a triangle as equilateral, isosceles, or scalene using elif.

# 27.wap to check whether a number is palindrome, Armstrong, or normal number using elif.

# 28.wap to assign salary category as low, medium, or high income using elif.

# 29.wap to check whether exam marks are fail, pass, first class, or distinction using elif.

# 30.wap to classify age group ticket prices using elif.

# 31.wap to create a login system with admin, user, or guest access using elif.

# 32.wap to classify weather condition as rainy, sunny, cloudy, or snowy using elif.

# 33.wap to check whether a character is alphabet, digit, whitespace, or special character using elif.

# 34.wap to classify numbers as even positive, odd positive, even negative, or odd negative using elif.

# 35.wap to classify a number as prime, composite, or neither using elif.

# 36.wap to create a unit converter menu using elif.

# 37.wap to check whether a vehicle is bike, car, bus, or truck using elif.

# 38.wap to classify employee work hours as part-time, full-time, or overtime using elif.

# 39.wap to assign tax percentage based on salary slabs using elif.

# 40.wap to classify students into house groups based on roll number using elif.

# 41.wap to create a simple ATM menu system using elif.

# 42.wap to classify electricity bill based on units consumed using elif.

# 43.wap to create a simple banking transaction menu using elif.

# 44.wap to classify mobile storage usage as low, medium, high, or full using elif.

# 45.wap to create a simple e-commerce discount system using elif.

# 46.wap to classify a number as perfect square, perfect cube, or both using elif.

# 47.wap to create a simple railway reservation category checker using elif.

# 48.wap to classify password strength as weak, medium, or strong using elif.

# 49.wap to create a simple grading dashboard using elif.

# 50.wap to create a mini smart home controller using elif.

# 51.wap to print fizzbuzz if the given number is divisible by 5 and 3, else print fizz if the given number is divisible by 5, else print buzz if the given number is divisible by 3.

# 52.wap to calculate total loan amount with interest based on loan type using elif.

# 53.wap to check whether a student belongs to python full stack, java full stack, or testing based on batch code using elif.

# 54.wap to welcome the tourist in their state language based on entered city using elif.

# 55.wap to create a simple restaurant menu billing system using elif.
