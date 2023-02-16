import pandas as pd
import re

class tweets_sentiment_analysis:
    def __init__(self, slurs_loc, tweets_loc):
        # Load racial slurs and tweets from CSV files
        self.racial_slurs = pd.read_csv(slurs_loc, header=None)
        self.tweets = pd.read_csv(tweets_loc)
      
    def preprocess_racial_slur(self, racial_slurs):
        # Preprocess racial slurs to ensure they are all lowercase
        racial_slurs = [ele[0].lower() for ele in racial_slurs.values]
        return racial_slurs

    def preprocess_tweets(self, tweets):
        # Preprocess tweets by removing punctuation and converting to lowercase
        tweets = [re.sub(r'[^a-zA-Z\s]', '', ele.lower()) for ele in tweets['tweet']]
        return tweets

    def get_profanity_degree(self, sentence, racial_slurs):
        # Split sentence into words
        words = re.findall(r'\w+', sentence)
    
        # Count number of words that are in the set of racial slurs
        num_racial_slurs = sum(1 for word in words if word.lower() in racial_slurs)
    
        # Determine degree of profanity based on number of racial slurs
        if num_racial_slurs == 0:
            return 'Not profane'
        elif num_racial_slurs == 1:
            return 'Mildly profane'
        elif num_racial_slurs == 2:
            return 'Moderately profane'
        else:
            return 'Highly profane'
        
    def analysis_all_tweets(self):
        # Preprocess racial slurs and tweets
        racial_slurs = self.preprocess_racial_slur(self.racial_slurs)
        tweets = self.preprocess_tweets(self.tweets)
        
        # Analyze all tweets and print the degree of profanity for each one
        for tweet in tweets:
            profanity_degree = self.get_profanity_degree(tweet, racial_slurs)
            print(profanity_degree)

# Create instance of tweets_sentiment_analysis and analyze all tweets
obj1 = tweets_sentiment_analysis("slurs - Sheet 1.csv", "tweets.csv")
obj1.analysis_all_tweets()
