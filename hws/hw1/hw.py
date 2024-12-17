#EX1
def solution(a, b):
    return a + b

print(solution(a = 5, b = 7))

#EX2
def reversed(word1):
    return word1[::-1]

print(reversed("games"))

#EX3
def lenword(word1):
    return len(word1)

print(lenword("games"))

#EX4
def plusstring(word1, word2):
    return word1 + word2

print(plusstring("games", "play"))

#EX5
def vowel(character):
    match character:
        case "a" | "e" | "i" | "o" | "u":
            return "Character is vowel"
        case _:
            return "Character is not vowel"

print(vowel("b"))

#EX6
def swap(word1):
    first, last = word1[0], word1[-1]
    return last + word1[1:-1] + first

print(swap("games"))

#EX7
def upper_word(word1):
    return word1.upper()

print(upper_word("games"))

#EX8
def rectangle(l, w):
    return l * w

print(rectangle(l = 150, w = 20))

#EX9
def even_number(numbers):
    if numbers % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

print(even_number(10))

#EX10
def words(word1):
    return word1[0:3]

print(words("games"))

#EX11
def interpol(name, age):
    return (f"My name is {name}. I am {age} years old.")

print(interpol(name="Bauyrzhan", age="26"))

#EX12
def word(characters):
    return characters[2:5]

print(word("Bauyrzhan"))

#EX13
numbers = "0027"

def convert(numbers):
    return int(numbers)

print(convert(numbers))

#EX14
word = "Baurzhan"

def repeated(word):
    return word * 3

print(repeated(word))

#EX15
num1 = 10
num2 = 5

print("Quotient: ", num1 // num2)
print("Remainder: ", num1 % num2)

#EX16
num1, num2 = float(10), float(3)

print("Float Result: ", num1 // num2)

#EX17
word = "ultimate fight championship"
letter_count = "a"

count = word.count(letter_count)

print(f"Character {letter_count} appears {count} times")

#EX18
words = "Hello World, \"Hello, World!\""

print(words)

#EX19
multi_string = """Hello.
My name is.
Bauyrzhan."""

print(multi_string)

#EX20
def solution(base, exponent):
    return base ** exponent

print(solution(2, 3))