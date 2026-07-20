import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(all_characters, k=12))


print("Your secure password is:", password)