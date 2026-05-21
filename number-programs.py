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

# TODO: 1. WAP to reverse a number
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

# TODO: 2. WAP to count digits in a number
n = int(input("enter a number: "))
i = 0
count = 0
while i < n + 1:
    count += 1
    i += 1
print(count)

"""

"""
# TODO: 3. WAP to find sum of digits in a number
# TODO: 4. WAP to find product of digits in a number
# TODO: 5. WAP to find maximum digit in a number
# TODO: 6. WAP to find minimum digit in a number
# TODO: 7. WAP to count even digits in a number
# TODO: 8. WAP to count odd digits in a number
# TODO: 9. WAP to find sum of even digits in a number
# TODO: 10. WAP to find sum of odd digits in a number
# TODO: 11. WAP to find difference between even and odd digit sum
# TODO: 12. WAP to find digit frequency in a number


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

# TODO: 13. WAP to reverse a number
# TODO: 14. WAP to check palindrome number


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

# TODO: 15. WAP to check palindrome number


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

# TODO: 16. WAP to check Armstrong number
# TODO: 17. WAP to print Armstrong numbers from 1 to n


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

# TODO: 18. WAP to check strong number


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

# TODO: 19. WAP to check perfect number


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

# TODO: 20. WAP to check spy number


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

# TODO: 21. WAP to check neon number


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

# TODO: 22. WAP to check automorphic number


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

# TODO: 23. WAP to check harshad number


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

# TODO: 24. WAP to check buzz number


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

# TODO: 25. WAP to check pronic number


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

# TODO: 26. WAP to check prime number
# TODO: 27. WAP to print prime numbers from 1 to n


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

# TODO: 28. WAP to check composite number


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

# TODO: 29. WAP to check xylem number


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

# TODO: 30. WAP to check twin prime number


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

# TODO: 31. WAP to check happy number
