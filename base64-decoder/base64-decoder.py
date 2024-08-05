# A simple base64 decoder using base64 library

import base64

encoded_text = 'UUc3NUhZVDg='  # use type in your encoded text

decoded_byte = base64.b64decode(encoded_text)

decoded_text = decoded_byte.decode('utf-8')

print(decoded_text)
