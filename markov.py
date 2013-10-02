#!/usr/bin/env python

from sys import argv
from random import choice


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # text_list is the original text, in order, seperated into a list by word
    text_list = corpus.replace("\"", '').replace("_", '').split()
    markov_chains = {}

    for i in range(0, len(text_list) - 2):
        tuple_key = (text_list[i], text_list[i + 1])
        value = text_list[i + 2]

        if tuple_key not in markov_chains:
            markov_chains[tuple_key] = [value]
        else:
            markov_chains[tuple_key].append(value)
    
    return markov_chains


def acceptable_beginning(string):
    # returns True if acceptable
    return ord(string[0]) in range(ord('A'), ord("Z") + 1)


def acceptable_ending(string):
    # returns True if acceptable
    return string[-1] in ".?!"


def make_sentence(chains):
    """Takes a dictionary of markov chains and returns a random sentence
    based off an original text."""

    #random start is a tuple key
    random_start = choice(chains.keys())
    
    while not acceptable_beginning(random_start[0]):
        random_start = choice(chains.keys())
    
    # list of words
    word_list = [random_start[0], random_start[1]]

    while not acceptable_ending(word_list[-1]):
        next_word = choice(chains[(word_list[-2], word_list[-1])])
        word_list.append(next_word)
    
    sentence = " ".join(word_list)

    return sentence

        
def make_text(chains):
    """Returns text in complete sentences based on original text"""

    #length of desired output text in characters
    length = 140
    tweet = make_sentence(chains)

    while len(tweet) > length:
        tweet = make_sentence(chains)

    if len(tweet) < length/3:
        next_sentence = make_sentence(chains)
        while len(tweet) + len(next_sentence) + 1 > length:
            next_sentence = make_sentence(chains)
        tweet += " " + next_sentence

    
    return tweet

def main():

    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename).read()
 
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()