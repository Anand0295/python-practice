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
n = 10
for i in range(n, 1):
    print(i, end=" ")
# 28. WAP to print even numbers from 1 to 100
# 29. WAP to print odd numbers from 1 to n
# 30. WAP to print multiplication table
# 31. WAP to print multiplication tables from 1 to 10
# 32. WAP to print squares from 1 to n
# 33. WAP to print cubes from 1 to n
# 34. WAP to print factorial of number
# 35. WAP to print Fibonacci series
# 36. WAP to print star pattern
# 37. WAP to print reverse star pattern
# 38. WAP to print right angle triangle pattern
# 39. WAP to print alphabet pattern
# 40. WAP to print ASCII values A-Z
# 41. WAP to print ASCII values a-z
# 42. WAP to print divisors of number
# 43. WAP to check prime number
# 44. WAP to print prime numbers from 1 to n
# 45. WAP to print Armstrong numbers from 1 to n
# 46. WAP to print perfect numbers from 1 to n
# 47. WAP to print strong numbers from 1 to n
# 48. WAP to print palindrome numbers from 1 to n
# 49. WAP to print leap years between ranges
# 50. WAP to print tables in reverse order


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
# 52. WAP to print index and character from string
# 53. WAP to print even index characters
# 54. WAP to print odd index characters
# 55. WAP to find index of vowels
# 56. WAP to create dictionary with index and value
# 57. WAP to print elements greater than index
# 58. WAP to replace even index values with square
# 59. WAP to print index positions of spaces
# 60. WAP to count indexes containing vowels
# 61. WAP to print indexes divisible by 3
# 62. WAP to reverse indexes and values
# 63. WAP to create tuple of index and word
# 64. WAP to print elements whose index is prime
# 65. WAP to print characters with ASCII values


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
# 67. WAP to multiply elements of two lists
# 68. WAP to combine names and marks
# 69. WAP to create dictionary from two lists
# 70. WAP to print bigger value among pairs
# 71. WAP to print smaller value among pairs
# 72. WAP to concatenate strings from two lists
# 73. WAP to compare elements of two lists
# 74. WAP to count matching elements
# 75. WAP to merge tuple elements
# 76. WAP to print student name with grade
# 77. WAP to create list of tuples
# 78. WAP to unzip list of tuples
# 79. WAP to print sum of pair values
# 80. WAP to print product of pair values
# 81. WAP to combine keys and values into dictionary
# 82. WAP to compare characters of two strings
# 83. WAP to create matrix addition using zip
# 84. WAP to transpose matrix using zip
# 85. WAP to pair vowels and consonants


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


# 86. WAP to combine unequal lists
# 87. WAP to merge strings of unequal length
# 88. WAP to create dictionary from unequal lists
# 89. WAP to replace missing values with 0
# 90. WAP to replace missing values with '*'
# 91. WAP to print longest paired sequence
# 92. WAP to compare unequal tuples
# 93. WAP to align names and marks
# 94. WAP to merge uneven matrices
# 95. WAP to print missing positions


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
# 97. WAP to sort list in descending order
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
