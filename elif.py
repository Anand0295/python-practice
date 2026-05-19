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
# signal = input("enter traffic signal: ")

# if signal == "red":
#     print("stop")
# elif signal == "yellow":
#     print("ready")
# elif signal == "green":
#     print("go")
# else:
#     print("invalid signal")

"""
enter traffic signal: red
stop

enter traffic signal: yellow
ready

enter traffic signal: green
go
"""

# 22.wap to create a menu-driven hotel ordering system using elif.

# print("welcome to hotel")
# print("choose your course")
# print("1.breakfast")
# print("2.lunch")
# print("3.dinner")

# course = int(input("enter your choice: "))

# if course == 1:
#     print("breakfast menu")
#     print("1.idli - 40")
#     print("2.dosa - 50")
#     print("3.poori - 60")
#     print("4.pongal - 70")
#     print("5.vada - 30")

#     item = int(input("enter item number: "))

#     if item == 1:
#         print("idli ordered")
#         print("total bill = 40")
#     elif item == 2:
#         print("dosa ordered")
#         print("total bill = 50")
#     elif item == 3:
#         print("poori ordered")
#         print("total bill = 60")
#     elif item == 4:
#         print("pongal ordered")
#         print("total bill = 70")
#     elif item == 5:
#         print("vada ordered")
#         print("total bill = 30")
#     else:
#         print("invalid item")

# elif course == 2:
#     print("lunch menu")
#     print("1.meals - 120")
#     print("2.biryani - 180")
#     print("3.fried rice - 150")
#     print("4.noodles - 140")
#     print("5.curd rice - 80")

#     item = int(input("enter item number: "))

#     if item == 1:
#         print("meals ordered")
#         print("total bill = 120")
#     elif item == 2:
#         print("biryani ordered")
#         print("total bill = 180")
#     elif item == 3:
#         print("fried rice ordered")
#         print("total bill = 150")
#     elif item == 4:
#         print("noodles ordered")
#         print("total bill = 140")
#     elif item == 5:
#         print("curd rice ordered")
#         print("total bill = 80")
#     else:
#         print("invalid item")

# elif course == 3:
#     print("dinner menu")
#     print("1.chapati - 60")
#     print("2.parotta - 80")
#     print("3.idiyappam - 90")
#     print("4.paneer dosa - 100")
#     print("5.tomato rice - 70")

#     item = int(input("enter item number: "))

#     if item == 1:
#         print("chapati ordered")
#         print("total bill = 60")
#     elif item == 2:
#         print("parotta ordered")
#         print("total bill = 80")
#     elif item == 3:
#         print("idiyappam ordered")
#         print("total bill = 90")
#     elif item == 4:
#         print("paneer dosa ordered")
#         print("total bill = 100")
#     elif item == 5:
#         print("tomato rice ordered")
#         print("total bill = 70")
#     else:
#         print("invalid item")

# else:
#     print("invalid course")

"""
welcome to hotel
choose your course
1.breakfast
2.lunch
3.dinner

enter your choice: 2

lunch menu
1.meals - 120
2.biryani - 180
3.fried rice - 150
4.noodles - 140
5.curd rice - 80

enter item number: 2
biryani ordered
total bill = 180
"""

# 23.wap to check whether a given year is leap year or century year using elif.
# year = int(input("enter a year: "))

# if year % 400 == 0:
#     print(f"{year} is leap year")
# elif year % 100 == 0:
#     print(f"{year} is century year")
# elif year % 4 == 0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is normal year")

"""
enter a year: 2000
2000 is leap year

enter a year: 1900
1900 is century year

enter a year: 2024
2024 is leap year

enter a year: 2023
2023 is normal year
"""

# 24.wap to classify angles as acute, right, obtuse, or straight using elif.
# angle = int(input("enter angle value: "))

# if angle < 90:
#     print("acute angle")
# elif angle == 90:
#     print("right angle")
# elif angle < 180:
#     print("obtuse angle")
# else:
#     print("straight angle")

"""
enter angle value: 45
acute angle

enter angle value: 90
right angle

enter angle value: 120
obtuse angle

enter angle value: 180
straight angle
"""

# 25.wap to check whether a shape is square, rectangle, or invalid using elif.
# length = int(input("enter length: "))
# breadth = int(input("enter breadth: "))

# if length == breadth:
#     print("square")
# elif length > 0 and breadth > 0:
#     print("rectangle")
# else:
#     print("invalid shape")

"""
enter length: 10
enter breadth: 10
square

enter length: 10
enter breadth: 5
rectangle

enter length: -2
enter breadth: 5
invalid shape
"""

# 26.wap to classify a triangle as equilateral, isosceles, or scalene using elif.
# a = int(input("enter first side: "))
# b = int(input("enter second side: "))
# c = int(input("enter third side: "))

# if a == b == c:
#     print("equilateral triangle")
# elif a == b or b == c or a == c:
#     print("isosceles triangle")
# else:
#     print("scalene triangle")

"""
enter first side: 5
enter second side: 5
enter third side: 5
equilateral triangle

enter first side: 5
enter second side: 5
enter third side: 8
isosceles triangle

enter first side: 3
enter second side: 4
enter third side: 5
scalene triangle
"""

# 27.wap to check whether a number is palindrome, Armstrong, or normal number using elif.
# n = int(input("enter a number: "))

# if str(n) == str(n)[::-1]:
#     print(f"{n} is palindrome")
# elif n == 153:
#     print(f"{n} is armstrong number")
# else:
#     print(f"{n} is normal number")

"""
enter a number: 121
121 is palindrome

enter a number: 153
153 is armstrong number

enter a number: 145
145 is normal number
"""

# 28.wap to assign salary category as low, medium, or high income using elif.
# salary = int(input("enter salary: "))

# if salary < 30000:
#     print("low income")
# elif salary <= 70000:
#     print("medium income")
# else:
#     print("high income")

"""
enter salary: 20000
low income

enter salary: 50000
medium income

enter salary: 100000
high income
"""

# 29.wap to check whether exam marks are fail, pass, first class, or distinction using elif.
# marks = int(input("enter marks: "))

# if marks < 35:
#     print("fail")
# elif marks < 60:
#     print("pass")
# elif marks < 75:
#     print("first class")
# else:
#     print("distinction")

"""
enter marks: 20
fail

enter marks: 50
pass

enter marks: 65
first class

enter marks: 90
distinction
"""

# 30.wap to classify age group ticket prices using elif.
# age = int(input("enter age: "))

# if age < 5:
#     print("free ticket")
# elif age < 18:
#     print("child ticket")
# elif age < 60:
#     print("adult ticket")
# else:
#     print("senior citizen ticket")

"""
enter age: 3
free ticket

enter age: 10
child ticket

enter age: 30
adult ticket

enter age: 70
senior citizen ticket
"""

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
