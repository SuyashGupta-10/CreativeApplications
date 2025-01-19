import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

number_no = random.randint(0,len(numbers) - 1)
symbol_no = random.randint(0, len(symbols) - 1)
letter_no = random.randint(0, len(letters) - 1)

""" password = ""
for x in range(0, nr_letters):
  letter_no = random.randint(0, len(letters) - 1)
  password += letters[letter_no]
for y in range(0, nr_symbols):
  symbol_no = random.randint(0, len(symbols) - 1)
  password += symbols[symbol_no]
for z in range(0, nr_numbers):
  number_no = random.randint(0, len(numbers) - 1)
  password += numbers[number_no]"""

password_list = []
for x in range(0, nr_letters):
  letter_no = random.randint(0, len(letters) - 1)
  password_list.append(letters[letter_no])
for y in range(0, nr_symbols):
  symbol_no = random.randint(0, len(symbols) - 1)
  password_list.append(symbols[symbol_no])
for z in range(0, nr_numbers):
  number_no = random.randint(0, len(numbers) - 1)
  password_list.append(numbers[number_no])

random.shuffle(password_list)

password = ''
for char in password_list:
  password += char

print(f"Your password is {password}")
input()