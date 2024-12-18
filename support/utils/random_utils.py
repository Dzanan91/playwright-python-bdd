import random
import string

def generate_random_string(length: int) -> str:
    """Generate a random string of given length with letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
