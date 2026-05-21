# =========================
# DIGIT BASED PROGRAMS
# =========================

# DIAGRAM:
# A number is broken into individual digits and each digit is processed separately.
#
# Example:  53821
#
# 53821 → 5 → 3 → 8 → 2 → 1
#          ↓   ↓   ↓   ↓   ↓
#        process each digit individually
#
# SYNTAX DIAGRAM:
#  while number > 0:
#      |--------------------------|
#      | Extract Last Digit       |
#      | (digit = number % 10)    |
#      |--------------------------|
#      | Process Digit            |
#      | (sum/count/min/max logic)|
#      |--------------------------|
#      | Truncate Last Digit      |
#      | (number //= 10)          |
#      |--------------------------|

# 1. WAP to reverse a number
# n = int(input("enter a number: "))
# i = 0
# res = 0
# while i < n + 1:
#     res = res * 10 + n % 10
#     n = n // 10
#     i += 1
# print(res)

"""
enter a number: 256
652
"""

# 2. WAP to count digits in a number
# n = int(input("enter a number: "))
# count = 0
# while n>0:
#     count += 1
#     n = n // 10
# print(count)

"""
enter a number: 9999
4
"""

# 3. WAP to find sum of digits in a number
# n = int(input("enter a number: "))
# sum = 0
# digit = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10
# print(sum)

# 1234 → last digit = 4 → sum = 0 + 4 = 4 → n = 123
# 123  → last digit = 3 → sum = 4 + 3 = 7 → n = 12
# 12   → last digit = 2 → sum = 7 + 2 = 9 → n = 1
# 1    → last digit = 1 → sum = 9 + 1 = 10 → n = 0
"""
enter a number: 1234
10
"""

# 4. WAP to find product of digits in a number
# n = int(input("enter a number: "))
# prod = 1
# digit = 0
# while n > 0:
#     digit = n % 10
#     prod = prod * digit
#     n = n // 10
# print(prod)

"""
enter a number: 123  
6
"""

# 5. WAP to find maximum digit in a number
# n = int(input("enter a number: "))

# max = 0  # stores the largest digit found

# while n > 0:
#     digit = n % 10  # extract last digit
#     if digit > max:
#         max = digit
#     n = n // 10  # remove last digit

# print(max)

"""
enter a number: 1580
8
"""

# 6. WAP to find minimum digit in a number
# n = int(input("enter a number: "))
# min = 9
# while n > 0:
#     digit = n % 10
#     if digit < min:
#         min = digit
#     n = n // 10
# print(min)

"""
enter a number: 12578
1
"""

# 7. WAP to count even digits in a number
# n = int(input("enter a number: "))
# count = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         count += 1
#     n = n // 10
# print(count)

"""
enter a number: 12345
2
"""

# 8. WAP to count odd digits in a number
# n = int(input("enter a number: "))
# count = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         count += 1
#     n = n // 10
# print(count)

"""
enter a number: 135726
4
"""
# 9. WAP to find sum of even digits in a number
# n = int(input("enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         sum = sum + digit
#     n = n // 10
# print(sum)

"""
enter a number: 246135
12
"""

# 10. WAP to find sum of odd digits in a number
# n = int(input("enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         sum = sum + digit
#     n = n // 10
# print(sum)

"""
enter a number: 123456
9
"""

# 11. WAP to find difference between even and odd digit sum
# n = int(input("enter a number: "))
# odd = 0
# even = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         odd = odd + digit
#     else:
#         even = even + digit
#     n = n // 10

# diff = even - odd
# print(diff)

# n = 1234

# digits:
# 4 → even sum = 4
# 3 → odd sum = 3
# 2 → even sum = 6
# 1 → odd sum = 4

# even = 6
# odd = 4

# diff = 6 - 4 = 2

"""
enter a number: 1234
2
"""

# 12. WAP to find digit frequency in a number

# n = int(input("enter a number: "))

# freq = {}  # dictionary to store digit counts

# while n > 0:
#     digit = n % 10  # extract last digit

#     if digit in freq:
#         freq[digit] += 1
#     else:
#         freq[digit] = 1

#     n = n // 10  # remove last digit

# print(freq)

"""
enter a number: 122334
{4: 1, 3: 2, 2: 2, 1: 1}
"""

# =========================
# REVERSE NUMBER
# =========================

# DIAGRAM:
# Reverse means reading digits from right to left
#
# Original Number:
#  12345
#
# Step:
#  12345 → read from right → 54321
#
# Visual flow:
# left → right  becomes  right → left
#
# SYNTAX DIAGRAM:
#  while number > 0:
#      |--------------------------|
#      | digit = number % 10      |
#      |--------------------------|
#      | rev = (rev * 10) + digit |
#      |--------------------------|
#      | number //= 10            |
#      |--------------------------|

# 13. WAP to reverse a number
# n = int(input("enter a number: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
# print(rev)

"""
enter a number: 1234
4321
"""

# 14. WAP to check palindrome number
# n = int(input("enter a number: "))
# temp = n
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
# if rev == temp:
#     print("it is palindrome number")
# else:
#     print("it is not palindrome number")

"""
enter a number: 121
it is palindrome number

enter a number: 256
it is not palindrome number
"""

# =========================
# PALINDROME NUMBER
# =========================

# DIAGRAM:
# A palindrome number looks the same from both sides
#
# Example:
# 121
#
# left side → 1 2 1 ← right side
#              ↖   ↗
#           mirror image
#
# SYNTAX DIAGRAM:
#  Extract & reverse all digits
#  if original_num == reversed_num:
#      |--------------------------|
#      | True Statement Block     |
#      | (It is a Palindrome)     |
#      |--------------------------|

# 15. WAP to check palindrome number
# n = int(input("enter a number: "))
# temp = n
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
# if rev == temp:
#     print("it is palindrome number")
# else:
#     print("it is not palindrome number")

"""
enter a number: 121
it is palindrome number

enter a number: 256
it is not palindrome number
"""

# =========================
# ARMSTRONG NUMBER
# =========================

# DIAGRAM:
# Each digit is raised to power (number of digits) and added
#
# Example: 153 (3 digits)
#
# 1³ + 5³ + 3³
# ↓    ↓    ↓
# 1 + 125 + 27 = 153
#
# Visual:
# digits → power → sum → original number
#
# SYNTAX DIAGRAM:
#  while number > 0:
#      |--------------------------|
#      | digit = number % 10      |
#      |--------------------------|
#      | sum += digit ** order    |
#      |--------------------------|
#      | number //= 10            |
#      |--------------------------|

# 16. WAP to check Armstrong number
# n = int(input("enter a number: "))
# s = n
# temp = n
# sum = 0
# power = 0

# while s > 0:
#     power += 1
#     s = s // 10

# while n > 0:
#     digit = n % 10
#     sum = sum + digit**power
#     n = n // 10

# if sum == temp:
#     print("it is armstrong number")
# else:
#     print("it is not armstrong number")

"""
enter a number: 153
it is armstrong number

enter a number: 1234
it is not armstrong number
"""

# 17. WAP to print Armstrong numbers from 1 to n
# n = int(input("enter a number: "))

# i = 1

# while i <= n:
#     temp = i
#     s = i
#     power = 0
#     total = 0

#     # count digits
#     while s > 0:
#         power += 1
#         s = s // 10

#     # compute Armstrong sum
#     s = i
#     while s > 0:
#         digit = s % 10
#         total += digit**power
#         s = s // 10

#     # check condition
#     if total == temp:
#         print(temp)

#     i += 1

"""
enter a number: 1700
1
2
3
4
5
6
7
8
9
153
370
371
407
1634
"""

# =========================
# STRONG NUMBER
# =========================

# DIAGRAM:
# Each digit is converted into factorial and added
#
# Example: 145
#
# 1! + 4! + 5!
# ↓    ↓    ↓
# 1 + 24 + 120 = 145
#
# Visual:
# digits → factorial → sum
#
# SYNTAX DIAGRAM:
#  while number > 0:
#      |--------------------------|
#      | digit = number % 10      |
#      |--------------------------|
#      | sum += factorial(digit)  |
#      |--------------------------|
#      | number //= 10            |
#      |--------------------------|

# 18. WAP to check strong number
# n = int(input("enter a number: "))
# temp = n
# total = 0
# while n > 0:
#     digit = n % 10
#     fact = i = 1

#     while i <= digit:
#         fact = fact * i
#         i += 1

#     total = total + fact
#     n = n // 10

# if total == temp:
#     print("it is a strong number")
# else:
#     print("it is not a strong number")

"""
enter a number: 145
it is a strong number

enter a number: 120
it is not a strong number
"""

# =========================
# PERFECT NUMBER
# =========================

# DIAGRAM:
# A number is split into its divisors and added
#
# Example: 6
#
# Divisors:
# 1, 2, 3
#
# 1 + 2 + 3 = 6
#
# Visual:
# number → divisors → sum = number
#
# SYNTAX DIAGRAM:
#  while i < number:
#      |--------------------------|
#      | if number % i == 0:      |
#      |     |--------------|     |
#      |     | sum += i     |     |
#      |     |--------------|     |
#      |--------------------------|
#      | i += 1                   |
#      |--------------------------|

# 19. WAP to check perfect number
# n = int(input("enter a number: "))
# temp = n
# i = 1
# sum = 0
# while i <= n // 2:
#     if n % i == 0:
#         sum += i
#     i += 1

# if temp == sum:
#     print("it is a perfect number")
# else:
#     print("it is not a perfect number")

"""
enter a number: 6
it is a perfect number

enter a number: 8
it is not a perfect number
"""

# =========================
# SPY NUMBER
# =========================

# DIAGRAM:
# Sum of digits equals product of digits
#
# Example: 123
#
# digits: 1, 2, 3
#
# Sum     = 1 + 2 + 3 = 6
# Product = 1 × 2 × 3 = 6
#
# Visual:
# SUM = PRODUCT ✔
#
# SYNTAX DIAGRAM:
#  while number > 0:
#      |--------------------------|
#      | digit = number % 10      |
#      |--------------------------|
#      | digit_sum += digit       |
#      |--------------------------|
#      | digit_prod *= digit      |
#      |--------------------------|
#      | number //= 10            |
#      |--------------------------|

# 20. WAP to check spy number
# n = int(input("enter a number: "))
# sum = 0
# prod = 1
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     prod = prod * digit
#     n = n // 10

# if sum == prod:
#     print("it is a spy number")
# else:
#     print("it is not a spy number")

"""
enter a number: 123
it is a spy number

enter a number: 145
it is not a spy number
"""

# =========================
# NEON NUMBER
# =========================

# DIAGRAM:
# Square the number → add digits of result
#
# Example: 9
#
# 9² = 81
#
# 8 + 1 = 9
#
# Visual:
# number → square → digit sum → original number
#
# SYNTAX DIAGRAM:
#  square = number * number
#  while square > 0:
#      |--------------------------|
#      | digit = square % 10      |
#      |--------------------------|
#      | digit_sum += digit       |
#      |--------------------------|
#      | square //= 10            |
#      |--------------------------|

# 21. WAP to check neon number
# n = int(input("enter a number: "))

# sq = n**2
# sum = 0
# while sq > 0:
#     digit = sq % 10
#     sum += digit
#     sq = sq // 10

# if sum == n:
#     print("it is a neon number")
# else:
#     print("it is not a neon number")

"""
enter a number: 9
it is a neon number

enter a number: 90
it is not a neon number
"""

# =========================
# AUTOMORPHIC NUMBER
# =========================

# DIAGRAM:
# Number appears at the end of its square
#
# Example: 5
#
# 5² = 25
#        ↑
#        5 appears at end
#
# Example: 6² = 36
#        ↑
#        6 appears at end
#
# Visual:
# number is suffix of square
#
# SYNTAX DIAGRAM:
#  square = number * number
#  while number > 0:
#      |--------------------------|
#      | if number%10 != square%10|
#      |     |--------------|     |
#      |     | status=False |     |
#      |     |--------------|     |
#      |--------------------------|
#      | number //= 10            |
#      | square //= 10            |
#      |--------------------------|

# 22. WAP to check automorphic number
# n = int(input("enter a number: "))
# sq = n * n
# flag = True
# while n > 0:
#     if n % 10 != sq % 10:
#         flag = False
#     n //= 10
#     sq //= 10
# if flag:
#     print("automorphic number")
# else:
#     print("not automorphic number")

"""
enter a number: 5
automorphic number

enter a number: 12
not automorphic number
"""


# =========================
# HARSHAD (NIVEN) NUMBER
# =========================

# DIAGRAM:
# Number is divisible by sum of its digits
#
# Example: 18
#
# digits → 1 + 8 = 9
# 18 ÷ 9 = 2 ✔
#
# Visual:
# number ÷ digit sum → remainder 0
#
# SYNTAX DIAGRAM:
#  while temp_num > 0:
#      |--------------------------|
#      | digit = temp_num % 10    |
#      |--------------------------|
#      | digit_sum += digit       |
#      |--------------------------|
#      | temp_num //= 10          |
#      |--------------------------|
#  if original_num % digit_sum == 0:

# 23. WAP to check harshad number
# n = int(input("enter a number: "))
# temp = n
# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10
# if temp % sum == 0:
#     print("harshad number")
# else:
#     print("not harshad number")

"""
enter a number: 18
harshad number

enter a number: 19
not harshad number
"""

# =========================
# BUZZ NUMBER
# =========================

# DIAGRAM:
# Number is divisible by 7 OR ends with 7
#
# Example:
# 7, 17, 27, 49
#
# Visual:
# ends with 7 OR divisible by 7
#
# SYNTAX DIAGRAM:
#  if number % 7 == 0 or number % 10 == 7:
#      |--------------------------|
#      | True Statement Block     |
#      | (It is a Buzz Number)    |
#      |--------------------------|

# 24. WAP to check buzz number
# n = int(input("enter a number: "))
# if n % 7 == 0 or n % 10 == 7:
#     print("buzz number")
# else:
#     print("not buzz number")

"""
enter a number: 7
buzz number

enter a number: 16
not buzz number
"""

# =========================
# PRONIC NUMBER
# =========================

# DIAGRAM:
# A number formed by multiplication of two consecutive numbers
#
# Example:
# 2 × 3 = 6
# 3 × 4 = 12
#
# Visual:
# n × (n+1)
#
# SYNTAX DIAGRAM:
#  while i * (i + 1) <= number:
#      |--------------------------|
#      | if i * (i + 1) == number:|
#      |     |--------------|     |
#      |     | status = True|     |
#      |     |--------------|     |
#      |--------------------------|
#      | i += 1                   |
#      |--------------------------|

# 25. WAP to check pronic number
# n = int(input("enter a number: "))
# i = 1
# flag = False
# while i * (i + 1) <= n:
#     if i * (i + 1) == n:
#         flag = True
#     i += 1
# if flag:
#     print("pronic number")
# else:
#     print("not pronic number")

"""
enter a number: 6
pronic number

enter a number: 10
not pronic number
"""

# =========================
# PRIME NUMBER
# =========================

# DIAGRAM:
# A number having only 2 factors
#
# Example:
# 7 → factors: 1, 7
#
# Visual:
# only two divisors
#
# SYNTAX DIAGRAM:
#  while i * i <= number:
#      |--------------------------|
#      | if number % i == 0:      |
#      |     |--------------|     |
#      |     | status=False |     |
#      |     |--------------|     |
#      |--------------------------|
#      | i += 1                   |
#      |--------------------------|

# 26. WAP to check prime number
# n = int(input("enter a number: "))
# if n <= 1:
#     print("not a prime number")
# else:
#     i = 2
#     while i * i <= n:
#         # n divisible by i → not prime
#         if n % i == 0:
#             print("not a prime number")
#             break
#         i += 1
#     else:
#         print("prime number")


"""
enter a number: 7
prime number

enter a number: 8
not a prime number

enter a number: 1
not a prime number
"""

# 27. WAP to print prime numbers from 1 to n
# n = int(input("enter range: "))
# num = 2   # start from first prime
# while num <= n:
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         print(num, end=" ")
#     num += 1

"""
enter range: 20
2 3 5 7 11 13 17 19

enter range: 10
2 3 5 7
"""

# =========================
# COMPOSITE NUMBER
# =========================

# DIAGRAM:
# A number having more than 2 factors
#
# Example:
# 6 → 1, 2, 3, 6
#
# Visual:
# multiple divisors
#
# SYNTAX DIAGRAM:
#  while i <= number // 2:
#      |--------------------------|
#      | if number % i == 0:      |
#      |     |--------------|     |
#      |     | factor_cnt+=1|     |
#      |     |--------------|     |
#      |--------------------------|
#      | i += 1                   |
#      |--------------------------|

# 28. WAP to check composite number
# n = int(input("enter a number: "))
# i = 1
# count = 0
# while i <= n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if count > 2:
#     print("composite number")
# else:
#     print("not composite number")

"""
enter a number: 6
composite number

enter a number: 7
not composite number
"""

# =========================
# XYLEM & PHLOEM NUMBER
# =========================

# DIAGRAM:
# Outer digits vs inner digits comparison
#
# Example: 1234
#
# Outer digits:
# 1 + 4 = 5
#
# Inner digits:
# 2 + 3 = 5
#
# If equal → XYLEM ✔
# If not equal → PHLOEM
#
# Visual:
# outer == inner OR outer != inner
#
# SYNTAX DIAGRAM:
#  outer_sum = last_digit + first_digit
#  while number > 9:
#      |--------------------------|
#      | digit = number % 10      |
#      |--------------------------|
#      | inner_sum += digit       |
#      |--------------------------|
#      | number //= 10            |
#      |--------------------------|

# 29. WAP to check xylem number
# n = int(input("enter a number: "))
# temp = n
# last = n % 10
# first = 0
# while temp > 0:
#     first = temp % 10
#     temp //= 10
# outer = first + last
# inner = 0
# temp = n // 10
# while temp > 9:
#     inner += temp % 10
#     temp //= 10
# if outer == inner:
#     print("xylem number")
# else:
#     print("phloem number")

"""
enter a number: 1234
xylem number

enter a number: 1213
phloem number
"""

# =========================
# TWIN PRIME
# =========================

# DIAGRAM:
# Two prime numbers with difference of 2
#
# Example:
# (3,5), (5,7), (11,13)
#
# Visual:
# prime —— gap 2 —— prime
#
# SYNTAX DIAGRAM:
#  if is_prime(n1) and is_prime(n2):
#      |--------------------------|
#      | if abs(n1 - n2) == 2:    |
#      |     |--------------|     |
#      |     | status = True|     |
#      |     |--------------|     |
#      |--------------------------|

# 30. WAP to check twin prime number


# =========================
# HAPPY NUMBER
# =========================

# DIAGRAM:
# Square digits repeatedly until result becomes 1
#
# Example:
# 19 →
# 1² + 9² = 82 →
# 8² + 2² = 68 →
# eventually → 1
#
# Visual:
# loop of digit squares → ends in 1
#
# SYNTAX DIAGRAM:
#  while number != 1 and number != 4:
#      |--------------------------|
#      | calc sum of squares of   |
#      | individual digits loop   |
#      |--------------------------|
#      | number = sum_of_squares  |
#      |--------------------------|

# 31. WAP to check happy number
# n = int(input("enter a number: "))
#
# def happy(n):
#     while n != 1 and n != 4:
#         temp = n
#         s = 0
#         while temp > 0:
#             d = temp % 10
#             s += d*d
#             temp //= 10
#         n = s
#     return n == 1
#
# if happy(n):
#     print("happy number")
# else:
#     print("not happy number")

"""
enter a number: 19
happy number

enter a number: 20
not happy number
"""
