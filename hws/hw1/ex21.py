# Exercise 21: exponentiation
#
# Declare a palindrome string (A palindrome is a word that is spelled the same forward and backward. ex: "racecar")
# Check if it is palindromic without using loops

def solution(word):
    return word == word[::-1]

print(solution('car'))
