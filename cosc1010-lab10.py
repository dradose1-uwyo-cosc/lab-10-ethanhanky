# Ethan Hankel
# UWYO COSC 1010
# Submission Date: 11/19/24
# Lab 10
# Lab Section: 07
# Sources, people worked with, help given to: 
# I used the recent powerpoints
# Chat GPT

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.



def crack_password():
    try:
        with open("hash", "r") as hash_file:
            target_hash = hash_file.read().strip() 
    except FileNotFoundError:
        print("Error: 'hash' no file found.")
        return
    except Exception as e:
        print(f"Error reading 'hash' file: {e}")
        return

    try:
        with open("rockyou.txt", "r", encoding="utf-8") as password_file:
            passwords = password_file.readlines()
    except FileNotFoundError:
        print("Error: 'rockyou.txt' no file found.")
        return
    except Exception as e:
        print(f"Error reading 'rockyou.txt': {e}")
        return
    else:
        print("Loading")



    for password in passwords:
        password = password.strip()  
        hashed_password = get_hash(password)

        if hashed_password == target_hash:
            print(f"The password is: {password}")
            break
    else:
        print("Password not found in the provided list.")

if __name__ == "__main__":
    crack_password()
