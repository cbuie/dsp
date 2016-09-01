#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
import re
import random


fin = 'python/Republic'


def word_list(fin): #scrub text file input and create word list, eliminate special characters and numbers
    word_list = []
    with open(fin,'r') as fit:
        for line in fit:
            for word in line.split():
                if re.sub('\W+','', word).lower().isdigit():
                    pass
                else:
                    word_list.append(re.sub('\W+','', word).lower())
    return word_list


def word_dict(words):
    d = {}
    for i, word in enumerate(words):
        try:
            w1, w2, w3 = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (w1, w2)
        if key not in d:
            d[key] = []
        #
        d[key].append(w3)

    return d


def fab_key (x0): #fabricate a new key
    x1 = x0[0][1]
    x2 = x0[1]
    x3 = x1,x2
    return  x3


words = word_list(fin) #list of words from file
dow = word_dict(words) #dictionary from words


sentence = []
randomKey = random.choice(dow.keys())
count = 0
while (count < 5):
    try:
        current_state = randomKey, random.choice(dow[randomKey])
        for i in range(len(current_state)): sentence.append(current_state[0][i])
        sentence.append(current_state[1])
    except:
        print 'fail'
        pass
    count =+1


    while (count < 5):
        try:
            sentence.append(random.choice(dow[fab_key(current_state)]))
            print count
            count = count + 1
        except:
            print 'fail'
            break
count = count + 1
print sentence




print fab_key(current_state)
print dow[fab_key(randomKey)]

# li = [key for key in d.keys() if key[0][0].isupper()]
# key = choice(li)
#
# li = []
# first, second = key
# li.append(first)
# li.append(second)
# while True:
#     try:
#         third = choice(d[key])
#     except KeyError:
#         break
#     li.append(third)
#     if third[-1] in EOS:
#         break
#     # else
#     key = (second, third)
#     first, second = key
#
# return ' '.join(li)

