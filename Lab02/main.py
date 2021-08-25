import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz


def preprocess(df):
    label_encoder = LabelEncoder()
    for column in df.columns:
        df[column] = label_encoder.fit_transform(df[column])


# Preprocessing data for training sets and tests sets.
def split(df, test_rates):
    feature = np.array(df[df.columns[1:]])
    label = np.array(df[df.columns[0]])

    # Split data.
    feature_train_list, feature_test_list, label_train_list, label_test_list = [], [], [], []
    for rate in test_rates:
        feature_train, feature_test, label_train, label_test = train_test_split(feature, label, test_size=rate)
        feature_train_list.append(feature_train)
        feature_test_list.append(feature_test)
        label_train_list.append(label_train)
        label_test_list.append(label_test)

    return feature_train_list, feature_test_list, label_train_list, label_test_list


# Building the decision tree classifier.
def building_clf(feature_train, label_train, feature_names, label_name, filename, directory, file_format):
    # Create DecisionTreeClassifier object.
    clf = DecisionTreeClassifier()
    clf = clf.fit(feature_train, label_train)

    # Export and draw graph.
    dot_data = export_graphviz(clf, feature_names=feature_names, class_names=label_name, filled=True, rounded=True, special_characters=True)
    graph = graphviz.Source(dot_data, filename=filename, directory=directory, format=file_format, engine='dot')
    graph.save()  # Save source code to gv file.
    graph.view()  # Draw graph and save to file with `file_format` file extension.


def building_all_clf(feature_train_list, label_train_list, directory=None, file_format='png'):
    filename_list = ['clf-40-60.gv', 'clf-60-40.gv', 'clf-80-20.gv', 'clf-90-10.gv']  # Filename corresponding to train/test rates.
    feature_names = list(df.columns[1:])  # List of features' name.
    label_name = df.columns[0]  # Target attribute name.

    # Building the decision tree classifiers.
    for i in range(len(test_rates)):
        building_clf(feature_train_list[i], label_train_list[i], feature_names, label_name, filename_list[i], directory, file_format)


# main function.
def main():
    # Read data from csv file.
    df = pd.read_csv('/Users/lehoanganh/Desktop/HoangAnh/SecondYear/ThirdSemester/Intro2AI/Intro2AI-HCMUS/Lab02/mushrooms.csv')

    # Encode data.
    preprocess(df)

    # Proportions (train/test): 40/60 - 60/40 - 80/20 - 90/10.
    test_rates = [0.6, 0.4, 0.2, 0.1]

    # Split into training and test sets.
    feature_train_list, feature_test_list, label_train_list, label_test_list = split(df, test_rates)

    # Building the decision tree classifiers.
    building_all_clf(feature_train_list, label_train_list, directory)


# Call main function.
main()
