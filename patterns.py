# ============================================================
#                    PATTERN FORMULAS + QUESTIONS
# ============================================================


# ============================================================
# SOLID SQUARE
# ============================================================

# FORMULA:
# i -> rows
# j -> columns
# print when:
# always print

# DIAGRAM:
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# CODE STRUCTURE:
# for i in range(no):
#     for j in range(no):
#         print('*', end=' ')
#     print()

# QUESTIONS:
# 1. WAP to print solid square star pattern
# 2. WAP to print solid number square
# 3. WAP to print solid alphabet square
# 4. WAP to print coordinates matrix
# 5. WAP to print multiplication square matrix


# ============================================================
# HOLLOW SQUARE
# ============================================================

# FORMULA:
# print when:
# i == 0
# j == 0
# i == no-1
# j == no-1

# DIAGRAM:
"""
* * * * *
*       *
*       *
*       *
* * * * *
"""

# CODE STRUCTURE:
# if i==0 or j==0 or i==no-1 or j==no-1

# QUESTIONS:
# 6. WAP to print hollow square
# 7. WAP to print hollow number square
# 8. WAP to print hollow alphabet square
# 9. WAP to print double hollow square
# 10. WAP to print hollow box with diagonals


# ============================================================
# PLUS PATTERN
# ============================================================

# FORMULA:
# print when:
# i == no//2
# j == no//2

# DIAGRAM:
"""
    *
    *
* * * * *
    *
    *
"""

# CODE STRUCTURE:
# if i==no//2 or j==no//2

# QUESTIONS:
# 11. WAP to print plus pattern
# 12. WAP to print hollow plus pattern
# 13. WAP to print thick plus pattern
# 14. WAP to print number plus pattern
# 15. WAP to print alphabet plus pattern


# ============================================================
# LEFT DIAGONAL
# ============================================================

# FORMULA:
# print when:
# i == j

# DIAGRAM:
"""
*
  *
    *
      *
        *
"""

# CODE STRUCTURE:
# if i==j

# QUESTIONS:
# 16. WAP to print left diagonal
# 17. WAP to print diagonal numbers
# 18. WAP to print diagonal alphabets
# 19. WAP to print hollow diagonal square
# 20. WAP to print double diagonal


# ============================================================
# RIGHT DIAGONAL
# ============================================================

# FORMULA:
# print when:
# i + j == no-1

# DIAGRAM:
"""
        *
      *
    *
  *
*
"""

# CODE STRUCTURE:
# if i+j==no-1

# QUESTIONS:
# 21. WAP to print right diagonal
# 22. WAP to print reverse diagonal numbers
# 23. WAP to print reverse diagonal alphabets
# 24. WAP to print hollow reverse diagonal
# 25. WAP to print X pattern


# ============================================================
# X PATTERN
# ============================================================

# FORMULA:
# print when:
# i == j
# i + j == no-1

# DIAGRAM:
"""
*       *
  *   *
    *
  *   *
*       *
"""

# CODE STRUCTURE:
# if i==j or i+j==no-1

# QUESTIONS:
# 26. WAP to print X pattern
# 27. WAP to print hollow X pattern
# 28. WAP to print number X pattern
# 29. WAP to print alphabet X pattern
# 30. WAP to print thick X pattern


# ============================================================
# LEFT TRIANGLE
# ============================================================

# FORMULA:
# print when:
# i >= j

# DIAGRAM:
"""
*
* *
* * *
* * * *
* * * * *
"""

# CODE STRUCTURE:
# if i>=j

# QUESTIONS:
# 31. WAP to print left triangle
# 32. WAP to print left number triangle
# 33. WAP to print left alphabet triangle
# 34. WAP to print Floyd triangle
# 35. WAP to print Pascal triangle


# ============================================================
# REVERSE LEFT TRIANGLE
# ============================================================

# FORMULA:
# print when:
# i + j <= no-1

# DIAGRAM:
"""
* * * * *
* * * *
* * *
* *
*
"""

# CODE STRUCTURE:
# if i+j<=no-1

# QUESTIONS:
# 36. WAP to print reverse left triangle
# 37. WAP to print reverse number triangle
# 38. WAP to print reverse alphabet triangle
# 39. WAP to print reverse Floyd triangle
# 40. WAP to print reverse Pascal triangle


# ============================================================
# PYRAMID
# ============================================================

# FORMULA:
# spaces = no-i
# stars = i

# DIAGRAM:
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

# CODE STRUCTURE:
# print(' '*(no-i), end='')
# print('* '*i)

# QUESTIONS:
# 41. WAP to print star pyramid
# 42. WAP to print number pyramid
# 43. WAP to print alphabet pyramid
# 44. WAP to print centered Floyd triangle
# 45. WAP to print palindrome pyramid


# ============================================================
# REVERSE PYRAMID
# ============================================================

# FORMULA:
# spaces = no-j
# stars = j

# DIAGRAM:
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

# CODE STRUCTURE:
# for j in range(no,0,-1)

# QUESTIONS:
# 46. WAP to print reverse pyramid
# 47. WAP to print reverse number pyramid
# 48. WAP to print reverse alphabet pyramid
# 49. WAP to print inverted Floyd triangle
# 50. WAP to print reverse palindrome pyramid


# ============================================================
# DIAMOND
# ============================================================

# FORMULA:
# upper pyramid + lower reverse pyramid

# DIAGRAM:
"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""

# QUESTIONS:
# 51. WAP to print diamond pattern
# 52. WAP to print hollow diamond
# 53. WAP to print number diamond
# 54. WAP to print alphabet diamond
# 55. WAP to print palindrome diamond


# ============================================================
# BUTTERFLY PATTERN
# ============================================================

# FORMULA:
# left stars + middle spaces + right stars

# DIAGRAM:
"""
*        *
**      **
***    ***
****  ****
**********
"""

# QUESTIONS:
# 56. WAP to print butterfly pattern
# 57. WAP to print reverse butterfly
# 58. WAP to print hollow butterfly
# 59. WAP to print number butterfly
# 60. WAP to print alphabet butterfly


# ============================================================
# HOURGLASS
# ============================================================

# FORMULA:
# reverse pyramid + pyramid

# DIAGRAM:
"""
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""

# QUESTIONS:
# 61. WAP to print hourglass pattern
# 62. WAP to print hollow hourglass
# 63. WAP to print number hourglass
# 64. WAP to print alphabet hourglass
# 65. WAP to print palindrome hourglass


# ============================================================
# HOLLOW TRIANGLE
# ============================================================

# FORMULA:
# print when:
# j == 0
# i == no-1
# i == j

# DIAGRAM:
"""
*
* *
*   *
*     *
* * * * *
"""

# QUESTIONS:
# 66. WAP to print hollow left triangle
# 67. WAP to print hollow reverse triangle
# 68. WAP to print hollow number triangle
# 69. WAP to print hollow alphabet triangle
# 70. WAP to print hollow centered triangle


# ============================================================
# ALPHABET PATTERNS
# ============================================================

# FORMULA:
# chr(65+i) -> uppercase
# chr(97+i) -> lowercase

# DIAGRAM:
"""
A
A B
A B C
A B C D
A B C D E
"""

# QUESTIONS:
# 71. WAP to print alphabet triangle
# 72. WAP to print reverse alphabet triangle
# 73. WAP to print alphabet pyramid
# 74. WAP to print alphabet diamond
# 75. WAP to print continuous alphabets


# ============================================================
# NUMBER PATTERNS
# ============================================================

# FORMULA:
# print(i)
# print(j)
# print(count)

# DIAGRAM:
"""
1
1 2
1 2 3
1 2 3 4
"""

# QUESTIONS:
# 76. WAP to print increasing number triangle
# 77. WAP to print decreasing number triangle
# 78. WAP to print repeated number triangle
# 79. WAP to print continuous numbers
# 80. WAP to print snake number pattern


# ============================================================
# SPECIAL PATTERNS
# ============================================================

# QUESTIONS:
# 81. WAP to print chessboard pattern
# 82. WAP to print zig-zag pattern
# 83. WAP to print wave pattern
# 84. WAP to print spiral matrix
# 85. WAP to print hollow pyramid
# 86. WAP to print hollow reverse pyramid
# 87. WAP to print hollow diamond
# 88. WAP to print star circle approximation
# 89. WAP to print border diagonals
# 90. WAP to print matrix boundary


# ============================================================
# MATRIX + INDEX PATTERNS
# ============================================================

# QUESTIONS:
# 91. WAP to print matrix coordinates
# 92. WAP to print row index matrix
# 93. WAP to print column index matrix
# 94. WAP to print transpose matrix
# 95. WAP to print identity matrix
# 96. WAP to print lower triangular matrix
# 97. WAP to print upper triangular matrix
# 98. WAP to print diagonal matrix
# 99. WAP to print anti-diagonal matrix
# 100. WAP to print matrix multiplication pattern


# ============================================================
# BONUS QUESTIONS
# ============================================================

# 101. WAP to print hollow butterfly
# 102. WAP to print mirrored triangle
# 103. WAP to print mirrored pyramid
# 104. WAP to print double pyramid
# 105. WAP to print sandglass pattern
# 106. WAP to print binary triangle
# 107. WAP to print alternating 0-1 triangle
# 108. WAP to print character pyramid
# 109. WAP to print concentric square pattern
# 110. WAP to print rangoli pattern
# 111. WAP to print swastik pattern
# 112. WAP to print heart pattern
# 113. WAP to print arrow pattern
# 114. WAP to print kite pattern
# 115. WAP to print staircase pattern
# 116. WAP to print hollow staircase
# 117. WAP to print mountain pattern
# 118. WAP to print valley pattern
# 119. WAP to print hill pattern
# 120. WAP to print nested box pattern
