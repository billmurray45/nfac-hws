import json
import os


def get_ascii_letter(filename):
    with open(filename, "r") as file:
        return json.load(file)


def get_ascii_art(ascii_file, ascii_dict, char):
    if char not in ascii_dict:
        return "Char not found!"

    start, end = ascii_dict[char]

    with open(ascii_file, "r") as file:
        lines = file.readlines()
        return [line.rstrip("\n") for line in lines[start - 1:end]]


def get_ascii_word(ascii_file, ascii_dict, word):
    ascii_lines = [get_ascii_art(ascii_file, ascii_dict, char) for char in word]
    max_height = max(len(art) for art in ascii_lines)
    ascii_lines = [[" " * len(art[0])] * (max_height - len(art)) + art for art in ascii_lines]
    result = ["".join(row) for row in zip(*ascii_lines)]

    return "\n".join(result)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASCII_JSON_FILE = os.path.join(BASE_DIR, "ascii_letters.json")
ASCII_ART_FILE = os.path.join(BASE_DIR, "standard.txt")

ascii_letters = get_ascii_letter(ASCII_JSON_FILE)

print(get_ascii_word(ASCII_ART_FILE, ascii_letters, "Python is number one"))