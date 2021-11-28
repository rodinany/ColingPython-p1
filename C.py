import pymorphy2
from itertools import product
import random

def generator(arr1, arr2):
    while True:
        i = random.choice(tuple(product(arr1, arr2, repeat=1)))
        n = morph.parse(i[0])[0]
        k = morph.parse(i[1])[0]
        if n.tag.gender == k.tag.gender and n.tag.case == k.tag.case == 'nomn':
            yield i
        else:
            continue

morph = pymorphy2.MorphAnalyzer()

nouns = []
adjectives = []

with open('rus_shuffled.txt', 'r', encoding="utf-8") as f:
    for word in f:
        word = word.strip('\n')
        p = morph.parse(word)[0]
        if p.tag.POS == 'NOUN':
            nouns.append(word)
        elif p.tag.POS == 'ADJF':
            adjectives.append(word)

print(next(generator(nouns, adjectives)))
print(next(generator(nouns, adjectives)))
print(next(generator(nouns, adjectives)))
print(next(generator(nouns, adjectives)))
print(next(generator(nouns, adjectives)))
print(next(generator(nouns, adjectives)))
