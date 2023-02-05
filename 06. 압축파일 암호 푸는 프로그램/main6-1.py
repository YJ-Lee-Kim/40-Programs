import itertools

password_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    to_attempt = itertools.product(password_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)