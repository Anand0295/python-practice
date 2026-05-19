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

# 16.wap to check whether battery percentage is low and power saving mode is needed using nested if.
# battery = int(input("enter battery percentage: "))

# if battery < 30:
#     if battery < 15:
#         print("power saving mode needed")
#     else:
#         print("battery is low")
# else:
#     print("battery level is good")

"""
enter battery percentage: 10
power saving mode needed

enter battery percentage: 25
battery is low

enter battery percentage: 80
battery level is good
"""

# 17.wap to check whether a product is in stock and eligible for discount using nested if.
# stock = input("is product in stock (yes/no): ")

# if stock == "yes":
#     amount = int(input("enter product amount: "))

#     if amount > 5000:
#         print("product eligible for discount")
#     else:
#         print("product not eligible for discount")
# else:
#     print("product out of stock")

"""
is product in stock (yes/no): yes
enter product amount: 7000
product eligible for discount
"""

# 18.wap to check whether a movie rating is above 8 and language is english using nested if.
# rating = float(input("enter movie rating: "))

# if rating > 8:
#     language = input("enter movie language: ")

#     if language == "english":
#         print("high rated english movie")
#     else:
#         print("high rated non-english movie")
# else:
#     print("movie rating is below 8")

"""
enter movie rating: 9
enter movie language: english
high rated english movie
"""

# 19.wap to check whether a number is palindrome and even using nested if.
# n = int(input("enter a number: "))
# rev = int(str(n)[::-1])

# if n == rev:
#     if n % 2 == 0:
#         print(f"{n} is even palindrome")
#     else:
#         print(f"{n} is palindrome but odd")
# else:
#     print(f"{n} is not palindrome")

"""
enter a number: 1221
1221 is palindrome but odd

enter a number: 2442
2442 is even palindrome

enter a number: 123
123 is not palindrome
"""

# 20.wap to check whether a student belongs to python batch and attendance is above 80 using nested if.
# batch = input("enter batch code: ")

# if batch[0:3].upper() == "PSP":
#     attendance = int(input("enter attendance percentage: "))

#     if attendance > 80:
#         print("python student with good attendance")
#     else:
#         print("python student with low attendance")
# else:
#     print("not a python batch student")

"""
enter batch code: psp_e9
enter attendance percentage: 85
python student with good attendance
"""

# 21.wap to check whether a user entered correct username and password using nested if.
# username = input("enter username: ")

# if username == "admin":
#     password = input("enter password: ")

#     if password == "admin123":
#         print("login successful")
#     else:
#         print("incorrect password")
# else:
#     print("incorrect username")

"""
enter username: admin
enter password: admin123
login successful
"""

# 22.wap to check whether a train is on time and seat is available using nested if.
# status = input("is train on time (yes/no): ")

# if status == "yes":
#     seat = input("is seat available (yes/no): ")

#     if seat == "yes":
#         print("seat booked successfully")
#     else:
#         print("no seats available")
# else:
#     print("train delayed")

"""
is train on time (yes/no): yes
is seat available (yes/no): yes
seat booked successfully
"""

# 23.wap to check whether a person is eligible for loan and has good credit score using nested if.
# salary = int(input("enter salary: "))

# if salary >= 30000:
#     credit = int(input("enter credit score: "))

#     if credit >= 750:
#         print("loan approved")
#     else:
#         print("poor credit score")
# else:
#     print("not eligible for loan")

"""
enter salary: 50000
enter credit score: 800
loan approved
"""

# 24.wap to check whether a number is Armstrong number and greater than 100 using nested if.
# n = int(input("enter a number: "))
# total = 0

# for i in str(n):
#     total += int(i) ** len(str(n))

# if n == total:
#     if n > 100:
#         print(f"{n} is Armstrong number and greater than 100")
#     else:
#         print(f"{n} is Armstrong number")
# else:
#     print(f"{n} is not Armstrong number")

"""
enter a number: 153
153 is Armstrong number and greater than 100

enter a number: 50
50 is not Armstrong number
"""

# 25.wap to check whether a mobile storage is above 80% and battery is below 20% using nested if.
# storage = int(input("enter storage percentage: "))

# if storage > 80:
#     battery = int(input("enter battery percentage: "))

#     if battery < 20:
#         print("storage high and battery low")
#     else:
#         print("storage high but battery sufficient")
# else:
#     print("storage usage normal")

"""
enter storage percentage: 90
enter battery percentage: 15
storage high and battery low
"""

# 26.wap to check whether a customer purchased above 5000 and has membership card using nested if.
# amount = int(input("enter purchase amount: "))

# if amount > 5000:
#     card = input("do you have membership card (yes/no): ")

#     if card == "yes":
#         print("eligible for special discount")
#     else:
#         print("membership card required")
# else:
#     print("purchase amount too low")

"""
enter purchase amount: 7000
do you have membership card (yes/no): yes
eligible for special discount
"""

# 27.wap to check whether a student passed theory and practical exams using nested if.
# theory = int(input("enter theory marks: "))

# if theory >= 35:
#     practical = int(input("enter practical marks: "))

#     if practical >= 35:
#         print("student passed both exams")
#     else:
#         print("failed in practical exam")
# else:
#     print("failed in theory exam")

"""
enter theory marks: 60
enter practical marks: 50
student passed both exams
"""

# 28.wap to check whether a vehicle speed exceeds limit and driver has license using nested if.
# speed = int(input("enter vehicle speed: "))

# if speed > 80:
#     license = input("do you have driving license (yes/no): ")

#     if license == "yes":
#         print("speed limit exceeded")
#     else:
#         print("speed limit exceeded and no license")
# else:
#     print("speed within limit")

"""
enter vehicle speed: 100
do you have driving license (yes/no): no
speed limit exceeded and no license
"""

# 29.wap to check whether a city belongs to Karnataka and language is Kannada using nested if.
# city = input("enter city name: ").lower()

# if city in ["bangalore", "mysore", "mangalore"]:
#     language = input("enter language: ").lower()

#     if language == "kannada":
#         print("city belongs to Karnataka and language is Kannada")
#     else:
#         print("city belongs to Karnataka but language is different")
# else:
#     print("city does not belong to Karnataka")

"""
enter city name: bangalore
enter language: kannada
city belongs to Karnataka and language is Kannada
"""

# 30.wap to check whether a bank account balance is above minimum and ATM pin is correct using nested if.
# balance = int(input("enter account balance: "))

# if balance >= 1000:
#     pin = int(input("enter ATM pin: "))

#     if pin == 1234:
#         print("transaction successful")
#     else:
#         print("incorrect ATM pin")
# else:
#     print("insufficient balance")

"""
enter account balance: 5000
enter ATM pin: 1234
transaction successful
"""

# 31.wap to check whether a triangle is valid and equilateral using nested if.
# a = int(input("enter side1: "))
# b = int(input("enter side2: "))
# c = int(input("enter side3: "))

# if a + b > c and b + c > a and a + c > b:
#     if a == b == c:
#         print("triangle is equilateral")
#     else:
#         print("triangle is valid but not equilateral")
# else:
#     print("invalid triangle")

"""
enter side1: 5
enter side2: 5
enter side3: 5
triangle is equilateral
"""

# 32.wap to check whether a number is positive and perfect square using nested if.
# n = int(input("enter a number: "))

# if n > 0:
#     if n ** 0.5 == int(n ** 0.5):
#         print(f"{n} is positive perfect square")
#     else:
#         print(f"{n} is positive but not perfect square")
# else:
#     print(f"{n} is not positive")

"""
enter a number: 25
25 is positive perfect square

enter a number: 10
10 is positive but not perfect square
"""

# 33.wap to check whether a user is admin and has edit permission using nested if.
# role = input("enter role: ")

# if role == "admin":
#     permission = input("do you have edit permission (yes/no): ")

#     if permission == "yes":
#         print("edit access granted")
#     else:
#         print("no edit permission")
# else:
#     print("not an admin")

"""
enter role: admin
do you have edit permission (yes/no): yes
edit access granted
"""

# 34.wap to check whether a person age is above 18 and passport is available using nested if.
# age = int(input("enter age: "))

# if age > 18:
#     passport = input("do you have passport (yes/no): ")

#     if passport == "yes":
#         print("eligible for international travel")
#     else:
#         print("passport required")
# else:
#     print("not eligible")

"""
enter age: 25
do you have passport (yes/no): yes
eligible for international travel
"""

# 35.wap to check whether rainfall is heavy and flood warning is needed using nested if.
# rainfall = int(input("enter rainfall in mm: "))

# if rainfall > 100:
#     river = input("is river level high (yes/no): ")

#     if river == "yes":
#         print("flood warning needed")
#     else:
#         print("heavy rainfall but no flood warning")
# else:
#     print("normal rainfall")

"""
enter rainfall in mm: 150
is river level high (yes/no): yes
flood warning needed
"""
