import random
import string

from .models import ShortURL

# Base62 alphabet: a-z, A-Z, 0-9
ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits  # 62 chars
KEY_LENGTH = 6


def generate_short_key():

    while True:
        key = "".join(random.choices(ALPHABET, k=KEY_LENGTH))
        if not ShortURL.objects.filter(short_key=key).exists():
            return key