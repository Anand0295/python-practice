# =========================================================
#                    FUNCTIONS ROADMAP
# =========================================================


# =========================================================
# FUNCTION STRUCTURE
# =========================================================

# def function_name(parameters):
#     |--------------------------------|
#     |  function body                 |
#     |  calculations / logic          |
#     |--------------------------------|
#     return value

# function_name(arguments)


# =========================================================
# PRINT FUNCTION
# =========================================================

# def display():
#     |--------------------------------|
#     |  directly prints output        |
#     |--------------------------------|

# QUESTIONS:
# 1. WAP to print hello world using function
# def prnt():
#     print("hello world")


# prnt()

"""
hello world
"""


# 2. WAP to print your name using function
# def name(name):
#     print(name)


# name(input("enter your name: "))

"""
enter your name: Anand
Anand
"""


# 3. WAP to print numbers from 1 to 10 using function
# def num():
#     for i in range(1, 11):
#         print(i, end=" ")

# num()

"""
1 2 3 4 5 6 7 8 9 10
"""


# 4. WAP to print even numbers using function
def even(no):
    for i in range(1, no + 1):
        if i % 2 == 0:
            print(i)


even(int(input("enter a number: ")))
# 5. WAP to print multiplication table using function


# =========================================================
# RETURN FUNCTION
# =========================================================

# def add(a,b):
#     |--------------------------------|
#     |  calculate result              |
#     |--------------------------------|
#     return result

# QUESTIONS:
# 6. WAP to return sum of two numbers
# 7. WAP to return square of a number
# 8. WAP to return cube of a number
# 9. WAP to return factorial of number
# 10. WAP to return reversed string


# =========================================================
# POSITIONAL ARGUMENTS
# =========================================================

# def function_name(a,b):
#     |--------------------------------|
#     | arguments mapped by position   |
#     |--------------------------------|

# function_name(10,20)

# a = 10
# b = 20

# QUESTIONS:
# 11. WAP to add two numbers using positional arguments
# 12. WAP to subtract two numbers using positional arguments
# 13. WAP to multiply two numbers using positional arguments
# 14. WAP to divide two numbers using positional arguments
# 15. WAP to swap two numbers using positional arguments


# =========================================================
# KEYWORD ARGUMENTS
# =========================================================

# def function_name(a,b):
#     |--------------------------------|
#     | values assigned using keyword  |
#     |--------------------------------|

# function_name(b=20,a=10)

# QUESTIONS:
# 16. WAP to create student details using keyword args
# 17. WAP to create employee details using keyword args
# 18. WAP to create bank account using keyword args
# 19. WAP to create product bill using keyword args
# 20. WAP to create login system using keyword args


# =========================================================
# DEFAULT PARAMETERS
# =========================================================

# def function_name(a,b=10):
#     |--------------------------------|
#     | uses default value if missing  |
#     |--------------------------------|

# QUESTIONS:
# 21. WAP to add numbers using default parameter
# 22. WAP to calculate SI using default rate
# 23. WAP to print greeting using default parameter
# 24. WAP to calculate salary with default bonus
# 25. WAP to create default login credentials


# =========================================================
# VARIABLE LENGTH ARGUMENTS (*args)
# =========================================================

# def function_name(*args):
#     |--------------------------------|
#     | stores multiple values tuple   |
#     |--------------------------------|

# function_name(1,2,3,4)

# QUESTIONS:
# 26. WAP to find sum using *args
# 27. WAP to find largest number using *args
# 28. WAP to multiply all numbers using *args
# 29. WAP to print all elements using *args
# 30. WAP to count total arguments using *args


# =========================================================
# VARIABLE KEYWORD ARGUMENTS (**kwargs)
# =========================================================

# def function_name(**kwargs):
#     |--------------------------------|
#     | stores key-value dictionary    |
#     |--------------------------------|

# QUESTIONS:
# 31. WAP to create student dictionary using **kwargs
# 32. WAP to create employee dictionary using **kwargs
# 33. WAP to create product details using **kwargs
# 34. WAP to print keys and values using **kwargs
# 35. WAP to count keyword arguments using **kwargs


# =========================================================
# ONLY POSITIONAL ARGUMENTS (/)
# =========================================================

# def function_name(a,b,/):
#     |--------------------------------|
#     | arguments must be positional   |
#     |--------------------------------|

# QUESTIONS:
# 36. WAP to add numbers using only positional args
# 37. WAP to calculate area using only positional args
# 38. WAP to compare numbers using only positional args
# 39. WAP to calculate average using only positional args
# 40. WAP to print student marks using only positional args


# =========================================================
# ONLY KEYWORD ARGUMENTS (*)
# =========================================================

# def function_name(*,a,b):
#     |--------------------------------|
#     | arguments must be keyword      |
#     |--------------------------------|

# QUESTIONS:
# 41. WAP to add numbers using keyword-only args
# 42. WAP to calculate bill using keyword-only args
# 43. WAP to calculate salary using keyword-only args
# 44. WAP to create login form using keyword-only args
# 45. WAP to create bank details using keyword-only args


# =========================================================
# COMBINATION OF (/, *)
# =========================================================

# def function_name(a,b,/,*,c,d):
#     |--------------------------------|
#     | a,b -> positional only         |
#     | c,d -> keyword only            |
#     |--------------------------------|

# QUESTIONS:
# 46. WAP to calculate total marks using / and *
# 47. WAP to create payroll system using / and *
# 48. WAP to create billing system using / and *
# 49. WAP to create bank transaction using / and *
# 50. WAP to create employee report using / and *


# =========================================================
# STRING FUNCTIONS
# =========================================================

# def string_function(s):
#     |--------------------------------|
#     | traverse characters            |
#     | perform string operations      |
#     |--------------------------------|

# QUESTIONS:
# 51. WAP to reverse string using function
# 52. WAP to count vowels using function
# 53. WAP to count consonants using function
# 54. WAP to count digits using function
# 55. WAP to count special characters using function
# 56. WAP to remove spaces using function
# 57. WAP to check palindrome string using function
# 58. WAP to capitalize alternate characters using function
# 59. WAP to count words using function
# 60. WAP to replace vowels using function


# =========================================================
# LIST FUNCTIONS
# =========================================================

# def list_function(lst):
#     |--------------------------------|
#     | traverse list                  |
#     | modify / compare elements      |
#     |--------------------------------|

# QUESTIONS:
# 61. WAP to find largest element using function
# 62. WAP to find smallest element using function
# 63. WAP to reverse list using function
# 64. WAP to remove duplicates using function
# 65. WAP to create squares list using function
# 66. WAP to create cubes list using function
# 67. WAP to count even numbers using function
# 68. WAP to count odd numbers using function
# 69. WAP to rotate list left using function
# 70. WAP to rotate list right using function


# =========================================================
# NUMBER FUNCTIONS
# =========================================================

# def number_function(n):
#     |--------------------------------|
#     | mathematical calculations      |
#     |--------------------------------|

# QUESTIONS:
# 71. WAP to check prime number using function
# 72. WAP to print prime numbers using function
# 73. WAP to print Armstrong numbers using function
# 74. WAP to print palindrome numbers using function
# 75. WAP to print perfect numbers using function
# 76. WAP to print strong numbers using function
# 77. WAP to print Fibonacci series using function
# 78. WAP to find sum of digits using function
# 79. WAP to reverse a number using function
# 80. WAP to count digits using function


# =========================================================
# PATTERN FUNCTIONS
# =========================================================

# def pattern_function(no):
#     |--------------------------------|
#     | outer loop -> rows             |
#     | inner loop -> columns          |
#     |--------------------------------|

# QUESTIONS:
# 81. WAP to print square pattern using function
# 82. WAP to print hollow square using function
# 83. WAP to print triangle pattern using function
# 84. WAP to print reverse triangle using function
# 85. WAP to print pyramid pattern using function
# 86. WAP to print reverse pyramid using function
# 87. WAP to print diamond pattern using function
# 88. WAP to print butterfly pattern using function
# 89. WAP to print X pattern using function
# 90. WAP to print plus pattern using function


# =========================================================
# ALPHABET PATTERN FUNCTIONS
# =========================================================

# FORMULAS:
#
# left line      -> j == 0
# right line     -> j == no-1
# top line       -> i == 0
# middle line    -> i == no//2
# bottom line    -> i == no-1
# diagonal       -> i == j
# opposite diag  -> i+j == no-1

# QUESTIONS:
# 91. WAP to print letter A using function
# 92. WAP to print letter B using function
# 93. WAP to print letter C using function
# 94. WAP to print letter D using function
# 95. WAP to print letter E using function
# 96. WAP to print letter H using function
# 97. WAP to print letter M using function
# 98. WAP to print letter X using function
# 99. WAP to print letter Y using function
# 100. WAP to print your name using star patterns and functions


# =========================================================
# EXTRA FUNCTIONS
# =========================================================

# 101. WAP to create nested functions
# 102. WAP to call inner function from outer function
# 103. WAP to return function from another function
# 104. WAP to pass function as argument
# 105. WAP to create calculator using multiple functions
# 106. WAP to create ATM application using functions
# 107. WAP to create library management using functions
# 108. WAP to create student management system using functions
# 109. WAP to create employee payroll using functions
# 110. WAP to create shopping cart using functions

# =========================================================
# RECURSION
# =========================================================

# def fun(n):
#     |------------------------------|
#     | function calls itself        |
#     |------------------------------|

# 111. WAP to find factorial using recursion
# 112. WAP to print Fibonacci using recursion
# 113. WAP to reverse string using recursion
# 114. WAP to calculate power using recursion
# 115. WAP to find sum of digits using recursion
# 116. WAP to count digits using recursion
# 117. WAP to check palindrome using recursion
# 118. WAP to print numbers from 1 to n using recursion
# 119. WAP to print numbers from n to 1 using recursion
# 120. WAP to find GCD using recursion

# =========================================================
# REAL-TIME FUNCTION PROGRAMS
# =========================================================

# 121. WAP to create login authentication system
# 122. WAP to create signup validation system
# 123. WAP to create password validation function
# 124. WAP to create email validation function
# 125. WAP to create OTP generator function
# 126. WAP to create banking transaction system
# 127. WAP to create billing system
# 128. WAP to create attendance management system
# 129. WAP to create marks card generator
# 130. WAP to create result processing system

# =========================================================
# ADVANCED ARGUMENT COMBINATIONS
# =========================================================

# def fun(a,b,/ , c,d , *args , e,f , **kwargs):
#     |------------------------------|
#     | all argument types together  |
#     |------------------------------|

# 131. WAP using positional + keyword + *args together
# 132. WAP using positional-only + keyword-only together
# 133. WAP using *args and **kwargs together
# 134. WAP to create dynamic calculator using *args
# 135. WAP to create dynamic dictionary using **kwargs
# 136. WAP to create flexible student report system
# 137. WAP to create invoice generator
# 138. WAP to create salary slip generator
# 139. WAP to create online order system
# 140. WAP to create dynamic menu-driven application

# =========================================================
# FUNCTION + PATTERN COMBINATIONS
# =========================================================

# 141. WAP to create star pattern functions
# 142. WAP to create alphabet pattern functions
# 143. WAP to create number pattern functions
# 144. WAP to create hollow pattern functions
# 145. WAP to create diagonal patterns using functions
# 146. WAP to create butterfly pattern using functions
# 147. WAP to create diamond pattern using functions
# 148. WAP to print your name using functions and patterns
# 149. WAP to print INDIA using star patterns
# 150. WAP to print PYTHON using star patterns
