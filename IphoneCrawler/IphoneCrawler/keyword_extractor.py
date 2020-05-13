import re
import math
import statistics
import numpy as np
import scipy.stats
import pandas


def model_extractor(name):
    model = re.match(r"\b(6s?|7|8|x(s|r)?|11)", name)
    if model:
        return model.group(0)
    else:
        return None


def size_extractor(name):
    pro = re.search(r"pro", name)
    if pro:
        model = 2  # pro model
        if re.search(r"max", name):
            model = 3
            return model  # return pro max model
        return model  # return pro model
    else:
        if re.search(r"plus", name):
            return 1  # return plus model
        return 0  # return base model


# words to remove from Dataset
noise_words = ["iphone", "apple", "i", "phone"]
stop_words = set(noise_words)

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
    Dataset['name'][i] = text

Dataset['model'] = Dataset['name'].apply(lambda x: model_extractor(str(x)))
Dataset['plus_size'] = Dataset['name'].apply(lambda x: size_extractor(x))

Dataset = Dataset.replace(to_replace='None', value=np.nan).dropna()
Dataset['price'] = Dataset['price'].astype(int)

# Get names of indexes for which column Age has value 30
indexPrice = Dataset[Dataset['price'] == 1].index

# Delete these row indexes from dataFrame
Dataset.drop(indexPrice, inplace=True)
print(Dataset.loc[(Dataset['model'] == '7') & (Dataset['plus_size'] == 1)].describe())


Dataset.to_excel('output.xlsx')
