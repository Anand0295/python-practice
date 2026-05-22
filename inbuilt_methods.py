# =========================
# STRING METHODS
# =========================

# 1. WAP to convert string into uppercase using upper()

# SYNTAX:
# string.upper()

# s --> original string
# upper() --> converts lowercase into uppercase

# hello --> HELLO

# s = "hello"
# print(s.upper())

"""
HELLO
"""


# 2. WAP to convert string into lowercase using lower()

# SYNTAX:
# string.lower()

# HELLO --> hello

# s = "HELLO"
# print(s.lower())

"""
hello
"""


# 3. WAP to swap uppercase into lowercase and vice versa using swapcase()

# SYNTAX:
# string.swapcase()

# H --> h
# e --> E

# s = "HeLLo"
# print(s.swapcase())

"""
hEllO
"""


# 4. WAP to capitalize first letter using capitalize()

# SYNTAX:
# string.capitalize()

# first letter --> uppercase
# remaining --> lowercase

# python programming --> Python programming

# s = "python programming"
# print(s.capitalize())

"""
Python programming
"""


# 5. WAP to convert every word first letter into uppercase using title()

# SYNTAX:
# string.title()

# every word first letter --> uppercase

# python programming --> Python Programming

# s = "python programming language"
# print(s.title())

"""
Python Programming Language
"""


# 6. WAP to remove spaces from both sides using strip()

# SYNTAX:
# string.strip()

# left spaces removed
# right spaces removed

# "   hello   " --> "hello"

# s = "   hello   "
# print(s.strip())

"""
hello
"""


# 7. WAP to remove left side spaces using lstrip()

# SYNTAX:
# string.lstrip()

# left spaces removed only

# "   hello" --> "hello"

# s = "   hello"
# print(s.lstrip())

"""
hello
"""


# 8. WAP to remove right side spaces using rstrip()

# SYNTAX:
# string.rstrip()

# right spaces removed only

# "hello   " --> "hello"

# s = "hello   "
# print(s.rstrip())

"""
hello
"""


# 9. WAP to replace one character with another using replace()

# SYNTAX:
# string.replace(old,new)

# a --> @

# banana --> b@n@n@

# s = "banana"
# print(s.replace("a", "@"))

"""
b@n@n@
"""


# 10. WAP to replace all spaces with hyphen using replace()

# SYNTAX:
# string.replace(" ","-")

# hello python world
# hello-python-world

# s = "hello python world"
# print(s.replace(" ", "-"))

"""
hello-python-world
"""


# 11. WAP to split string into list using split()

# SYNTAX:
# string.split()

# words separated into list

# python java c
# ['python','java','c']

# s = "python java c"
# print(s.split())

"""
['python', 'java', 'c']
"""


# 12. WAP to split string from right side using rsplit()

# SYNTAX:
# string.rsplit(separator,maxsplit)

# right side splitting

# one two three four

# s = "one two three four"
# print(s.rsplit(" ", 2))

"""
['one two', 'three', 'four']
"""


# 13. WAP to count occurrences of a character using count()

# SYNTAX:
# string.count(value)

# banana
# a --> 3 times

# s = "banana"
# print(s.count("a"))

"""
3
"""


# 14. WAP to count occurrences of a word in sentence

# SYNTAX:
# string.count(word)

# hi hello hi python hi
# hi --> 3

# s = "hi hello hi python hi"
# print(s.count("hi"))

"""
3
"""


# 15. WAP to join list elements into string using join()

# SYNTAX:
# "separator".join(iterable)

# list --> string

# ['python','java','c']
# python java c

# lst = ["python", "java", "c"]
# print(" ".join(lst))

"""
python java c
"""


# 16. WAP to check whether string starts with given word using startswith()

# SYNTAX:
# string.startswith(value)

# python programming
# starts with python --> True

# s = "python programming"
# print(s.startswith("python"))

"""
True
"""


# 17. WAP to check whether string ends with given word using endswith()

# SYNTAX:
# string.endswith(value)

# hello.py
# ends with .py --> True

# s = "hello.py"
# print(s.endswith(".py"))

"""
True
"""


# 18. WAP to find first index position using index()

# SYNTAX:
# string.index(value)

# banana
# first a --> index 1

# s = "banana"
# print(s.index("a"))

"""
1
"""


# 19. WAP to find last index position using rindex()

# SYNTAX:
# string.rindex(value)

# banana
# last a --> index 5

# s = "banana"
# print(s.rindex("a"))

"""
5
"""


# 20. WAP to find first occurrence using find()

# SYNTAX:
# string.find(value)

# banana
# first n --> index 2

# s = "banana"
# print(s.find("n"))

"""
2
"""


# 21. WAP to find last occurrence using rfind()

# SYNTAX:
# string.rfind(value)

# banana
# last n --> index 4

# s = "banana"
# print(s.rfind("n"))

"""
4
"""


# 22. WAP to check whether string is uppercase using isupper()

# SYNTAX:
# string.isupper()

# HELLO --> uppercase

# s = "HELLO"
# print(s.isupper())

"""
True
"""


# 23. WAP to check whether string is lowercase using islower()

# SYNTAX:
# string.islower()

# hello --> lowercase

# s = "hello"
# print(s.islower())

"""
True
"""


# 24. WAP to check whether string contains only digits using isdigit()

# SYNTAX:
# string.isdigit()

# 12345 --> digits only

# s = "12345"
# print(s.isdigit())

"""
True
"""


# 25. WAP to check whether string contains only alphabets using isalpha()

# SYNTAX:
# string.isalpha()

# python --> alphabets only

# s = "python"
# print(s.isalpha())

"""
True
"""


# 26. WAP to check whether string contains alphabets and numbers using isalnum()

# SYNTAX:
# string.isalnum()

# python123 --> alphabets + numbers

# s = "python123"
# print(s.isalnum())

"""
True
"""


# 27. WAP to check whether string contains only spaces using isspace()

# SYNTAX:
# string.isspace()

# "   " --> spaces only

# s = "   "
# print(s.isspace())

"""
True
"""


# 28. WAP to check whether string is title case using istitle()

# SYNTAX:
# string.istitle()

# Hello Python --> title case

# s = "Hello Python"
# print(s.istitle())

"""
True
"""


# 29. WAP to replace vowels with * using replace()

# SYNTAX:
# string.replace(old,new)

# education
# *d*c*t**n

# s = "education"
# s = s.replace("a", "*")
# s = s.replace("e", "*")
# s = s.replace("i", "*")
# s = s.replace("o", "*")
# s = s.replace("u", "*")
# print(s)

"""
*d*c*t**n
"""


# 30. WAP to split email using @ symbol

# SYNTAX:
# string.split("@")

# abc@gmail.com
# ['abc','gmail.com']

# email = "abc@gmail.com"
# print(email.split("@"))

"""
['abc', 'gmail.com']
"""


# 31. WAP to count number of spaces in string

# SYNTAX:
# string.count(" ")

# hello python world
# spaces --> 2

# s = "hello python world"
# print(s.count(" "))

"""
2
"""


# 32. WAP to join tuple elements into string

# SYNTAX:
# "separator".join(tuple)

# tuple --> string

# t = ("python", "java", "c")
# print("-".join(t))

"""
python-java-c
"""


# 33. WAP to remove special characters using replace()

# SYNTAX:
# string.replace(old,"")

# @ # ! removed

# hello@123#python!
# hello123python

# s = "hello@123#python!"
# s = s.replace("@", "")
# s = s.replace("#", "")
# s = s.replace("!", "")
# print(s)

"""
hello123python
"""


# 34. WAP to check whether filename ends with .py

# SYNTAX:
# string.endswith(".py")

# program.py --> True

# file = "program.py"
# print(file.endswith(".py"))

"""
True
"""


# 35. WAP to extract domain name from email

# SYNTAX:
# string.split("@")[1]

# abc@gmail.com
# gmail.com

# email = "abc@gmail.com"
# print(email.split("@")[1])

"""
gmail.com
"""


# 36. WAP to convert snake_case into title case

# SYNTAX:
# string.replace("_"," ").title()

# python_programming_language
# Python Programming Language

# s = "python_programming_language"
# print(s.replace("_", " ").title())

"""
Python Programming Language
"""


# 37. WAP to count vowels using count()

# SYNTAX:
# string.count(vowel)

# education
# vowels --> 5

# s = "education"

# count = 0

# count += s.count("a")
# count += s.count("e")
# count += s.count("i")
# count += s.count("o")
# count += s.count("u")

# print(count)

"""
5
"""


# 38. WAP to remove commas from number string

# SYNTAX:
# string.replace(",","")

# 1,00,000
# 100000

# s = "1,00,000"
# print(s.replace(",", ""))

"""
100000
"""


# 39. WAP to check whether mobile number contains only digits

# SYNTAX:
# string.isdigit()

# 9876543210 --> digits only

# mobile = "9876543210"
# print(mobile.isdigit())

"""
True
"""


# 40. WAP to reverse words using split() and join()

# SYNTAX:
# split() → reverse() → join()

# hello python world
# world python hello

# s = "hello python world"

# words = s.split()

# words.reverse()

# print(" ".join(words))

"""
world python hello
"""

# =========================
# LIST METHODS
# =========================

# 41. WAP to add element into list using append()

# SYNTAX:
# list.append(value)

# append() --> adds single element at end

# [1,2,3] + 4

# lst = [1, 2, 3]
# lst.append(4)

# print(lst)

"""
[1, 2, 3, 4]
"""


# 42. WAP to add multiple elements using extend()

# SYNTAX:
# list.extend(iterable)

# extend() --> adds multiple values

# [1,2] + [3,4]

# lst = [1, 2]
# lst.extend([3, 4])

# print(lst)

"""
[1, 2, 3, 4]
"""


# 43. WAP to insert element at specific position using insert()

# SYNTAX:
# list.insert(index,value)

# insert at index 1

# [10,20,30]
# add 15

# lst = [10, 20, 30]
# lst.insert(1, 15)

# print(lst)

"""
[10, 15, 20, 30]
"""


# 44. WAP to remove element using remove()

# SYNTAX:
# list.remove(value)

# removes first occurrence

# [1,2,3,2]
# remove 2

# lst = [1, 2, 3, 2]
# lst.remove(2)

# print(lst)

"""
[1, 3, 2]
"""


# 45. WAP to remove last element using pop()

# SYNTAX:
# list.pop()

# removes last value

# [10,20,30]

# lst = [10, 20, 30]

# lst.pop()

# print(lst)

"""
[10, 20]
"""


# 46. WAP to remove element at specific index using pop(index)

# SYNTAX:
# list.pop(index)

# remove index 1

# [10,20,30]

# lst = [10, 20, 30]

# lst.pop(1)

# print(lst)

"""
[10, 30]
"""


# 47. WAP to clear complete list using clear()

# SYNTAX:
# list.clear()

# removes all elements

# [1,2,3] --> []

# lst = [1, 2, 3]

# lst.clear()

# print(lst)

"""
[]
"""


# 48. WAP to delete list using del

# SYNTAX:
# del variable

# deletes complete list

# lst = [1, 2, 3]

# del lst

# print(lst)

"""
NameError
"""


# 49. WAP to reverse list using reverse()

# SYNTAX:
# list.reverse()

# [1,2,3]
# [3,2,1]

# lst = [1, 2, 3]

# lst.reverse()

# print(lst)

"""
[3, 2, 1]
"""


# 50. WAP to sort list in ascending order using sort()

# SYNTAX:
# list.sort()

# ascending order

# [4,1,3,2]

# lst = [4, 1, 3, 2]

# lst.sort()

# print(lst)

"""
[1, 2, 3, 4]
"""


# 51. WAP to sort list in descending order using sort(reverse=True)

# SYNTAX:
# list.sort(reverse=True)

# descending order

# [1,2,3,4]
# [4,3,2,1]

# lst = [1, 2, 3, 4]

# lst.sort(reverse=True)

# print(lst)

"""
[4, 3, 2, 1]
"""


# 52. WAP to count occurrences of element using count()

# SYNTAX:
# list.count(value)

# count of 2

# [1,2,2,3,2]

# lst = [1, 2, 2, 3, 2]

# print(lst.count(2))

"""
3
"""


# 53. WAP to find index of element using index()

# SYNTAX:
# list.index(value)

# first index of 20

# [10,20,30]

# lst = [10, 20, 30]

# print(lst.index(20))

"""
1
"""


# 54. WAP to append list inside another list

# SYNTAX:
# list.append(list)

# nested list created

# [1,2] + [3,4]

# lst1 = [1, 2]
# lst2 = [3, 4]

# lst1.append(lst2)

# print(lst1)

"""
[1, 2, [3, 4]]
"""


# 55. WAP to extend string into list

# SYNTAX:
# list.extend(string)

# each character added separately

# "python"

# lst = [1, 2]

# lst.extend("python")

# print(lst)

"""
[1, 2, 'p', 'y', 't', 'h', 'o', 'n']
"""


# 56. WAP to insert list at specific index

# SYNTAX:
# list.insert(index,list)

# list inserted as single element

# lst = [1, 2, 5]

# lst.insert(2, [3, 4])

# print(lst)

"""
[1, 2, [3, 4], 5]
"""


# 57. WAP to remove duplicate values from list

# SYNTAX:
# list(set(list))

# duplicates removed

# [1,2,2,3]

# lst = [1, 2, 2, 3]

# lst = list(set(lst))

# print(lst)

"""
[1, 2, 3]
"""


# 58. WAP to pop all elements one by one

# SYNTAX:
# while len(list)>0:
#     list.pop()

# removes elements one by one

# [1,2,3]

# lst = [1, 2, 3]

# while len(lst) > 0:
#     print(lst.pop())

"""
3
2
1
"""


# 59. WAP to sort string list alphabetically

# SYNTAX:
# list.sort()

# alphabetical sorting

# ["banana","apple","cat"]

# lst = ["banana", "apple", "cat"]

# lst.sort()

# print(lst)

"""
['apple', 'banana', 'cat']
"""


# 60. WAP to reverse numeric list

# SYNTAX:
# list.reverse()

# [10,20,30]
# [30,20,10]

# lst = [10, 20, 30]

# lst.reverse()

# print(lst)

"""
[30, 20, 10]
"""


# 61. WAP to count even numbers in list

# SYNTAX:
# number%2==0

# even --> divisible by 2

# [1,2,3,4,6]

# lst = [1, 2, 3, 4, 6]

# count = 0

# for i in lst:

#     if i % 2 == 0:
#         count += 1

# print(count)

"""
3
"""


# 62. WAP to count odd numbers in list

# SYNTAX:
# number%2!=0

# odd numbers

# [1,2,3,5]

# lst = [1, 2, 3, 5]

# count = 0

# for i in lst:

#     if i % 2 != 0:
#         count += 1

# print(count)

"""
3
"""


# 63. WAP to create list of squares

# SYNTAX:
# number**2

# 1² 2² 3²

# lst = [1, 2, 3, 4]

# res = []

# for i in lst:
#     res.append(i**2)

# print(res)

"""
[1, 4, 9, 16]
"""


# 64. WAP to create list of cubes

# SYNTAX:
# number**3

# 1³ 2³ 3³

# lst = [1, 2, 3]

# res = []

# for i in lst:
#     res.append(i**3)

# print(res)

"""
[1, 8, 27]
"""


# 65. WAP to merge two lists using extend()

# SYNTAX:
# list.extend(list)

# [1,2] + [3,4]

# lst1 = [1, 2]
# lst2 = [3, 4]

# lst1.extend(lst2)

# print(lst1)

"""
[1, 2, 3, 4]
"""


# 66. WAP to remove all negative numbers from list

# SYNTAX:
# number>=0

# negatives removed

# [-1,2,-3,4]

# lst = [-1, 2, -3, 4]

# res = []

# for i in lst:

#     if i >= 0:
#         res.append(i)

# print(res)

"""
[2, 4]
"""


# 67. WAP to find largest element in list

# SYNTAX:
# max(list)

# largest value

# [10,50,20]

# lst = [10, 50, 20]

# print(max(lst))

"""
50
"""


# 68. WAP to find smallest element in list

# SYNTAX:
# min(list)

# smallest value

# [10,50,20]

# lst = [10, 50, 20]

# print(min(lst))

"""
10
"""


# 69. WAP to insert element before last position

# SYNTAX:
# list.insert(-1,value)

# insert before last

# [1,2,4]

# lst = [1, 2, 4]

# lst.insert(-1, 3)

# print(lst)

"""
[1, 2, 3, 4]
"""


# 70. WAP to remove all occurrences of given element

# SYNTAX:
# while value in list:
#     list.remove(value)

# remove all 2

# [1,2,2,3,2]

# lst = [1, 2, 2, 3, 2]

# while 2 in lst:
#     lst.remove(2)

# print(lst)

"""
[1, 3]
"""

# =========================
# TUPLE
# =========================

# 71. WAP to create tuple using packing

# SYNTAX:
# t = value1,value2,value3

# packing --> multiple values into tuple

# 10 20 30 --> tuple

# t = 10, 20, 30

# print(t)

"""
(10, 20, 30)
"""


# 72. WAP to unpack tuple values into variables

# SYNTAX:
# a,b,c = tuple

# unpacking --> tuple values into variables

# (1,2,3)

# t = (1, 2, 3)

# a, b, c = t

# print(a)
# print(b)
# print(c)

"""
1
2
3
"""


# 73. WAP to count occurrences using tuple count()

# SYNTAX:
# tuple.count(value)

# count of 2

# (1,2,2,3)

# t = (1, 2, 2, 3)

# print(t.count(2))

"""
2
"""


# 74. WAP to find index position using tuple index()

# SYNTAX:
# tuple.index(value)

# index of 30

# (10,20,30)

# t = (10, 20, 30)

# print(t.index(30))

"""
2
"""


# 75. WAP to create single value tuple

# SYNTAX:
# (value,)

# comma mandatory

# (10,)

# t = (10,)

# print(t)

# print(type(t))

"""
(10,)
<class 'tuple'>
"""


# 76. WAP to concatenate two tuples

# SYNTAX:
# tuple1 + tuple2

# (1,2) + (3,4)

# t1 = (1, 2)
# t2 = (3, 4)

# print(t1 + t2)

"""
(1, 2, 3, 4)
"""


# 77. WAP to replicate tuple elements

# SYNTAX:
# tuple * number

# repeat tuple

# (1,2) * 3

# t = (1, 2)

# print(t * 3)

"""
(1, 2, 1, 2, 1, 2)
"""


# 78. WAP to convert list into tuple

# SYNTAX:
# tuple(list)

# [1,2,3] --> tuple

# lst = [1, 2, 3]

# t = tuple(lst)

# print(t)

"""
(1, 2, 3)
"""


# 79. WAP to access nested tuple element

# SYNTAX:
# tuple[index][index]

# nested access

# ((1,2),(3,4))

# t = ((1, 2), (3, 4))

# print(t[1][0])

"""
3
"""


# 80. WAP to unpack nested tuple

# SYNTAX:
# (a,b),(c,d)=tuple

# nested unpacking

# ((1,2),(3,4))

# t = ((1, 2), (3, 4))

# (a, b), (c, d) = t

# print(a)
# print(b)
# print(c)
# print(d)

"""
1
2
3
4
"""


# 81. WAP to swap two variables using tuple unpacking

# SYNTAX:
# a,b=b,a

# swapping values

# 10 ↔ 20

# a = 10
# b = 20

# a, b = b, a

# print(a)
# print(b)

"""
20
10
"""


# 82. WAP to check whether element exists in tuple

# SYNTAX:
# value in tuple

# check presence

# (10,20,30)

# t = (10, 20, 30)

# print(20 in t)

"""
True
"""


# 83. WAP to count vowels in tuple of characters

# SYNTAX:
# char in "aeiou"

# vowels count

# ('a','b','e','x')

# t = ('a', 'b', 'e', 'x')

# count = 0

# for i in t:

#     if i in "aeiouAEIOU":
#         count += 1

# print(count)

"""
2
"""


# 84. WAP to find maximum value in tuple

# SYNTAX:
# max(tuple)

# largest value

# (10,50,20)

# t = (10, 50, 20)

# print(max(t))

"""
50
"""


# 85. WAP to find minimum value in tuple

# SYNTAX:
# min(tuple)

# smallest value

# (10,50,20)

# t = (10, 50, 20)

# print(min(t))

"""
10
"""

# =========================
# SET METHODS
# =========================

# 86. WAP to add single element into set using add()

# SYNTAX:
# set.add(value)

# add one value

# {1,2,3} + 4

# s = {1, 2, 3}

# s.add(4)

# print(s)

"""
{1, 2, 3, 4}
"""


# 87. WAP to add multiple elements using update()

# SYNTAX:
# set.update(values)

# multiple values added

# {1,2} + 3,4,5

# s = {1, 2}

# s.update([3, 4, 5])

# print(s)

"""
{1, 2, 3, 4, 5}
"""


# 88. WAP to remove element using remove()

# SYNTAX:
# set.remove(value)

# removes exact value

# {1,2,3}

# s = {1, 2, 3}

# s.remove(2)

# print(s)

"""
{1, 3}
"""


# 89. WAP to remove random element using pop()

# SYNTAX:
# set.pop()

# random deletion

# {10,20,30}

# s = {10, 20, 30}

# print(s.pop())

# print(s)

"""
10
{20, 30}
"""


# 90. WAP to clear complete set using clear()

# SYNTAX:
# set.clear()

# removes all elements

# {1,2,3} --> {}

# s = {1, 2, 3}

# s.clear()

# print(s)

"""
set()
"""


# 91. WAP to create set from list

# SYNTAX:
# set(list)

# list --> set

# [1,2,2,3]

# lst = [1, 2, 2, 3]

# s = set(lst)

# print(s)

"""
{1, 2, 3}
"""


# 92. WAP to remove duplicate values using set

# SYNTAX:
# list(set(list))

# duplicates removed

# [1,1,2,2,3]

# lst = [1, 1, 2, 2, 3]

# print(list(set(lst)))

"""
[1, 2, 3]
"""


# 93. WAP to add tuple into set

# SYNTAX:
# set.add(tuple)

# tuple allowed inside set

# (1,2)

# s = {10, 20}

# s.add((1, 2))

# print(s)

"""
{10, 20, (1, 2)}
"""


# 94. WAP to check whether element exists in set

# SYNTAX:
# value in set

# membership checking

# {1,2,3}

# s = {1, 2, 3}

# print(2 in s)

"""
True
"""


# 95. WAP to union two sets

# SYNTAX:
# set1.union(set2)

# all unique values

# {1,2} U {2,3}

# s1 = {1, 2}
# s2 = {2, 3}

# print(s1.union(s2))

"""
{1, 2, 3}
"""


# 96. WAP to find common elements between sets

# SYNTAX:
# set1.intersection(set2)

# common values

# {1,2,3} ∩ {2,3,4}

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# print(s1.intersection(s2))

"""
{2, 3}
"""


# 97. WAP to find difference between sets

# SYNTAX:
# set1.difference(set2)

# values only in first set

# {1,2,3} - {2,3}

# s1 = {1, 2, 3}
# s2 = {2, 3}

# print(s1.difference(s2))

"""
{1}
"""


# 98. WAP to remove all elements one by one using pop()

# SYNTAX:
# while len(set)>0:
#     set.pop()

# popping repeatedly

# {1,2,3}

# s = {1, 2, 3}

# while len(s) > 0:

#     print(s.pop())

"""
1
2
3
"""


# 99. WAP to check whether set allows duplicate values

# SYNTAX:
# duplicates automatically removed

# {1,1,2,2}

# s = {1, 1, 2, 2, 3}

# print(s)

"""
{1, 2, 3}
"""


# 100. WAP to create empty set correctly

# SYNTAX:
# set()

# {} --> dictionary
# set() --> empty set

# s = set()

# print(type(s))

"""
<class 'set'>
"""


# =========================
# DICTIONARY METHODS
# =========================

# 101. WAP to create dictionary using key-value pairs

# SYNTAX:
# {key:value}

# dictionary creation

# name --> python
# version --> 3

# d = {"name": "python", "version": 3}

# print(d)

"""
{'name': 'python', 'version': 3}
"""


# 102. WAP to access all keys using keys()

# SYNTAX:
# dictionary.keys()

# returns all keys

# d = {"a": 1, "b": 2, "c": 3}

# print(d.keys())

"""
dict_keys(['a', 'b', 'c'])
"""


# 103. WAP to access all values using values()

# SYNTAX:
# dictionary.values()

# returns all values

# d = {"a": 1, "b": 2, "c": 3}

# print(d.values())

"""
dict_values([1, 2, 3])
"""


# 104. WAP to access all items using items()

# SYNTAX:
# dictionary.items()

# returns key-value pairs

# d = {"a": 1, "b": 2}

# print(d.items())

"""
dict_items([('a', 1), ('b', 2)])
"""


# 105. WAP to get value using get()

# SYNTAX:
# dictionary.get(key)

# gets value using key

# d = {"name": "python"}

# print(d.get("name"))

"""
python
"""


# 106. WAP to update dictionary using update()

# SYNTAX:
# dictionary.update(other_dictionary)

# updates dictionary

# d = {"a":1}
# add b:2

# d = {"a": 1}

# d.update({"b": 2})

# print(d)

"""
{'a': 1, 'b': 2}
"""


# 107. WAP to add default value using setdefault()

# SYNTAX:
# dictionary.setdefault(key,value)

# adds if key not present

# d = {"a":1}

# d = {"a": 1}

# d.setdefault("b", 2)

# print(d)

"""
{'a': 1, 'b': 2}
"""


# 108. WAP to create dictionary using fromkeys()

# SYNTAX:
# dict.fromkeys(keys,value)

# same value for all keys

# a,b,c --> 0

# keys = ["a", "b", "c"]

# d = dict.fromkeys(keys, 0)

# print(d)

"""
{'a': 0, 'b': 0, 'c': 0}
"""


# 109. WAP to remove value using pop()

# SYNTAX:
# dictionary.pop(key)

# removes given key

# d = {"a":1,"b":2}

# d = {"a": 1, "b": 2}

# d.pop("a")

# print(d)

"""
{'b': 2}
"""


# 110. WAP to remove last inserted item using popitem()

# SYNTAX:
# dictionary.popitem()

# removes last pair

# d = {"a":1,"b":2}

# d = {"a": 1, "b": 2}

# d.popitem()

# print(d)

"""
{'a': 1}
"""


# 111. WAP to clear dictionary using clear()

# SYNTAX:
# dictionary.clear()

# removes all items

# d = {"a":1,"b":2}

# d = {"a": 1, "b": 2}

# d.clear()

# print(d)

"""
{}
"""


# 112. WAP to add new key-value pair using d[key]=value

# SYNTAX:
# dictionary[key]=value

# adding pair

# d["c"]=3

# d = {"a": 1}

# d["b"] = 2

# print(d)

"""
{'a': 1, 'b': 2}
"""


# 113. WAP to merge two dictionaries

# SYNTAX:
# d1.update(d2)

# combines dictionaries

# d1={"a":1}
# d2={"b":2}

# d1 = {"a": 1}
# d2 = {"b": 2}

# d1.update(d2)

# print(d1)

"""
{'a': 1, 'b': 2}
"""


# 114. WAP to count frequency of characters using dictionary

# SYNTAX:
# dictionary[char]=count

# aabcc

# a=2
# b=1
# c=2

# s = "aabcc"

# d = {}

# for i in s:

#     d[i] = s.count(i)

# print(d)

"""
{'a': 2, 'b': 1, 'c': 2}
"""


# 115. WAP to create dictionary from two lists

# SYNTAX:
# dict(zip(list1,list2))

# keys + values

# names + marks

# keys = ["a", "b", "c"]
# values = [10, 20, 30]

# d = dict(zip(keys, values))

# print(d)

"""
{'a': 10, 'b': 20, 'c': 30}
"""


# 116. WAP to update marks of student

# SYNTAX:
# dictionary[key]=new_value

# update existing value

# marks["python"]=95

# marks = {"python": 80, "java": 70}

# marks["python"] = 95

# print(marks)

"""
{'python': 95, 'java': 70}
"""


# 117. WAP to store square values in dictionary

# SYNTAX:
# dictionary[number]=number**2

# 1:1
# 2:4
# 3:9

# d = {}

# for i in range(1, 6):

#     d[i] = i ** 2

# print(d)

"""
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


# 118. WAP to store cube values in dictionary

# SYNTAX:
# dictionary[number]=number**3

# 1:1
# 2:8
# 3:27

# d = {}

# for i in range(1, 6):

#     d[i] = i ** 3

# print(d)

"""
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""


# 119. WAP to check whether key exists in dictionary

# SYNTAX:
# key in dictionary

# membership checking

# d = {"a":1,"b":2}

# d = {"a": 1, "b": 2}

# print("a" in d)

"""
True
"""


# 120. WAP to remove all items one by one

# SYNTAX:
# while len(dictionary)>0:
#     dictionary.popitem()

# removes repeatedly

# d = {"a":1,"b":2,"c":3}

# d = {"a": 1, "b": 2, "c": 3}

# while len(d) > 0:

#     print(d.popitem())

"""
('c', 3)
('b', 2)
('a', 1)
"""


# 121. WAP to create nested dictionary

# SYNTAX:
# {key:{inner_key:value}}

# dictionary inside dictionary

# student details

# d = {
#     "student1": {"name": "python", "marks": 90},
#     "student2": {"name": "java", "marks": 80}
# }

# print(d)

"""
{'student1': {'name': 'python', 'marks': 90}, 'student2': {'name': 'java', 'marks': 80}}
"""


# 122. WAP to access nested dictionary value

# SYNTAX:
# dictionary[key][inner_key]

# nested access

# d["student1"]["marks"]

# d = {
#     "student1": {"name": "python", "marks": 90}
# }

# print(d["student1"]["marks"])

"""
90
"""


# 123. WAP to convert keys into list

# SYNTAX:
# list(dictionary.keys())

# keys --> list

# d={"a":1,"b":2}

# d = {"a": 1, "b": 2}

# print(list(d.keys()))

"""
['a', 'b']
"""


# 124. WAP to convert values into tuple

# SYNTAX:
# tuple(dictionary.values())

# values --> tuple

# d={"a":1,"b":2}

# d = {"a": 1, "b": 2}

# print(tuple(d.values()))

"""
(1, 2)
"""


# 125. WAP to sort dictionary keys

# SYNTAX:
# sorted(dictionary.keys())

# alphabetical sorting

# c,a,b

# d = {"c": 3, "a": 1, "b": 2}

# print(sorted(d.keys()))

"""
['a', 'b', 'c']
"""


# =========================
# CONCATENATION
# =========================

# 126. WAP to concatenate two strings
# 127. WAP to concatenate two lists
# 128. WAP to concatenate two tuples
# 129. WAP to concatenate string with number using type casting
# 130. WAP to concatenate list with tuple
# 131. WAP to concatenate tuple with list
# 132. WAP to concatenate set with set
# 133. WAP to concatenate dictionary with dictionary
# 134. WAP to concatenate nested lists
# 135. WAP to concatenate list of strings into single string
# 136. WAP to concatenate multiple tuples
# 137. WAP to concatenate username and domain
# 138. WAP to concatenate first name and last name
# 139. WAP to concatenate two dictionaries using update()
# 140. WAP to concatenate immutable and mutable datatypes


# =========================
# REPLICATION
# =========================

# 141. WAP to replicate string using *
# 142. WAP to replicate list using *
# 143. WAP to replicate tuple using *
# 144. WAP to replicate nested list
# 145. WAP to create repeated pattern using string replication
# 146. WAP to print triangle pattern using replication
# 147. WAP to create repeated zeros list
# 148. WAP to create repeated boolean list
# 149. WAP to replicate tuple of numbers
# 150. WAP to replicate list containing strings
# 151. WAP to check whether set supports replication
# 152. WAP to check whether dictionary supports replication
# 153. WAP to replicate empty string
# 154. WAP to replicate list containing mutable elements
# 155. WAP to create matrix using replication


# =========================
# COPY METHODS
# =========================

# 156. WAP to perform normal assignment copy
# 157. WAP to check changes reflected in normal copy
# 158. WAP to perform shallow copy using copy()
# 159. WAP to check shallow copy with nested list
# 160. WAP to perform deep copy using deepcopy()
# 161. WAP to check deep copy with nested list
# 162. WAP to compare memory addresses using id()
# 163. WAP to copy list using slicing
# 164. WAP to copy tuple
# 165. WAP to copy set using copy()
# 166. WAP to copy dictionary using copy()
# 167. WAP to modify copied dictionary
# 168. WAP to copy nested dictionary
# 169. WAP to compare shallow copy and deep copy
# 170. WAP to check mutable object behavior in copies
# 171. WAP to check immutable object behavior in copies
# 172. WAP to create independent nested list using deep copy
# 173. WAP to check copied list after append()
# 174. WAP to check copied list after remove()
# 175. WAP to copy list manually using loop
