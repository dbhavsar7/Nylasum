import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import *
from keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import warnings
from nltk.corpus import stopwords
import numpy as np
import pandas as pd 
import re
from sklearn.model_selection import train_test_split as tts
from bs4 import BeautifulSoup
from attention import AttentionLayer

# gpus = tf.config.experimental.list_physical_devices('GPU')
# for gpu in gpus: 
#     tf.config.experimental.set_memory_growth(gpu, True)

# def text_cleaner(text, num):
#     """
#     This function cleans a text by removing everything :)
#     """
#     # define new string 
#     newString = text.lower()
#     newString = BeautifulSoup(newString, "lxml").text
#     newString = re.sub(r'\([^)]*\)', '', newString)
#     newString = re.sub('"','', newString)
#     newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])    
#     newString = re.sub(r"'s\b","",newString)
#     newString = re.sub("[^a-zA-Z]", " ", newString) 
#     newString = re.sub('[m]{2,}', 'mm', newString)

#     # Clean texts with number 0
#     if num == 0:
#         tokens = [w for w in newString.split() if not w in stop_words]

#     # Clean Summaries with number 1
#     else:
#         tokens=newString.split()
    
#     long_words = []
#     for i in tokens:
#         if len(i) > 1:
#             long_words.append(i)   
#     return (" ".join(long_words)).strip()
