import os
import tweepy
from dotenv import load_dotenv
import random
import markovify
from datetime import datetime

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Load keys from .env
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


def mousers_tweet(sentence):
    '''Authenticates user and tweets the sentence generated'''
    #Authenticate to twitter with keys
    auth=tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    #Twitter api object
    tweepy_api = tweepy.API(auth)

    #Authentication check
    try:
        tweepy_api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    tweepy_api.update_status(sentence)

def generate_random_sentence(text):
    ''' Use markovify to generate a random sentence of 140 characters
        from the sentences on cat-text.txt. Generates 200 sentences and outputs one random sentence from the list.'''
    random.seed(datetime.now())
    text_model = markovify.Text(text, state_size=2)
    pos_sentences = []
    #Generate a list of 200 generated sentences, limited to 140 characters
    #Trying to do this to 
    for _ in range(200):
        pos_sentences.append( text_model.make_short_sentence(140,tries=100) )
    

    rand = random.randint(0,199)

    #output a random sentence from the list.
    return pos_sentences[rand]


if __name__ == '__main__':
    with open("cat-text.txt", encoding="utf-8") as f:
        text = f.read()
    # Build the model.
    sentence = generate_random_sentence(text)
    print(sentence)
    mousers_tweet(sentence)

    


