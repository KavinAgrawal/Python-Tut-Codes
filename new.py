import pandas as pd
import numpy as np
import re
import collections as collections
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords

col_names=['Text', 'Sentiment'] 
data = pd.read_csv("Round1_Problem1-of-2_Dataset_amazon_cells_labelled.txt",sep="\n",delimiter="\t",names=col_names)

vocabs=[]
for i in range(data.shape[0]):
    print(data['Text'][i])
    
    #removing website links
    data['Text'][i]=re.sub(r"www.\S+.com", "", data['Text'][i])
    print(data['Text'][i])
    
    #removing punctuations
    #data['Text'][i]=re.sub(r"`~@#$%^&*()_+{}|:\"<>?/*-+-=\\\;\'/", "", data['Text'][i])
    #data['Text'][i]=re.sub(r".", ' . ', data['Text'][i])
    #data['Text'][i]=re.sub(r"!", ' ! ', data['Text'][i])
    #data['Text'][i]=re.sub(r",", ' , ', data['Text'][i])
    
    #removing stopwords
    data['Text'][i] = ' '.join([word for word in data['Text'][i].split() if word not in (stopwords.words('english'))])
    print(data['Text'][i]) 
    
    #lemmatizing
    data['Text'][i] = ' '.join([WordNetLemmatizer().lemmatize(word) for word in data['Text'][i].split()])
    print(data['Text'][i])
    
    #tokenizing
    token_data=[]
    for word in data['Text'][i].split():
        token_data.append(word)
        vocabs.append(word)
    data['Text'][i]=token_data
    print(data['Text'][i])
    #data['Text'][i]=word_tokenize(data['Text'][i]) 
    
    
data['Text'].as_matrix
print(data)
data['Text']
for row in data['Text']:
        print(row)

