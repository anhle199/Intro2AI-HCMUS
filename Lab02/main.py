import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


# Preprocessing data for training sets and tests sets.
def preprocess_data(df, test_proportions):
    feature = np.array(df[df.columns[1:]])
    label = np.array(df[df.columns[0]])

    feature_train_list, label_train_list, feature_test_list, label_test_list = [], [], [], []
    for proportion in test_proportions:
        feature_train, label_train, feature_test, label_test = train_test_split(feature, label, test_size=proportion)
        feature_train_list.push(feature_train)
        label_train_list.push(label_train)
        feature_test_list.push(feature_test)
        label_test_list.push(label_test)

    return feature_train_list, label_train_list, feature_test_list, label_test_list


def main():
    df = pd.read_csv('/Users/lehoanganh/Desktop/HoangAnh/SecondYear/ThirdSemester/Intro2AI/Intro2AI-HCMUS/Lab02/mushrooms.csv')

    # Proportions (train/test): 40/60 - 60/40 - 80/20 - 90/10.
    test_proportions = [0.6, 0.4, 0.2, 0.1]

    feature_train_list, label_train_list, feature_test_list, label_test_list = preprocess_data(df, test_proportions)
    