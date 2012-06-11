# -*- coding: utf-8 -*-

import random

import env
import dynamo

from flask import Flask


app = Flask(__name__)



denv = env.prefix('dynamo_')
table = dynamo.table(denv['table'], (denv['secret_key'], denv['secret_access_key']))

set_one = [
    'chaos', 'tasty', 'fruity', 'nice', 'swell', 'flying', 'loud', 'wet',
    'bitter', 'good', 'sweet', 'friendly', 'sad', 'flat', 'sharp', 'bright'
]

set_two = [
    'monkey', 'penguin', 'pizza', 'taco', 'fajita', 'synthesizer', 'iphone',
    'beer', 'wine', 'apple', 'chip', 'book', 'kindle', 'lens', 'camera', 'dog',
    'puppy', 'bunny', 'speaker', 'car'
]


def generate_slug():
    a = random.choice(set_one)
    b = random.choice(set_two)
    c = random.randint(0,1000)

    return '{0}-{1}-{2}'.format(a, b, c)


def fresh_slug():
    slug = generate_slug()

    if slug not in table:
        table[slug] = {}
        return slug

    # Recursion.
    return fresh_slug()



@app.route('/')
def slug():
    return fresh_slug()