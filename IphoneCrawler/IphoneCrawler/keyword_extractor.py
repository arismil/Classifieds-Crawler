import re

import numpy as np
import pandas
import locale
from sqlalchemy import create_engine

import pymysql


def model_extractor(name):
    model = re.match(r"\b(6s?|7|8|x([sr])?|11|12)", name)
    if model:
        return model.group(0)
    else:
        return None


def size_extractor(name):
    pro = re.search(r"\bpro\b", name)
    if pro:
        model = 2  # pro model
        if re.search(r"\bmax\b", name):
            model = 3
            return model  # return pro max model
        return model  # return pro model
    else:
        if re.search(r"\bplus\b", name):
            return 1  # return plus model
        return 0  # return base model


# words to remove from Dataset
noise_words = ["iphone", "apple", "i", "phone"]
stop_words = set(noise_words)

# load the Dataset
Dataset = pandas.read_csv('iphones.csv')
Dataset.to_excel('outputbefore.xlsx')
# lower text
Dataset['name'] = Dataset['name'].apply(lambda x: x.lower())
# remove tags
Dataset['name'] = Dataset['name'].apply(lambda x: re.sub("&lt;/?.*?&gt;", " ", x))
# remove noise
Dataset['name'] = Dataset['name'].apply(lambda x: re.sub("[^a-z0-9]+", " ", x))
# remove decimal part
Dataset['price'] = Dataset['price'].apply(lambda x: re.sub(",.*", " ", str(x)))
# remove any non digit
Dataset['price'] = Dataset['price'].apply(lambda x: re.sub("\D", "", str(x)))

# text cleanup
for i in range(len(Dataset['name'])):
    text = Dataset['name'][i]
    text = text.split()
    text = [word for word in text if not word in stop_words]
    text = " ".join(text)
    Dataset.loc[i, 'name'] = text

Dataset['model'] = Dataset['name'].apply(lambda x: model_extractor(str(x)))
Dataset['plus_size'] = Dataset['name'].apply(lambda x: size_extractor(x))


#DROP NONE VALUES
Dataset = Dataset.replace(to_replace='None', value=np.nan)
Dataset = Dataset.replace(to_replace='', value=np.nan)
# Dataset['price'] = Dataset['price'].astype(int)
# Dataset = Dataset[Dataset['price'] > 10]
locale.setlocale(locale.LC_ALL, 'el_gr')
Dataset['date'] = pandas.to_datetime(Dataset['date'], format='%d/%m/%Y %I:%M  %p')


sqlEngine = create_engine('mysql+pymysql://root:Q3DG$38p@127.0.0.1/eshop', pool_recycle=3600)

dbConnection = sqlEngine.connect()
Dataset.to_sql('classifieds', con=dbConnection, if_exists='replace', index_label='id')
dbConnection.close()
Dataset.to_excel('output.xlsx')
Dataset.to_csv('output.csv')
