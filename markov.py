#!/usr/bin/env python

from sys import argv

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
    
    print markov_chains




    





    return markov_chains

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

def main():

    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename).read()
    make_chains(input_text)


    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
#    print random_text

# if __name__ == "__main__":
#     main()
main()