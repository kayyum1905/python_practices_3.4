import random


#length of the password string
char = random.randint(8, 12)
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
punctuations = ('!', '+', '&', '?', '_', '#', '-', '*', '.')


def generate_password():
    total = 0
    password = ''
    while total < char:
        pick = random.randint(1, 5)  # 1: choose letter, 2: choose number and 3: choose punctuation
        if pick == 1 or pick == 2:
            case = random.randint(0, 1)
            # normal in lower case
            if case == 0:
                password += random.choice(letters)
            # then change the character to uppercase
            elif case == 1:
                password += random.choice(letters).upper()
        elif pick == 3 or pick == 4:
            password += str(random.choice(numbers))
        elif pick == 5:
            password += random.choice(punctuations)
        total += 1
    else:
        print(password)


generate_password()
