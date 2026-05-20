#  ┌──► while condition:
#  │        |----------------------|
#  │        |  True Statements     |
#  │        |----------------------|
#  │        |  Update Expression   |
#  └────────|  (e.g., i += 1)      |
#           |----------------------|

# 1. WAP to print 1 to 5 numbers using while loop.
# n = 1
# while n < 6:
#     print(n)
#     n += 1

"""
1
2
3
4
5
"""

# 2. WAP to print 1 to 10 numbers using while loop.
# n = 1
# while n <= 10:
#     print(n)
#     n += 1

"""
1
2
3
4
5
6
7
8
9
10
"""

# TODO: 3. WAP to print hello python 5 times using while loop.
# n = 1
# while n < 6:
#     print("hello python")
#     n += 1

"""
hello python
hello python
hello python
hello python
hello python
"""

# TODO: 4. WAP to print numbers from 10 to 1 using while loop.
# i = 10
# while i > 0:
#     print(i)
#     i -= 1

"""
10
9
8
7
6
5
4
3
2
1
"""

# TODO: 5. WAP to print even numbers from 1 to 10 using while loop.
# i = 1
# while i < 11:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

"""
2 4 6 8 10 
"""

# TODO: 6. WAP to print odd numbers from 1 to n using while loop.
# n = int(input("enter a number: "))
# i = 1
# while i < n + 1:
#     if i % 2 != 0:
#         print(i, end=" ")
#     i += 1

"""
enter a number: 20
1 3 5 7 9 11 13 15 17 19
"""

# TODO: 7. WAP to print nth table using while loop.
# n = int(input("enter a number: "))
# i = 1
# while i < n + 1:
#     print(f"{n} * {i} = {i * n}")
#     i += 1

"""
enter a number: 15
15 * 1 = 15
15 * 2 = 30
15 * 3 = 45
15 * 4 = 60
15 * 5 = 75
15 * 6 = 90
15 * 7 = 105
15 * 8 = 120
15 * 9 = 135
15 * 10 = 150
15 * 11 = 165
15 * 12 = 180
15 * 13 = 195
15 * 14 = 210
15 * 15 = 225
"""

# TODO: 8. WAP to reverse the given number without using type casting using while loop.
# n = int(input("enter a number: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
#     print(rev)

# rev*10 --> to tenth place n%10 --> to return the last position value
# n // 10 --> deletes last position value

"""
enter a number: 256
652
"""
# TODO: 9. WAP to check whether given number is palindrome or not using while loop.
# n = int(input("enter a number: "))
# temp = n
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
# if rev == temp:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")

# 1*10  =10       #10+2=12   12*10  =120    120+1=121
# 12         #1          #0
"""
enter a number: 121
it is a palindrome

enter a number: 153
not a palindrome
"""
# TODO: 10. WAP to traverse through a string using while loop.
# st = input("enter a string: ")
# i = 0
# while len(st) > i:
#     print(st[i])
#     i += 1

"""
enter a string: hello
h
e
l
l
o
"""

# TODO: 11. WAP to reverse a string using while loop.
s = input("enter a string: ")
i = 0
rev = ""
while i < len(s):
    rev = s[i] + rev
    i += 1
print(rev)

"""
enter a string: hello
olleh
"""

# TODO: 12. WAP to check whether given string is palindrome or not using while loop.
s = input("enter a string: ")
i = 0
rev = ""
while i < len(s):
    rev = s[i] + rev
    i += 1
if rev == s:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")
# TODO: 13. WAP to convert uppercase letters into lowercase and lowercase letters into uppercase without using string methods using while loop.
# TODO: 14. WAP to print fibonacci series using while loop.
# n = int(input("enter a number: "))
# a = 0
# b = 1
# print(a, b, end=" ")
# i = 1
# while i <= n - 2:
#     c = a + b
#     print(c, end=" ")
#     a = b
#     b = c
#     i += 1

"""
0 1 1 2 3 5 8 13 21 34
"""
# TODO: 15. WAP to print factorial of a given number using while loop.
# n = 5
# i = 1
# fact = 1
# while i < n + 1:
#     fact = fact * n
#     n -= 1
# print(fact)

"""
120
"""

# TODO: 16. WAP to check whether a given number is perfect square or not.

# TODO: 17. WAP to check whether a given number is perfect number or not using while loop.

# TODO: 18. WAP to print sum of digits present in a number using while loop.
# TODO: 19. WAP to check whether a given number is harshad number or not using while loop.
# TODO: 20. WAP to check whether a given number is strong number or not using while loop.

# TODO: 21. WAP to traverse through a list and check whether the word length is even or odd, if even add as it is else reverse the word and add to a new list using while loop.
# TODO: 22. WAP to traverse through a list and check whether the word starts with vowel or consonant, if vowel add as it is else reverse the word and add to a new list using while loop.
# TODO: 23. WAP to traverse through a list and create a new list with tuple of word and index if word length is even else word and length of the word using while loop.
# TODO: 24. WAP to create a list with word and reverse word pair inside a tuple using while loop.
# TODO: 25. WAP to create a dictionary with key as word and value as index of the word using while loop.

# TODO: 26. WAP to create a dictionary with key as word and value as index if word length is even else length of the word using while loop.
# TODO: 27. WAP to create a dictionary with key as number and value as square of the number if even else cube of the number using while loop.
# TODO: 28. WAP to print numbers from n to 1 using while loop.
# TODO: 29. WAP to print sum of first n natural numbers using while loop.
# TODO: 30. WAP to print multiplication table in reverse order using while loop.

# TODO: 31. WAP to count vowels and consonants in a string using while loop.
# TODO: 32. WAP to print numbers from 1 to 50 divisible by 5 using while loop.
# TODO: 33. WAP to print numbers from 50 to 1 using while loop.
# n = 50
# while n > 0:
#     print(n, end=" ")
#     n -= 1

"""
50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""
# TODO: 34. WAP to print square of numbers from 1 to n using while loop.
# n = int(input("enter a number: "))
# i = 1
# while i < n + 1:
#     print(f"square of {i} is {i**2}")
#     i += 1

"""
enter a number: 15
square of 1 is 1
square of 2 is 4
square of 3 is 9
square of 4 is 16
square of 5 is 25
square of 6 is 36
square of 7 is 49
square of 8 is 64
square of 9 is 81
square of 10 is 100
square of 11 is 121
square of 12 is 144
square of 13 is 169
square of 14 is 196
square of 15 is 225
"""
# TODO: 35. WAP to print cube of numbers from 1 to n using while loop.
# n = int(input("enter a number: "))
# i = 1
# while i < n + 1:
#     print(f"cube of {i} is {i**3}")
#     i += 1

"""
enter a number: 9
cube of 1 is 1
cube of 2 is 8
cube of 3 is 27
cube of 4 is 64
cube of 5 is 125
cube of 6 is 216
cube of 7 is 343
cube of 8 is 512
cube of 9 is 729
"""

# TODO: 36. WAP to count number of digits in a given number using while loop.
# TODO: 37. WAP to print sum of even digits in a given number using while loop.
# TODO: 38. WAP to print product of digits in a given number using while loop.
# TODO: 39. WAP to check whether a given number is spy number or not using while loop.
# TODO: 40. WAP to check whether a given number is neon number or not using while loop.

# TODO: 41. WAP to print all factors of a given number using while loop.


"""

"""
# TODO: 42. WAP to check whether a given number is prime or not using while loop.
# TODO: 43. WAP to print prime numbers from 1 to n using while loop.
# TODO: 44. WAP to print multiplication tables from 1 to 5 using nested while loop.
# TODO: 45. WAP to count uppercase and lowercase letters in a string using while loop.

# TODO: 46. WAP to remove spaces from a string using while loop.
# TODO: 47. WAP to print characters present at even index positions in a string using while loop.
# TODO: 48. WAP to create a list with length of each word using while loop.
# TODO: 49. WAP to create a dictionary with word as key and reverse word as value using while loop.
# TODO: 50. WAP to check whether a given number is automorphic number or not using while loop.
