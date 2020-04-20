import re

import pandas

# load the dataset
dataset = pandas.read_csv('iphone.csv')
dataset.head()

# words to remove from dataset
noise_words = ["iphone", "με", "apple"]
stop_words = set(noise_words)

# get price
dataset['price_normalized'] = dataset['price'].apply(lambda x: str(x).split(",")[0])
# measure word count
dataset['word_count'] = dataset['name'].apply(lambda x: len(str(x).split(" ")))
# word frequency tables
frequent_words = pandas.Series(' '.join(dataset['name']).split()).value_counts()[:20]
rare = pandas.Series(' '.join(dataset['name']).split()).value_counts()[-20:]

for i in range(0, 109):
    # Remove punctuations
    text = re.sub('[^a-zA-Z]', ' ', dataset['name'][i])

    # Convert to lowercase
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)
    print(text)
    ##Convert to list from string
    text = text.split()
