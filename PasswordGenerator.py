import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to The Pypassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
pass_length = nr_symbols + nr_letters + nr_numbers

pass_array = []

i = 1
while i in range(1, nr_letters +1):
    pass_array.append(letters[random.randint(0, len(letters)-1)])
    i += 1

j = 1
while j in range(1, nr_symbols +1):
    pass_array.append(symbols[random.randint(0, len(symbols)-1)])
    j += 1

k = 1
while k in range(1, nr_numbers +1):
    pass_array.append(numbers[random.randint(0, len(numbers)-1)])
    k += 1


random.shuffle(pass_array)

password = ''
for x in pass_array:
    password += x

# password = "".join(final_array)
print(f"Your password is {password}")




