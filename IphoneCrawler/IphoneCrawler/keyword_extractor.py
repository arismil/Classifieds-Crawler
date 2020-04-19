import csv
from collections import Counter
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
#nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
import math

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

# csv file name
filename = "iphone.csv"

# initializing the titles and rows list
fields = []
rows = []
iphones = []
prices = []
# reading csv file
with open(filename, 'r', encoding="utf8") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        iphones.append(row[0])
        prices.append(row[1])

    # get total number of rows
    print("Total no. of rows: %d" % csvreader.line_num)

# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
#
# #  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in iphones[:5]:
#     # parsing each column of a row
#     print(row)
#     print('\n')
for line in range(len(iphones)):
    iphones[line] = iphones[line].lower()
    iphones[line] = iphones[line].split()
    print(iphones[line])