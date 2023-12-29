import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*(),./<>?;:'[]-_=+"

upper, lower, nums, syms = True, True, True, False

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 5 # Adjust the number of characters in the password
amount = 1  # Adjust the number of passwords to generate

with open("generated_passwords.txt", "w") as file:
    for x in range(amount):
        password = "".join(random.sample(all, length))
        file.write(password + "\n")
        print(password)