import re
from pprint import pprint

import pandas
from tensorflow.keras.preprocessing.text import Tokenizer

# words to remove from Dataset
noise_words = ["iphone", "apple", "i", "phone"]
stop_words = set(noise_words)

corpus = []
# load the Dataset
Dataset = pandas.read_json('iphone.json')
# lower text
Dataset['name'] = Dataset['name'].apply(lambda x: x.lower())
# remove tags
Dataset['name'] = Dataset['name'].apply(lambda x: re.sub("&lt;/?.*?&gt;", " ", x))
# remove noise
Dataset['name'] = Dataset['name'].apply(lambda x: re.sub("[^a-z0-9]+", " ", x))
# remove decimal part
Dataset['price'] = Dataset['price'].apply(lambda x: re.sub(",.*", " ", str(x)))
# remove thousand point
Dataset['price'] = Dataset['price'].apply(lambda x: re.sub("\.", "", str(x)))
# text cleanup
for i in range(len(Dataset['name'])):
    text = Dataset['name'][i]
    text = text.split()
    text = [word for word in text if not word in stop_words]
    text = " ".join(text)
    corpus.append(text)
    Dataset['name'][i] = text

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(corpus)
word_index = tokenizer.word_index
print(word_index)
