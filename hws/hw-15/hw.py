"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
from hws.hw1.exx import solution


class Pizza:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError("Ingredient already in there!")

        self.ingredients.append(ingredient)

"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def get_current_floor(self):
        return self.current_floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств для снятие!")

    def check_balance(self):
        return self.balance


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Возврат не может быть отрицательным!")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1



"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        pass


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        pass

    @staticmethod
    def subtract(x, y):
        pass

    @staticmethod
    def multiply(x, y):
        pass

    @staticmethod
    def divide(x, y):
        pass


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if mileage < 0 or speed < 0:
            raise ValueError("Negative Value!")

        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        return self.students


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        self.departure = delay_time


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        pass

    def add(self, other):
        pass

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return  2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Negative radius!")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Invalid triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(AbstractShape):
    def __init__(self, radius):
        pass

class Rectangle(AbstractShape):
    def __init__(self, height, width):
        pass

class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        pass

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def play_song(self):
        if self.songs:
            return self.songs[self.current_index]
        else:
            return "Playlist is empty."

    def next_song(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            print(f"Now playing: {self.songs[self.current_index]}")
        else:
            print("Playlist is empty.")

    def shuffle(self):
        if self.songs:
            random.shuffle(self.songs)
            self.current_index = 0
            print(f"Playlist shuffled! Now playing: {self.songs[self.current_index]}")
        else:
            print("Playlist is empty.")


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(f"Added {quantity} units to stock.")
        else:
            raise ValueError("Invalid quantity. Must be greater than 0.")

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity. Must be greater than 0.")
        elif self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} units of {self.name}.")
        else:
            print(f"Not enough stock! Only {self.quantity} left.")

    def check_stock(self):
        print(f"Current stock of {self.name}: {self.quantity} units.")
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}")


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def print_all(self):
        return self.students + self.teachers

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("No cards left to deal.")

    def count(self):
        return len(self.cards)
