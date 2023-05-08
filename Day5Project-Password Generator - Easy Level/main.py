import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['<', '>', '?', '/', '|', '+', '=', ')', '(', '&', '%', '$', '#', '@', '!', '^', '*']

num_letters = int(input("How many letters you do want in your password? \n"))
num_numbers = int(input("How many numbers you do want in your password? \n"))
num_symbols = int(input("How many symbols do you want in your password? \n"))

password = ""
for char in range(1, num_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

for char in range(1, num_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers

for char in range(1, num_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols
print(password)

