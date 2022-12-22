#! /usr/bin/python3

import sys, os
import numpy as np
import operator

def createDataSet(data, label):
    group = np.array(data)
    labels = label
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
        key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def training(f_training):
    data_arr = []
    label_arr = []
    for f_name in os.listdir(f_training):
        label_arr.append(int(f_name.split('_')[0]))
        with open(f_training + "/" + f_name, "rt") as f:
            count = 0
            f_data = []
            for line in f:
                f_data.append(line.strip())
            f_data = "".join(f_data)
        data_arr.append(list(map(int, f_data)))
    return data_arr, label_arr

def test(f_test, group, labels, k):
    error = 0
    for f_name in os.listdir(f_test):
        answer = int(f_name.split('_')[0])
        data = []
        with open(f_test + "/" + f_name, "rt") as f:
            count = 0
            f_data = []
            for line in f:
                f_data.append(line.strip())
            f_data = "".join(f_data)
        result = classify0(list(map(int, f_data)), group, labels, k)
        if result != answer:
            error += 1
    return error

dir_training = sys.argv[1]
dir_test = sys.argv[2]

data_arr, label_arr = training(dir_training)
group, labels = createDataSet(data_arr, label_arr)
for k in range(1, 21):
    error = test(dir_test, group, labels, k)
    print(round((error / len(os.listdir(dir_test))) * 100))


