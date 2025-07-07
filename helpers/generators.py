import random
import string


def generate_random_string(length: int, digits: bool = False) -> str:
    chars = string.ascii_letters
    if digits:
        chars += string.digits
    return ''.join(random.choice(chars) for _ in range(length))

name = f"User {generate_random_string(5)}{random.randint(100, 999)}"
email = f"user{random.randint(100, 999)}@gmail.ru"
password = f"UniquePassword{random.randint(100, 999)}"