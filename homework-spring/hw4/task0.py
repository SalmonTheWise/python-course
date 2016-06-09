__author__ = 'jack-a-lynn'
from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, \
    GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score


# function to get images from directory as matrix
# with shape of (n, 10000)
def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images

# lets get images from siamese and other_cats directories
# and then shuffle them so our train/validation split is fair
siamese = get_images("siamese")
other_cats = get_images("other_cats")
np.random.shuffle(siamese)
np.random.shuffle(other_cats)

# print(siamese.shape)
# print(other_cats.shape)


# lets get 300 (150 siamese and 150 other cats) of images as training data
train_s = siamese[:150, ]
train_oc = other_cats[:150, ]

# other images are validation data
validate_s = siamese[150:, ]
validate_oc = other_cats[150:, ]

train = np.concatenate((train_s, train_oc))
validate = np.concatenate((validate_s, validate_oc))

# true classes 1 for siamese image and 0 for other cats image
train_y = np.concatenate((np.ones(150), np.zeros(150)))


# lets learn our Classifier

forests = (RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier)
estimators = (10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000)


scores = []
for k in forests:
    for i in estimators:
        random_forest = k(n_estimators=i)
        random_forest = random_forest.fit(train, train_y)
        validate_y = np.concatenate((np.ones(50), np.zeros(50)))
        predicted_y = random_forest.predict(validate)
        scores.append(accuracy_score(validate_y, predicted_y))

RF = scores[0:11]
ET = scores[11:22]
AB = scores[22:33]
GB = scores[33:44]

#lets write!

est_accuracy = open('estimators_table.txt', 'w')
est_accuracy.write('\t'.join(['Forest', 'n=10', 'n=20', 'n=40',
                              'n=80', 'n=100', 'n=150', 'n=200', 'n=300', 'n=400', 'n=500', 'n=1000']) + '\n')
est_accuracy.write('RandomForestClassifier\t')
for score in RF:
    est_accuracy.write("%s " % score + '\t')
est_accuracy.write('\n')
est_accuracy.write('ExtraTreesClassifier\t')
for score in ET:
    est_accuracy.write("%s " % score + '\t')
est_accuracy.write('\n')
est_accuracy.write('AdaBoostClassifier\t')
for score in AB:
    est_accuracy.write("%s " % score + '\t')
est_accuracy.write('\n')
est_accuracy.write('GradientBoostingClassifier\t')
for score in GB:
    est_accuracy.write("%s " % score + '\t')
est_accuracy.close()
