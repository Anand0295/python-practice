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

# WAP:
# 1.wap to reverse a number
# 2.wap to count digits in a number
# 3.wap to find sum of digits in a number
# 4.wap to find product of digits in a number
# 5.wap to find maximum digit in a number
# 6.wap to find minimum digit in a number
# 7.wap to count even digits in a number
# 8.wap to count odd digits in a number
# 9.wap to find sum of even digits in a number
# 10.wap to find sum of odd digits in a number
# 11.wap to find difference between even and odd digit sum
# 12.wap to find digit frequency in a number


# =========================
# REVERSE NUMBER
# =========================

# DIAGRAM:
# Reverse means reading digits from right to left

# Original Number:
#  12345
#
# Step:
#  12345 → read from right → 54321

# Visual flow:
# left → right  becomes  right → left

# WAP:
# 13.wap to reverse a number
# 14.wap to check palindrome number


# =========================
# PALINDROME NUMBER
# =========================

# DIAGRAM:
# A palindrome number looks the same from both sides

# Example:
# 121
#
# left side → 1 2 1 ← right side
#              ↖   ↗
#           mirror image

# WAP:
# 15.wap to check palindrome number


# =========================
# ARMSTRONG NUMBER
# =========================

# DIAGRAM:
# Each digit is raised to power (number of digits) and added

# Example: 153 (3 digits)

# 1³ + 5³ + 3³
# ↓    ↓    ↓
# 1 + 125 + 27 = 153

# Visual:
# digits → power → sum → original number

# WAP:
# 16.wap to check Armstrong number
# 17.wap to print Armstrong numbers from 1 to n


# =========================
# STRONG NUMBER
# =========================

# DIAGRAM:
# Each digit is converted into factorial and added

# Example: 145

# 1! + 4! + 5!
# ↓    ↓    ↓
# 1 + 24 + 120 = 145

# Visual:
# digits → factorial → sum

# WAP:
# 18.wap to check strong number


# =========================
# PERFECT NUMBER
# =========================

# DIAGRAM:
# A number is split into its divisors and added

# Example: 6

# Divisors:
# 1, 2, 3
#
# 1 + 2 + 3 = 6

# Visual:
# number → divisors → sum = number

# WAP:
# 19.wap to check perfect number


# =========================
# SPY NUMBER
# =========================

# DIAGRAM:
# Sum of digits equals product of digits

# Example: 123

# digits: 1, 2, 3
#
# Sum     = 1 + 2 + 3 = 6
# Product = 1 × 2 × 3 = 6

# Visual:
# SUM = PRODUCT ✔

# WAP:
# 20.wap to check spy number


# =========================
# NEON NUMBER
# =========================

# DIAGRAM:
# Square the number → add digits of result

# Example: 9

# 9² = 81
#
# 8 + 1 = 9

# Visual:
# number → square → digit sum → original number

# WAP:
# 21.wap to check neon number


# =========================
# AUTOMORPHIC NUMBER
# =========================

# DIAGRAM:
# Number appears at the end of its square

# Example: 5

# 5² = 25
#        ↑
#        5 appears at end

# Example: 6² = 36
#        ↑
#        6 appears at end

# Visual:
# number is suffix of square

# WAP:
# 22.wap to check automorphic number


# =========================
# HARSHAD (NIVEN) NUMBER
# =========================

# DIAGRAM:
# Number is divisible by sum of its digits

# Example: 18

# digits → 1 + 8 = 9
# 18 ÷ 9 = 2 ✔

# Visual:
# number ÷ digit sum → remainder 0

# WAP:
# 23.wap to check harshad number


# =========================
# BUZZ NUMBER
# =========================

# DIAGRAM:
# Number is divisible by 7 OR ends with 7

# Example:
# 7, 17, 27, 49

# Visual:
# ends with 7 OR divisible by 7

# WAP:
# 24.wap to check buzz number


# =========================
# PRONIC NUMBER
# =========================

# DIAGRAM:
# A number formed by multiplication of two consecutive numbers

# Example:

# 2 × 3 = 6
# 3 × 4 = 12

# Visual:
# n × (n+1)

# WAP:
# 25.wap to check pronic number


# =========================
# PRIME NUMBER
# =========================

# DIAGRAM:
# A number having only 2 factors

# Example:

# 7 → factors: 1, 7

# Visual:
# only two divisors

# WAP:
# 26.wap to check prime number
# 27.wap to print prime numbers from 1 to n


# =========================
# COMPOSITE NUMBER
# =========================

# DIAGRAM:
# A number having more than 2 factors

# Example:

# 6 → 1, 2, 3, 6

# Visual:
# multiple divisors

# WAP:
# 28.wap to check composite number


# =========================
# XYLEM & PHLOEM NUMBER
# =========================

# DIAGRAM:
# Outer digits vs inner digits comparison

# Example: 1234

# Outer digits:
# 1 + 4 = 5

# Inner digits:
# 2 + 3 = 5

# If equal → XYLEM ✔
# If not equal → PHLOEM

# Visual:
# outer == inner OR outer != inner

# WAP:
# 29.wap to check xylem number


# =========================
# TWIN PRIME
# =========================

# DIAGRAM:
# Two prime numbers with difference of 2

# Example:
# (3,5), (5,7), (11,13)

# Visual:
# prime —— gap 2 —— prime

# WAP:
# 30.wap to check twin prime number


# =========================
# HAPPY NUMBER
# =========================

# DIAGRAM:
# Square digits repeatedly until result becomes 1

# Example:
# 19 →
# 1² + 9² = 82 →
# 8² + 2² = 68 →
# eventually → 1

# Visual:
# loop of digit squares → ends in 1

# WAP:
# 31.wap to check happy number
