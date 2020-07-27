#!/usr/bin/env python
# coding: utf-8

# import libraries here; add more as necessary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import warnings
import requests
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_hub as  hub
import tensorflow_datasets as tfds
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.tree  import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import fbeta_score,accuracy_score
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import fbeta_score, make_scorer
from collections import OrderedDict
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from flask import Flask, request, jsonify, render_template
warnings.filterwarnings('ignore')

def load_models():
    model = tf.keras.models.load_model('german_credit.h5')
    return model

def get_predictions():
    X_test = request.get_json(force=True)
    X_test_new = pd.DataFrame(X_test) 
    X_test_new = X_test_new.astype(float)
    model = load_models()
    prediction = model.predict(X_test_new)
    return prediction

