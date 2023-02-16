# AffinityAnswers-Data_Engineering_Internship_Problem
## Introduction
This code is a program written in Python that analyzes Twitter tweets for profanity by detecting racial slurs in the tweets. The program takes as input a file containing a list of words indicating racial slurs and a file containing the tweets to be analyzed. The output of the program is the degree of profanity for each sentence in the file. The program is modularized into several methods for better organization and readability.

## Assumptions
- The input files are in CSV format.
- The list of racial slurs is provided in a CSV file with one slur per row.
- The tweets to be analyzed are provided in a CSV file with a "tweet" column containing the text of each tweet.
- The degree of profanity is determined based on the number of racial slurs detected in each tweet.
- The degree of profanity is classified as "Not profane", "Mildly profane", "Moderately profane", or "Highly profane" depending on the number of racial   slurs detected in the tweet.
- The program assumes that the input files are not too large to fit into memory.

## Data Structures
The program reads the input files into pandas dataframes. The dataframe for the racial slurs contains a single column of slur strings. The dataframe for the tweets contains a single column of tweet text.

## Decorators
This code does not use decorators.

## Modularization
The code is modularized into the following methods:

- __init__(self, slurs_loc, tweets_loc): This method initializes the class with the file locations for the racial slurs and tweets.
- preprocess_racial_slur(self,racial_slurs): This method preprocesses the list of racial slurs by converting all slur strings to lowercase.
- preprocess_tweets(self,tweets): This method preprocesses the tweets by removing all non-alphabetic characters and converting all text to lowercase.
- get_profanity_degree(self,sentence, racial_slurs): This method determines the degree of profanity of a given tweet sentence based on the number of racial slurs detected in the sentence.
- analysis_all_tweets(self): This method runs the analysis for all tweets and outputs the degree of profanity for each tweet sentence.
Example Usage
makefile
Copy code
# Initialize object with file locations
obj1 = tweets_sentiment_analysis("slurs.csv", "tweets.csv")

# Analyze all tweets and output degree of profanity for each sentence
obj1.analysis_all_tweets()
Conclusion
This program provides a simple yet effective way to analyze Twitter tweets for profanity by detecting racial slurs in the text. By using pandas dataframes, the program is able to efficiently process large volumes of data. The code can be easily extended to include other types of profanity detection by modifying the get_profanity_degree method.
