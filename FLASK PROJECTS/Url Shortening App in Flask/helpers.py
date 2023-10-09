import string
import random
import re

def random_string_generator(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=N))
    return str(res)

def random_string_generator_only_alpha(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.ascii_uppercase, k=N))
    return str(res)


def is_valid_url(url):
    # Define a regular expression pattern to match URLs
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Match the scheme (http, https, or ftp)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # Match domain
        r'localhost|'  # Match "localhost"
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Match IP address
        r'(?::\d+)?'  # Match optional port number
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(url_pattern.match(url))