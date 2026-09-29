import secrets
import string

ALPHABET = string.ascii_letters + string.digits
LENGTH = 8

def generate_password():
    return ''.join(secrets.choice(ALPHABET) for _ in range(LENGTH))

if __name__ == '__main__':
    for i in range(5):
        print(i + 1, generate_password())