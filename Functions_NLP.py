#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the Python libraries
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os
import sys

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


# We will define a a function to map the amount and % of missing values for the different variables
def show_null(df):
    null_columns = ((df.isnull().sum(axis = 0)/len(df)).sort_values(ascending=False)*100).index
    null_data = pd.concat([df.isnull().sum(axis = 0),
                           ((df.isnull().sum(axis = 0)/len(df)).sort_values(ascending=False)*100),
                           df.loc[:, df.columns.isin(list(null_columns))].dtypes]
                          , axis=1, sort= 'True')
    null_data = null_data.rename(columns={0: 'Amount', 
                                          1: 'Missing data (%)', 
                                          2: 'type'}).sort_values(ascending=False, by = 'Missing data (%)')
    null_data = null_data[null_data["Amount"]!=0]
    return null_data

pd.set_option('display.max_rows', None) # I want to show all the results


# In[ ]:


# Download text processing libraries and create dictionaries
import re
import string
import nltk
from nltk.corpus import stopwords

# Function to preprocess our text data
def clean_text(text):
    import re
    ', '.join(text)
    # Step 1. Drop special characters and keep just the alpha
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text) #remove all except A-Z, a-z, 0-9   
    ', '.join(text)
    #Step 2. Transform them into lower case
    text = text.lower().split()

    #Step 3. Delete stop words
    from nltk.corpus import stopwords
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]    
    text = " ".join(text)
    return(text)

def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ' '.join(list_of_text)
    return combined_text

