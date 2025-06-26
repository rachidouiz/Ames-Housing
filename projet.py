import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
# Chargement du dataset
df = pd.read_csv('AmesHousing.csv')

# Aperçu des données
df.head()
df.info()
df.describe()
