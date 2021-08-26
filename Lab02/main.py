import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt


# Encode each cell in dataframe.
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


def draw_graph(clf_list, feature_names, label_name, filenames, directory=None, file_extension='png'):
    for i in range(len(clf_list)):
        dot_data = export_graphviz(clf_list[i], feature_names=feature_names, class_names=label_name, filled=True, rounded=True, special_characters=True)
        graph = graphviz.Source(dot_data, filename=filenames[i], directory=directory, format=file_extension, engine='dot')
        # graph.save()  # Save source code to gv file.
        # graph.view()  # Draw graph and save to file with `png` file extension.
        graph.render()


# Building the decision tree classifiers.
def build_all_clf(test_rates, feature_train_list, label_train_list):
    clf_list = []
    for i in range(len(test_rates)):
        clf = DecisionTreeClassifier()
        clf = clf.fit(feature_train_list[i], label_train_list[i])
        clf_list.append(clf)

    return clf_list


# Evaluating the decision tree classifiers.
def evaluate_all_clf(clf_list, feature_test_list, label_test_list, filenames):
    rates_string = ['40/60', '60/40', '80/20', '90/10']

    for i in range(len(clf_list)):
        # Classification report.
        label_pred = clf_list[i].predict(feature_test_list[i])
        print("The Decision Tree Classifier Report (train/test - {})".format(rates_string[i]))
        print(classification_report(label_test_list[i], label_pred))
        print('')  # new line.

        # Confusion matrix.
        cfm = confusion_matrix(label_test_list[i], label_pred)
        plt.figure(i + 1)
        sns.heatmap(cfm, annot=True, linewidths=1, cbar=None)
        plt.title('The Decision Tree Classifier Confusion Matrix (train/test - {})'.format(rates_string[i]))
        plt.ylabel('Truth label')
        plt.xlabel('Predicted label')
        plt.savefig(fname=filenames[i])


# The depth and accuracy of a decision tree for a specific train/test rates.
def calc_accuracy_scores(max_depths, feature_train, label_train, feature_test, label_test):
    clf_list = []
    scores = []
    for i in range(len(max_depths)):
        clf = DecisionTreeClassifier(max_depth=max_depths[i])
        clf = clf.fit(feature_train, label_train)
        clf_list.append(clf)

        label_pred = clf.predict(feature_test)
        scores.append(accuracy_score(label_test, label_pred))

    return clf_list, scores


# main function.
def main():
    # Read data from csv file.
    df = pd.read_csv('mushrooms.csv')

    # Encode and fit data.
    preprocess(df)

    # Proportions (train/test): 40/60 - 60/40 - 80/20 - 90/10.
    test_rates = [0.6, 0.4, 0.2, 0.1]
    feature_names = list(df.columns[1:])
    label_name = df.columns[0]

    # Split into training and test sets.
    feature_train_list, feature_test_list, label_train_list, label_test_list = split(df, test_rates)

    # Building the decision tree classifiers.
    clf_list = build_all_clf(test_rates, feature_train_list, label_train_list)

    # Drawing the decision tree classifiers.
    # Export these graph to png file with the correspoding name (filenames_for_proportion).
    train_test_rates = ['40-60', '60-40', '80-20', '90-10']
    filenames_for_proportion = ['clf-{}.gv'.format(rate) for rate in train_test_rates]
    draw_graph(clf_list, feature_names, label_name, filenames_for_proportion)

    # Evaluating the decision tree classifiers.
    filenames_for_evaluate = ['clf-evaluate-{}.png'.format(rate) for rate in train_test_rates]
    evaluate_all_clf(clf_list, feature_test_list, label_test_list, filenames_for_evaluate)

    # The depth and accuracy of a decision tree (train/test - 80/20).
    index = test_rates.index(0.2)
    max_depths = [None, 2, 3, 4, 5, 6, 7]
    clf_list_for_max_depth, scores = calc_accuracy_scores(
        max_depths,
        feature_train_list[index],
        label_train_list[index],
        feature_test_list[index],
        label_test_list[index]
    )

    # Drawing the decision tree classifiers of `train/test - 80/20` rates for each max_depth.
    # Export these graph to png file with the correspoding name (filenames_for_max_depth).
    filenames_for_max_depth = ['clf-max-depth-{}.gv'.format(max_depth) for max_depth in max_depths]
    draw_graph(clf_list_for_max_depth, feature_names, label_name, filenames_for_max_depth)

    # Shows a table of accuracy scores of `train/test - 80/20` case.
    print('\n\n          TABLE')
    print('-----------------------------------')
    print('max_depth        Accuracy')
    print('-----------------------------------')
    for i in range(len(max_depths)):
        print(max_depths[i], '\t\t', scores[i])

    # Show all figures drawn in evaluate_all_clf() function.
    plt.show()


if __name__ == '__main__':
    main()
