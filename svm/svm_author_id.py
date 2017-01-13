#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC

#clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.0)


# Reduce training set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

# Training of the Model
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# Test prediction
t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

###=============TASK
print "Prediction 10", pred[10]
print "Prediction 26", pred[26]
print "Prediction 50", pred[50]

j = 0
for i in range(len(pred)):
    if pred[i] == 1:
        j += 1
print "Chris (1) class has ", j
#===================

### Calculate an accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)


print "Accuracy = ", accuracy

#########################################################


