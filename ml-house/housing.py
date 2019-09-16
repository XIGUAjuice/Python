#%%
import os
import tarfile
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/raw/master/"
HOUSING_PATH = "datasets/housing/"
SAVE_PATH = r".\datasets\housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "housing.tgz"


def fetch_housing_data(download_url=HOUSING_URL, save_path=SAVE_PATH):
    if not os.isdir(save_path):
        os.mkdir(save_path)

    tgz_path = save_path + "housing.tgz"
    urllib.request.urlretrieve(download_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=save_path)
    housing_tgz.close()


def load_data(path=SAVE_PATH):
    csv_path = os.path.join(path, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_data()

housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5, inplace=True)
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    train_set = housing.loc[train_index]
    test_set = housing.loc[test_index]

for set in (train_set, test_set):
    set.drop(["income_cat"], axis=1, inplace=True)

housing = train_set.copy()
imputer = Imputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis=1)
X = imputer.fit_transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns)

encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encodeded = encoder.fit_transform(housing_cat)
#%%
