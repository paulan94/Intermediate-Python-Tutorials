from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(str(ascii_lower) for _ in range(3)))
    url = ''.join(['http://', starting, '.com'])
    return url

url = random_starting_url()
print url
