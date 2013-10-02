from markov import *
from sys import argv
import twitter


def post_tweet(api, random_text):

    tweet = api.PostUpdate(random_text)
    return tweet

def main():

    script, filename = argv

    api = twitter.Api(consumer_key='consumer_key',
consumer_secret='consumer_secret', access_token_key='access_token', access_token_secret='access_token_secret')


    input_text = open(filename).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    post_tweet(api, random_text)

if __name__ == "__main__":
    main()
