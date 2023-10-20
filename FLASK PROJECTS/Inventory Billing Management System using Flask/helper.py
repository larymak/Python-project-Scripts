import string, random

def random_id(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.ascii_uppercase, k=N))
    return res

def handle_catch(caller, on_exception):
    try:
         return caller()
    except:
         return on_exception