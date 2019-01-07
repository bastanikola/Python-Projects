--------------------------------------------------------------
### PROJECT: AMAZON ALEXA REVIEW ANALYSIS ###
--------------------------------------------------------------
'''
    -Dataset consists of 3000 Amazon customers, reviews,
     star ratings, date of review, variant and feedback of
     various amazon Alexa products like Alexa Echo, Echo dots.
    -The objective is to discover insights into customers reviews
     and perform sentiment analysis on the data
    -Dataset: www.kaggle.com/sid321axn/amazon-alexa-reviews
'''
-------------------------------
### IMPORTING THE LIBRARIES ###
-------------------------------
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

--------------------------
### IMPORTING THE DATA ###
--------------------------
df_alexa = pd.read_csv('amazon_alexa.tsv', sep = '\t')

df_alexa.head()
df_alexa.tail()
df_alexa.keys()
df_alexa["verified_reviews"]
df_alexa.info()
df_alexa.describe()

--------------------------
### DATA VISUALIZATION ###
--------------------------
positive = df_alexa[ df_alexa['feedback'] == 1]
negative = df_alexa[ df_alexa['feedback'] == 0]

positive
negative

sns.countplot(df_alexa['feedback'], label = 'Count')

sns.countplot(df_alexa['rating'], label = 'Count')
#or
sns.countplot(x = 'rating', data = df_alexa)

df_alexa['rating'].hist(bins = 5)

plt.figure(figsize = (40,15))
sns.barplot(x = 'variation', y = 'rating', data = df_alexa, palette = 'deep')

------------------
### WORD CLOUD ###
------------------
from wordcloud import WordCloud

#df_alexa['verified_reviews']
words = df_alexa['verified_reviews'].tolist()
#len(words)
words_as_one_string = ' '.join(words)
#len(words_as_one_string)

plt.figure(figsize = (20, 30))
plt.imshow(WordCloud().generate(words_as_one_string))

---------------------------------------------
### DATA CLEANING AND FEATURE ENGINEERING ###
---------------------------------------------
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
alexa_countvectorizer = vectorizer.fit_transform(df_alexa['verified_reviews'])
alexa_countvectorizer.shape

word_count_array = alexa_countvectorizer.toarray()
plt.plot(word_count_array[1,:])
df_alexa['verified_reviews'][1]

df_alexa['length'] = df_alexa['verified_reviews'].apply(len)
df_alexa.head()
df_alexa['length'].hist(bins = 100)

min_char = df_alexa['length'].min()
df_alexa [ df_alexa['length'] == min_char ] ['verified_reviews'].iloc[0]

max_char = df_alexa['length'].max()
df_alexa [ df_alexa['length'] == max_char ] ['verified_reviews'].iloc[0]

df_alexa [ df_alexa['length'] == 100 ] ['verified_reviews'].iloc[0]
