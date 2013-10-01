#!/usr/bin/env python

from sys import argv
from random import randint, choice

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # text_list is the original text, in order, seperated into a list by word
    text_list = corpus.split()
    markov_chains = {}

    for i in range(0, len(text_list) - 2):
        tuple_key = (text_list[i], text_list[i + 1])
        value = text_list[i + 2]

        if tuple_key not in markov_chains:
            markov_chains[tuple_key] = [value]
        else:
            markov_chains[tuple_key].append(value)
    
    return markov_chains


def acceptable_beginning (string):
    # returns True if acceptable
    word = string.strip("\"")
    return ord(word[0]) in range(ord('A'), ord("Z") + 1)
    
        
def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    #length of output text in characters
    length = 140

    #random start is a tuple key
    random_start = choice(chains.keys())
    
    while not acceptable_beginning(random_start[0]):
        random_start = choice(chains.keys())
    
    # list of words
    tweet_list = [random_start[0], random_start[1]]

    tweet = ''
    
    # makes are random text
    while len(tweet) < length:
        next_word = choice(chains[(tweet_list[-2], tweet_list[-1])])
        
        # the one is for the final space 
        if len(next_word) + len(tweet) + 1 >= length:
            break
        else:
            tweet_list.append(next_word) 
            tweet = " ".join(tweet_list)

    return tweet







    return "Here's some random text."

def main():

    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

# if __name__ == "__main__":
#     main()
main()