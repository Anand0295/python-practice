# =========================
# FOR LOOP
# =========================

# ┌──► for variable in iterable:
# │        |----------------------|
# │        |  Traverse Elements   |
# │        |----------------------|
# │        |  Executes Repeatedly |
# └────────|  Until iterable ends |
#          |----------------------|


# =========================
# ELEMENT / COLLECTION
# =========================

# ┌──► for element in collection:
# │        |----------------------|
# │        |  Access Each Element |
# │        |----------------------|
# │        |  One By One          |
# └────────|  print(element)      |
#          |----------------------|


# 1. WAP to print all elements in a list
# n = eval(input("enter a list: "))
# for i in n:
#     print(i, end=" ")


"""
enter a list: [1,2,3,4,5]
1 2 3 4 5
"""

# 2. WAP to print all characters in a string
# n = input("enter a string: ")
# for i in n:
#     print(i, end=" ")

"""
enter a string: hello world
h e l l o   w o r l d
"""

# 3. WAP to print all elements in a tuple
# n = eval(input("enter a tuple: "))
# for i in n:
#     print(i, end=" ")

"""
enter a tuple: (1,2,3,4,5,6,7,8)
1 2 3 4 5 6 7 8 
"""

# 4. WAP to print all values in a set
# n = eval(input("enter your set: "))
# for i in n:
#     print(i, end=" ")

"""
enter your set: {1,2,3,4,5}
1 2 3 4 5
"""

# 5. WAP to print all keys in dictionary
# n = eval(input("enter your dictionary: "))
# for i in n:
#     print(i, end=" ")

"""
enter your dictionary: {'a':1,'b':2}
a b
"""

# 6. WAP to print all values in dictionary
# n = eval(input("enter your dictionary: "))
# for i in n.values():
#     print(i, end=" ")

"""
enter your dictionary: {'a':1,'b':2}
1 2
"""

# 7. WAP to print key-value pairs in dictionary
# n = eval(input("enter your dictionary: "))
# for i in n.items():
#     print(i, end=" ")

"""
enter your dictionary: {'a':1,'b':2}
('a', 1) ('b', 2)
"""

# 8. WAP to count vowels in string
# n = input("enter a string: ")
# count = 0
# for i in n:
#     if i in "aeiouAEIOU":
#         count += 1
# print(count)

"""
enter a string: hello
2
"""

# 9. WAP to count consonants in string
# n = input("enter a string: ")
# count = 0
# for i in n:
#     if i not in "aeiouAEIOU":
#         count += 1
# print(count)

"""
enter a string: hello
3
"""

# 10. WAP to count uppercase letters in string
# n = input("enter a string: ")
# count = 0
# for i in n:
#     if i.isupper():
#         count += 1
# print(count)

"""
enter a string: HeLLo
3
"""

# 11. WAP to count lowercase letters in string
# n = input("enter a string: ")
# count = 0
# for i in n:
#     if i.islower():
#         count += 1
# print(count)

"""
enter a string: hello
5
"""

# # 12. WAP to count digits in string
# n = input("enter a string: ")
# count = 0
# for i in n:
#     if i.isdigit():
#         count += 1
# print(count)

"""
enter a string: h1l2l3o4
4
"""

# 13. WAP to print even numbers from list
# lst = eval(input("enter a list: "))
# for i in lst:
#     if i % 2 == 0:
#         print(i, end=" ")

"""
enter a list: [1,2,3,4,5,6]
2 4 6
"""

# 14. WAP to print odd numbers from list
# lst = eval(input("enter a list: "))
# for i in lst:
#     if i % 2 != 0:
#         print(i, end=" ")

"""
enter a list: [1,2,3,4,5,6]
1 3 5
"""
# 15. WAP to find sum of list elements
# lst = eval(input("enter a list: "))
# sum = 0
# for i in lst:
#     sum += i
# print(sum)

"""
enter a list: [1,2,3]
6
"""

# 16. WAP to find product of list elements
# lst = eval(input("enter a list: "))
# prod = 1
# for i in lst:
#     prod *= i
# print(prod)

"""
enter a list: [1,2,3]
6
"""

# 17. WAP to find largest element in list
# lst = eval(input("enter a list: "))
# j = lst[0]
# for i in lst:
#     if i > j:
#         j = i

# print(j)

"""
enter a list: [1,2,3,4,5]
5
"""
# 18. WAP to find smallest element in list
# l10

"""
enter a list: [1,2,3,4,5]
1
"""

# 19. WAP to create list of squares
# n = int(input("enter the range: "))
# lst = []
# for i in range(n + 1):
#     lst.append(i**2)
# print(lst)

"""
enter the range: 10
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

# lst1 = eval(input("enter a list: "))
# lst2 = []
# for i in lst1:
#     lst2.append(i**2)
# print(lst2)

"""
enter a list: [1,2,3,4,5]
[1, 4, 9, 16, 25]
"""
# 20. WAP to create list of cubes
# n = int(input("enter the range: "))
# lst = []
# for i in range(n + 1):
#     lst.append(i**3)
# print(lst)

"""
enter the range: 15
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375]
"""

# lst1 = eval(input("enter a list: "))
# lst2 = []
# for i in lst1:
#     lst2.append(i**3)
# print(lst2)

"""
enter a list: [1, 2, 3, 4, 5]
[1, 8, 27, 64, 125]
"""

# 21. WAP to reverse string using loop
# n = input("enter a string: ")
# m = ""
# for i in n:
#     m = n[::-1]
# print(m)

"""
enter a string: hello
olleh
"""

# 22. WAP to create frequency dictionary of characters
# s = input("enter a string: ")
# dict = {}
# for i in s:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)

"""
enter a string: hello  
{'h': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1}
"""

# 23. WAP to remove spaces from string
# n = input("enter a string: ")
# res = ""
# for i in n:
#     if i != " ":
#         res += i
# print(res)

"""
enter a string: h e l l o
hello
"""

# 24. WAP to print palindrome characters matching
# s = input("enter a string: ")
# r = s[::-1]
# for i in range(len(s)):
#     if s[i] == r[i]:
#         print(s[i], end=" ")

"""
enter a string: madam
m a d a m 
"""

# 25. WAP to count special characters in string
# s = input("enter a string: ")
# count = 0
# for i in s:
#     if not i.isalnum():
#         count += 1
# print(count)


"""
enter a string: hello@#$
3

enter a string: hello
0
"""

# =========================
# RANGE()
# =========================

# ┌──► for i in range(start, stop, step):
# │        |----------------------|
# │        |  Generates Numbers   |
# │        |----------------------|
# │        |  Iteration Control   |
# └────────|  Increment / Decrement|
#          |----------------------|


# 26. WAP to print numbers from 1 to 10
# n = 10
# for i in range(1, n + 1):
#     print(i, end=" ")

"""
1 2 3 4 5 6 7 8 9 10
"""

# 27. WAP to print numbers from 10 to 1
# for i in range(10, 0, -1):
#     print(i, end=" ")

"""
10 9 8 7 6 5 4 3 2 1
"""

# 28. WAP to print even numbers from 1 to 100
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end=" ")

"""
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
"""

# 29. WAP to print odd numbers from 1 to n
# n = int(input("enter a number: "))
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(i, end=" ")

"""
enter a number: 10
1 3 5 7 9 
"""

# 30. WAP to print multiplication table
# n = int(input("enter a number: "))
# for i in range(1, n + 1):
#     print(f"{n} * {i} = {i * n}")

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

# 31. WAP to print multiplication tables from 1 to 10
# for i in range(1, 11):
#     print("Table of", i)
#     print()
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#     print()

"""
Table of 1

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

Table of 2

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

Table of 3

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30

Table of 4

4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40

Table of 5

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

Table of 6

6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60

Table of 7

7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70

Table of 8

8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80

Table of 9

9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90

Table of 10

10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
"""

# 32. WAP to print squares from 1 to n
# n = int(input("enter a number: "))
# for i in range(1, n + 1):
#     print(i**2, end=" ")

"""
enter a number: 5
1 4 9 16 25
"""

# 33. WAP to print cubes from 1 to n
# n = int(input("enter a number: "))
# for i in range(1, n + 1):
#     print(i**3, end=" ")

"""
enter a number: 9
1 8 27 64 125 216 343 512 729 
"""

# 34. WAP to print factorial of number
# n = int(input("enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(f"{n}! = {fact}")

"""
enter a number: 5
5! = 120
"""

# 35. WAP to print Fibonacci series
# n = int(input("enter a number: "))
# a = 0
# b = 1
# print(a, b, end=" ")
# for i in range(1, n + 2):
#     c = a + b
#     print(c, end=" ")
#     a = b
#     b = c

"""
enter a number: 10
0 1 1 2 3 5 8 13 21 34 55 89 144
"""

# 36. WAP to print star pattern
# n = int(input("enter number of rows: "))
# for i in range(n):
#     print("* " * n)

"""
enter number of rows: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""

# 37. WAP to print reverse star pattern
# n = int(input("enter number of rows: "))
# for i in range(n, 0, -1):
#     print("* " * i)

"""
enter number of rows: 5
* * * * *
* * * *
* * *
* *
*
"""

# 38. WAP to print right angle triangle pattern
# n = int(input("enter number of rows: "))
# for i in range(1, n + 1):
#     print("* " * i)

"""
enter number of rows: 5
*
* *
* * *
* * * *
* * * * *
"""

# 39. WAP to print alphabet pattern
# n = int(input("enter number of rows: "))
# ch = 65
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(ch), end=" ")
#         ch += 1

#     print()

"""
enter number of rows: 5
A 
B C 
D E F 
G H I J 
K L M N O 
"""

# 40. WAP to print ASCII values A-Z
# for i in range(65, 91):
#     print(chr(i), "=", i)

"""
A = 65
B = 66
C = 67
D = 68
E = 69
F = 70
G = 71
H = 72
I = 73
J = 74
K = 75
L = 76
M = 77
N = 78
O = 79
P = 80
Q = 81
R = 82
S = 83
T = 84
U = 85
V = 86
W = 87
X = 88
Y = 89
Z = 90
"""

# 41. WAP to print ASCII values a-z
# for i in range(97, 123):
#     print(chr(i), "=", i)

"""
a = 97
b = 98
c = 99
d = 100
e = 101
f = 102
g = 103
h = 104
i = 105
j = 106
k = 107
l = 108
m = 109
n = 110
o = 111
p = 112
q = 113
r = 114
s = 115
t = 116
u = 117
v = 118
w = 119
x = 120
y = 121
z = 122
"""

# 42. WAP to print divisors of number
# n = int(input("enter a number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

"""
enter a number: 10
1 2 5 10
"""

# 43. WAP to check prime number
# n = int(input("enter a number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")

# else:
#     print("not a prime number")

"""
enter a number: 3
prime number

enter a number: 15
not a prime number
"""

# 44. WAP to print prime numbers from 1 to n
# n = int(input("Enter your number: "))

# for i in range(2, n + 1):
#     is_prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(i, end=" ")

"""
Enter your number: 10
2 3 5 7 
"""

# 45. WAP to print Armstrong numbers from 1 to n
# n = int(input("enter range: "))

# for i in range(1, n + 1):
#     temp = i
#     digits = len(str(i))
#     total = 0

#     for j in str(i):
#         total += int(j) ** digits

#     if total == temp:
#         print(i, end=" ")

"""
enter range: 100 
1 2 3 4 5 6 7 8 9
"""

# 46. WAP to print perfect numbers from 1 to n
# n = int(input("enter range: "))

# for i in range(1, n + 1):
#     total = 0

#     for j in range(1, i):
#         if i % j == 0:
#             total += j

#     if total == i:
#         print(i, end=" ")

"""
enter range: 100
6 28
"""

# 47. WAP to print strong numbers from 1 to n
# n = int(input("enter range: "))

# for i in range(1, n + 1):
#     temp = i
#     total = 0

#     for j in str(i):
#         fact = 1

#         for k in range(1, int(j) + 1):
#             fact *= k

#         total += fact

#     if total == temp:
#         print(i, end=" ")

"""
enter range: 100
1 2
"""

# 48. WAP to print palindrome numbers from 1 to n
# n = int(input("enter range: "))

# for i in range(1, n + 1):
#     if str(i) == str(i)[::-1]:
#         print(i, end=" ")

"""
enter range: 500 
1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 222 232 242 252 262 272 282 292 303 313 323 333 343 353 363 373 383 393 404 414 424 434 444 454 464 474 484 494
"""

# 49. WAP to print leap years between ranges
# start = int(input("enter start year: "))
# end = int(input("enter end year: "))

# for i in range(start, end + 1):
#     if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#         print(i, end=" ")

"""
enter start year: 1900
enter end year: 3000
1904 1908 1912 1916 1920 1924 1928 1932 1936 1940 1944 1948 1952 1956 1960 1964 1968 1972 1976 1980 1984 1988 1992 1996 2000 2004 2008 2012 2016 2020 2024 2028 2032 2036 2040 2044 2048 2052 2056 2060 2064 2068 2072 2076 2080 2084 2088 2092 2096 2104 2108 2112 2116 2120 2124 2128 2132 2136 2140 2144 2148 2152 2156 2160 2164 2168 2172 2176 2180 2184 2188 2192 2196 2204 2208 2212 2216 2220 2224 2228 2232 2236 2240 2244 2248 2252 2256 2260 2264 2268 2272 2276 2280 2284 2288 2292 2296 2304 2308 2312 2316 2320 2324 2328 2332 2336 2340 2344 2348 2352 2356 2360 2364 2368 2372 2376 2380 2384 2388 2392 2396 2400 2404 2408 2412 2416 2420 2424 2428 2432 2436 2440 2444 2448 2452 2456 2460 2464 2468 2472 2476 2480 2484 2488 2492 2496 2504 2508 2512 2516 2520 2524 2528 2532 2536 2540 2544 2548 2552 2556 2560 2564 2568 2572 2576 2580 2584 2588 2592 2596 2604 2608 2612 2616 2620 2624 2628 2632 2636 2640 2644 2648 2652 2656 2660 2664 2668 2672 2676 2680 2684 2688 2692 2696 2704 2708 2712 2716 2720 2724 2728 2732 2736 2740 2744 2748 2752 2756 2760 2764 2768 2772 2776 2780 2784 2788 2792 2796 2800 2804 2808 2812 2816 2820 2824 2828 2832 2836 2840 2844 2848 2852 2856 2860 2864 2868 2872 2876 2880 2884 2888 2892 2896 2904 2908 2912 2916 2920 2924 2928 2932 2936 2940 2944 2948 2952 2956 2960 2964 2968 2972 2976 2980 2984 2988 2992 2996 
"""

# 50. WAP to print tables in reverse order
# n = int(input("enter number: "))

# for i in range(10, 0, -1):
#     print(f"{n} x {i} = {n * i}")

"""
enter number: 15
15 x 10 = 150
15 x 9 = 135
15 x 8 = 120
15 x 7 = 105
15 x 6 = 90
15 x 5 = 75
15 x 4 = 60
15 x 3 = 45
15 x 2 = 30
15 x 1 = 15
"""

# =========================
# ENUMERATE()
# =========================

# ┌──► for index, value in enumerate(iterable):
# │        |----------------------|
# │        |  Index + Element     |
# │        |----------------------|
# │        |  Tuple Unpacking     |
# └────────|  (index, value)      |
#          |----------------------|


# 51. WAP to print index and element from list
# lst = eval(input("enter a list: "))
# for i, j in enumerate(lst):
#     print(i, j)

"""
enter a list: [1,2,3,4,5]
0 1
1 2
2 3
3 4
4 5
"""

# lst = eval(input("enter a list: "))
# for i in enumerate(lst):
#     print(i)

"""
enter a list: [1,2,3,4,5]
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
"""

# 52. WAP to print index and character from string
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     print(i, j)

"""
enter a string: hello
0 h
1 e
2 l
3 l
4 o
"""

# 53. WAP to print even index characters
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     if i % 2 == 0:
#         print(j)

"""
enter a string: hello python
h
l
o
p
t
o
"""

# 54. WAP to print odd index characters
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     if i % 2 != 0:
#         print(j, end=" ")
"""
enter a string: NeerajKumar
e r j u a
"""

# 55. WAP to find index of vowels
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     if j in "aeiouAEIOU":
#         print(i, end=" ")

"""
enter a string: hello world
1 4 7
"""

# 56. WAP to create dictionary with index and value
# lst = eval(input(("enter a list: ")))
# d = {}
# for i, j in enumerate(lst):
#     d[i] = j
# print(d)

"""
enter a list: [1,2,'hello',[1,2,3],(100,99,98),{11,22,33}]
{0: 1, 1: 2, 2: 'hello', 3: [1, 2, 3], 4: (100, 99, 98), 5: {33, 11, 22}}
"""

# 57. WAP to print elements greater than index
# lst = eval(input("enter a list: "))
# for i, j in enumerate(lst):
#     if j > i:
#         print(j, end=" ")

"""
enter a list: [0,2,1,5,3,8]
2 5 8
"""

# 58. WAP to replace even index values with square
# lst = eval(input("enter a list: "))
# for i, j in enumerate(lst):
#     if i % 2 == 0:
#         lst[i] = j ** 2
# print(lst)

"""
enter a list: [1,2,3,4,5]
[1, 2, 9, 4, 25]
"""

# 59. WAP to print index positions of spaces
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     if j == " ":
#         print(i, end=" ")

"""
enter a string: hello world python
5 11
"""

# 60. WAP to count indexes containing vowels
# s = input("enter a string: ")
# count = 0
# for i, j in enumerate(s):
#     if j.lower() in "aeiou":
#         count += 1
# print(count)

"""
enter a string: education
5
"""

# 61. WAP to print indexes divisible by 3
# lst = eval(input("enter a list: "))
# for i, j in enumerate(lst):
#     if i % 3 == 0:
#         print(i, end=" ")

"""
enter a list: [10,20,30,40,50,60,70]
0 3 6
"""

# 62. WAP to reverse indexes and values
# lst = eval(input("enter a list: "))
# for i, j in reversed(list(enumerate(lst))):
#     print(i, j)

"""
enter a list: [10,20,30,40]
3 40
2 30
1 20
0 10
"""

# 63. WAP to create tuple of index and word
# lst = input("enter words: ").split()
# res = []
# for i, j in enumerate(lst):
#     res.append((i, j))
# print(tuple(res))

"""
enter words: python java sql html
((0, 'python'), (1, 'java'), (2, 'sql'), (3, 'html'))
"""

# 64. WAP to print elements whose index is prime
# lst = eval(input("enter a list: "))
# for i, j in enumerate(lst):

#     if i > 1:
#         for k in range(2, i):
#             if i % k == 0:
#                 break
#         else:
#             print(j, end=" ")

"""
enter a list: [10,20,30,40,50,60,70]
30 40 60 70
"""

# 65. WAP to print characters with ASCII values
# s = input("enter a string: ")
# for i, j in enumerate(s):
#     print(j, ord(j))

"""
enter a string: ABC
A 65
B 66
C 67
"""


# =========================
# ZIP()
# =========================

# ┌──► for a, b in zip(iter1, iter2):
# │        |----------------------|
# │        |  Pair Elements       |
# │        |----------------------|
# │        |  Parallel Traversal  |
# └────────|  Tuple Pairing       |
#          |----------------------|


# 66. WAP to add elements of two lists
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9, 10]
# res = []
# for a, b in zip(lst1, lst2):
#     res.append(a + b)
# print(res)

"""
[7, 9, 11, 13, 15]
"""

# 67. WAP to multiply elements of two lists
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9, 10]
# res = []
# for a, b in zip(lst1, lst2):
#     res.append(a * b)
# print(res)

"""
[6, 14, 24, 36, 50]
"""

# 68. WAP to combine names and marks
# names = ["anand", "neeraj", "john", "abdul", "ramya"]
# marks = [85, 80, 76, 35, 59, 15]
# d = {}
# for a, b in zip(names, marks):
#     d[a] = b
# print(d)

"""
{'anand': 85, 'neeraj': 80, 'john': 76, 'abdul': 35, 'ramya': 59}
"""

# 69. WAP to create dictionary from two lists
# lst1 = [1, 2, 3, 4, 5]
# lst2 = ["apple", "banana", "orange", "pineapple"]
# d = {}
# for a, b in zip(lst1, lst2):
#     d[a] = b
# print(d)

"""
{1: 'apple', 2: 'banana', 3: 'orange', 4: 'pineapple'}
"""

# 70. WAP to print bigger value among pairs
# lst1 = [10, 20, 30, 40]
# lst2 = [20, 30, 40, 50, 60]
# for a, b in zip(lst1, lst2):
#     if a > b:
#         print(a, end=" ")
#     else:
#         print(b, end=" ")

"""
20 30 40 50
"""

# 71. WAP to print smaller value among pairs
# lst1 = [10, 20, 30, 40]
# lst2 = [20, 30, 40, 50, 60]
# for a, b in zip(lst1, lst2):
#     if a < b:
#         print(a, end=" ")
#     else:
#         print(b, end=" ")

"""
10 20 30 40 
"""

# 72. WAP to concatenate strings from two lists
# lst1 = ["py", "ja", "c"]
# lst2 = ["thon", "va"]
# res = []
# for i, j in zip(lst1, lst2):
#     res.append(i + j)
# print(res)

"""
['python', 'java']
"""

# lst1 = [1, 2, 3, 4]
# lst2 = [1, 5, 3, 8]
# for a, b in zip(lst1, lst2):
#     if a == b:
#         print(a, "same")
#     else:
#         print(a, b, "different")

"""
1 same
2 5 different
3 same
4 8 different
"""

# 74. WAP to count matching elements
# lst1 = [1, 2, 3, 4]
# lst2 = [1, 5, 3, 8]
# count = 0
# for a, b in zip(lst1, lst2):
#     if a == b:
#         count += 1
# print(count)

"""
2
"""
# 75. WAP to merge tuple elements
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# res = ()
# for a, b in zip(t1, t2):
#     res += (a, b)
# print(res)

"""
(1, 4, 2, 5, 3, 6)
"""


# 76. WAP to print student name with grade
# names = ["ram", "sam", "tom"]
# grades = ["A", "B", "A+"]
# for a, b in zip(names, grades):
#     print(a, ":", b)

"""
ram : A
sam : B
tom : A+
"""


# 77. WAP to create list of tuples
# lst1 = [1, 2, 3]
# lst2 = ["a", "b", "c"]
# res = []
# for a, b in zip(lst1, lst2):
#     res.append((a, b))
# print(res)

"""
[(1, 'a'), (2, 'b'), (3, 'c')]
"""


# 78. WAP to unzip list of tuples
# lst = [(1, 'a'), (2, 'b'), (3, 'c')]
# lst1 = []
# lst2 = []
# for a, b in lst:
#     lst1.append(a)
#     lst2.append(b)
# print(lst1)
# print(lst2)

"""
[1, 2, 3]
['a', 'b', 'c']
"""


# 79. WAP to print sum of pair values
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# for a, b in zip(lst1, lst2):
#     print(a + b, end=" ")

"""
5 7 9
"""


# 80. WAP to print product of pair values
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# for a, b in zip(lst1, lst2):
#     print(a * b, end=" ")

"""
4 10 18
"""


# 81. WAP to combine keys and values into dictionary
# keys = ["a", "b", "c"]
# values = [100, 200, 300]
# d = {}
# for a, b in zip(keys, values):
#     d[a] = b
# print(d)

"""
{'a': 100, 'b': 200, 'c': 300}
"""


# 82. WAP to compare characters of two strings
# s1 = "python"
# s2 = "pythxx"
# for a, b in zip(s1, s2):
#     if a == b:
#         print(a, "same")
#     else:
#         print(a, b, "different")

"""
p same
y same
t same
h same
o x different
n x different
"""


# 83. WAP to create matrix addition using zip
# m1 = [[1,2],[3,4]]
# m2 = [[5,6],[7,8]]

# for a, b in zip(m1, m2):

#     row = []

#     for x, y in zip(a, b):
#         row.append(x + y)

#     print(row)

"""
[6, 8]
[10, 12]
"""


# 84. WAP to transpose matrix using zip
# matrix = [[1,2,3],
#           [4,5,6]]

# for i in zip(*matrix):
#     print(list(i))

"""
[1, 4]
[2, 5]
[3, 6]
"""


# 85. WAP to pair vowels and consonants
# vowels = ['a', 'e', 'i']
# consonants = ['b', 'c', 'd']

# for a, b in zip(vowels, consonants):
#     print((a, b))

"""
('a', 'b')
('e', 'c')
('i', 'd')
"""


# =========================
# ZIP_LONGEST()
# =========================

# ┌──► for a, b in zip_longest():
# │        |----------------------|
# │        |  Unequal Pairing     |
# │        |----------------------|
# │        |  Missing → fillvalue |
# └────────|  Continues Till End  |
#          |----------------------|


# # 86. WAP to combine unequal lists
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3, 4]
# res = {}
# for i, j in zip_longest(lst1, lst2):
#     res[i] = j
# print(res)

"""
{1: 1, 2: 2, 3: 3, None: 4}
"""

# 87. WAP to merge strings of unequal length
# s1 = "hello"
# s2 = "qspiders"
# res = {}
# for i, j in zip_longest(s1, s2):
#     res[i] = j
# print(res)

"""
{'h': 'q', 'e': 's', 'l': 'i', 'o': 'd', None: 's'}
"""

# 88. WAP to create dictionary from unequal lists
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3, 4]
# res = {}
# for i, j in zip_longest(lst1, lst2):
#     res[i] = j
# print(res)

"""
{1: 1, 2: 2, 3: 3, None: 4}
"""
# 89. WAP to replace missing values with 0
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9]
# d = {}
# for i, j in zip_longest(lst1, lst2, fillvalue=0):
#     d[i] = j
# print(d)

"""
{1: 6, 2: 7, 3: 8, 4: 9, 5: 0}
"""

# 90. WAP to replace missing values with '*'
# from itertools import zip_longest

# list1 = [1, 2, 3]
# list2 = ["a", "b"]

# result = list(zip_longest(list1, list2, fillvalue="*"))

# print(result)

"""
[(1, 'a'), (2, 'b'), (3, '*')]
"""

# 91. WAP to print longest paired sequence
# lst1 = [1, 2, 3]
# lst2 = ["a", "b", "c"]
# for i in zip_longest(lst1, lst2, fillvalue="*"):
#     print(i)

"""
(1, 'a')
(2, 'b')
(3, 'c')
"""

# 92. WAP to compare unequal tuples
# t1 = (1, 2, 3)
# t2 = (4, 5)
# for i, j in itertools.zip_longest(t1, t2):
#     if i == j:
#         print("Even")
#     else:
#         print("Uneven")

"""
Uneven
Uneven
Uneven
"""

# 93. WAP to align names and marks
# from itertools import zip_longest  # noqa: E402

# names = ["Ram", "Sam", "John"]
# marks = [85, 92]
# for name, mark in zip_longest(names, marks, fillvalue="*"):
#     print(name, mark)

"""
Output:
Ram 85
Sam 92
John *
"""

# 94. WAP to merge uneven matrices
# from itertools import zip_longest  # noqa: E402

# m1 = [[1, 2], [3, 4]]
# m2 = [[5, 6]]

# for row1, row2 in zip_longest(m1, m2, fillvalue=["*"]):
#     print(row1, row2)

"""
Output:
[1, 2] [5, 6]
[3, 4] ['*']
"""
# 95. WAP to print missing positions
# a = [10, 20, 30, 40]
# b = [10, 20]

# for index, (i, j) in enumerate(zip_longest(a, b, fillvalue="*")):
#     if i == "*" or j == "*":
#         print("Missing position:", index)

"""
Output:
Missing position: 2
Missing position: 3
"""


# =========================
# SORTED()
# =========================

# ┌──► sorted(iterable)
# │        |----------------------|
# │        |  Returns Sorted Copy |
# │        |----------------------|
# │        |  Original Unchanged  |
# └────────|  Asc / Desc Order    |
#          |----------------------|


# 96. WAP to sort list in ascending order
lst = [9, 8, 7, 6, 4, 3, 2, 1]
for i in sorted(lst):
    print(i, end=" ")

"""
1 2 3 4 6 7 8 9
"""

# 97. WAP to sort list in descending order
lst = [9, 8, 7, 6, 4, 3, 2, 1]


# 98. WAP to sort tuple
# 99. WAP to sort set
# 100. WAP to sort dictionary keys
# 101. WAP to sort dictionary values
# 102. WAP to sort string alphabetically
# 103. WAP to sort words by length
# 104. WAP to sort nested list by second value
# 105. WAP to sort names alphabetically
# 106. WAP to sort marks descending
# 107. WAP to sort vowels in string
# 108. WAP to sort characters ignoring case
# 109. WAP to sort list without modifying original
# 110. WAP to sort tuples by last element


# =========================
# REVERSED()
# =========================

# ┌──► reversed(iterable)
# │        |----------------------|
# │        |  Reverse Traversal   |
# │        |----------------------|
# │        |  Returns Iterator    |
# └────────|  Reverse Sequence    |
#          |----------------------|


# 111. WAP to reverse string using reversed()
# 112. WAP to reverse list using reversed()
# 113. WAP to reverse tuple
# 114. WAP to print reverse numbers from list
# 115. WAP to reverse words in sentence
# 116. WAP to reverse nested list
# 117. WAP to reverse dictionary keys
# 118. WAP to reverse sorted list
# 119. WAP to reverse even numbers only
# 120. WAP to reverse vowels in string


# =========================
# NESTED FOR LOOP
# =========================

# ┌──► for outer:
# │      for inner:
# │        |----------------------|
# │        |  Nested Iteration    |
# │        |----------------------|
# │        |  Rows × Columns      |
# └────────|  Pattern Traversal   |
#          |----------------------|


# 121. WAP to print square star pattern
# 122. WAP to print number triangle
# 123. WAP to print Floyd triangle
# 124. WAP to print multiplication matrix
# 125. WAP to print identity matrix
# 126. WAP to print chessboard pattern
# 127. WAP to create nested list matrix
# 128. WAP to print transpose matrix
# 129. WAP to compare all pairs in list
# 130. WAP to print combinations of characters
# 131. WAP to print duplicate pairs
# 132. WAP to print common elements between lists
# 133. WAP to print Cartesian product
# 134. WAP to print all substrings
# 135. WAP to print all sublists


# =========================
# ADVANCED FOR LOOP
# =========================

# ┌──► combined loop logic
# │        |----------------------|
# │        |  Multiple Concepts   |
# │        |----------------------|
# │        |  Filtering + Logic   |
# └────────|  Complex Traversal   |
#          |----------------------|


# 136. WAP to print words whose length is prime
# 137. WAP to print palindrome words from list
# 138. WAP to create dictionary of word lengths
# 139. WAP to group even and odd numbers
# 140. WAP to count frequency of list elements
# 141. WAP to find second largest number
# 142. WAP to remove duplicates manually
# 143. WAP to find missing number in sequence
# 144. WAP to rotate list left
# 145. WAP to rotate list right
# 146. WAP to check anagram strings
# 147. WAP to merge alternate characters
# 148. WAP to print diagonal matrix elements
# 149. WAP to flatten nested list
# 150. WAP to print longest word in sentence
# 151. WAP to print shortest word in sentence
# 152. WAP to count repeated words
# 153. WAP to create inverted dictionary
# 154. WAP to separate vowels and consonants
# 155. WAP to print cumulative sum list
# 156. WAP to print cumulative product list
# 157. WAP to print indexes of duplicate elements
# 158. WAP to create multiplication table list
# 159. WAP to generate prime list using loops
# 160. WAP to generate Fibonacci list
# 161. WAP to create star pyramid
# 162. WAP to create reverse pyramid
# 163. WAP to check symmetric matrix
# 164. WAP to count words in sentence
# 165. WAP to reverse alternate words
# 166. WAP to capitalize alternate characters
# 167. WAP to sort words by vowels count
# 168. WAP to print matrix boundary elements
# 169. WAP to create identity matrix
# 170. WAP to print hollow square pattern
# 171. WAP to print Pascal triangle
# 172. WAP to print diamond star pattern
# 173. WAP to merge dictionaries using loops
# 174. WAP to compare two matrices
# 175. WAP to perform matrix multiplication
