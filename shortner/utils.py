import random
import string

from .models import ShortURL
import qrcode
import io
import base64
# Base62 alphabet: a-z, A-Z, 0-9
ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits  # 62 chars
KEY_LENGTH = 6


def generate_short_key():

    while True:
        key = "".join(random.choices(ALPHABET, k=KEY_LENGTH))
        if not ShortURL.objects.filter(short_key=key).exists():
            return key
        


def generate_qr_code(url):
    qr = qrcode.make(url)
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str