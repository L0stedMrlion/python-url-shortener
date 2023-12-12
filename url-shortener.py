import string
import random

url_database = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

def shorten_url(long_url):
    if long_url:
        short_code = generate_short_code()
        short_url = f'http://yourdomain.com/{short_code}'
        url_database[short_code] = long_url
        return short_url
    else:
        return 'Please provide a valid URL.'

# Příklad použití:
long_url_to_shorten = 'https://www.example.com'
shortened_url = shorten_url(long_url_to_shorten)
print(f'Shortened URL: {shortened_url}')
