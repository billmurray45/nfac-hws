import argparse
from ascii_art import get_ascii_word

parser = argparse.ArgumentParser()
parser.add_argument("message", help="Message for input")
args = parser.parse_args()

result = get_ascii_word("standard.txt", args.message)

print(result)