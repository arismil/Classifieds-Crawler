import re

import pandas
from sklearn.feature_extraction.text import CountVectorizer

# nltk.download('stopwords')
# nltk.download('wordnet')

# load the dataset
dataset = pandas.read_csv('iphone.csv')
dataset.head()

# words to remove from dataset
noise_words = ["iphone", "apple", "i", "phone"]
stop_words = set(noise_words)
corpus = []
# get price
dataset['price_normalized'] = dataset['price'].apply(lambda x: str(x).split(",")[0])
# measure word count
dataset['word_count'] = dataset['name'].apply(lambda x: len(str(x).split(" ")))
# word frequency tables
frequent_words = pandas.Series(' '.join(dataset['name']).split()).value_counts()[:20]
rare = pandas.Series(' '.join(dataset['name']).split()).value_counts()[-20:]

for i in range(len(dataset)):
    # Remove punctuations
    text = dataset['name'][i]

    # Convert to lowercase
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # remove special characters and digits
    text = re.sub("[^a-z0-9]+", " ", text)

    # Convert to list from string
    text = text.split()
    line = []
    # Stemming
    for word in text:
        if not word in stop_words:
            line.append(word)
    text = line

    text = " ".join(text)
    corpus.append(text)

cv = CountVectorizer(max_df=0.7, stop_words=stop_words, max_features=10000, ngram_range=(1, 1))
X = cv.fit_transform(corpus)
print(list(cv.vocabulary_.keys())[:10])
