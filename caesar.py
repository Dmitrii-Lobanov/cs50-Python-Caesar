import cs50
import sys

if len(sys.argv) != 2:
    print("Error! You should input only one integer!")
    exit(1)

key = int(sys.argv[1])

if key < 0:
    print("Please input positive number")
    exit(1)
else:
    plaintext = cs50.get_string("plaintext: ")
    print("ciphertext: ", end="")

    for c in plaintext:
        if c.islower():
            encr_char = chr(((ord(c) - 97 + key) % 26) + 97)
            print(encr_char, end="")
        elif c.isupper():
            encr_char = chr(((ord(c) - 65 + key) % 26) + 65)
            print(encr_char, end="")
        else:
            print(c, end="")
    print()
