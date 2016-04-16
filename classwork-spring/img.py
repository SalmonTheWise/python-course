__author__ = 'jack-a-lynn'
from scipy.ndimage import imread
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier,\
    ExtraTreesClassifier


def get_imgs(dir_name):
    imgs = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        imgs.append(x)
    imgs = np.array(imgs)
    return imgs

faces = get_imgs("faces")
non_faces = get_imgs("non_faces")
np.random.shuffle(faces)
np.random.shuffle(non_faces)
# print(faces.shape)
# print(non_faces.shape)

train_faces = faces[:350, ]
validate_faces = faces[350:, ]

train_non_faces = non_faces[:350, ]
validate_non_faces = non_faces[350:, ]

train = np.concatenate((train_faces, train_non_faces))
validate = np.concatenate((validate_faces, validate_non_faces))

print(train.shape)
print(validate.shape)

train_y = np.array((np.ones(350), np.zeros(350)))
train_y.shape = (700, )
print(train_y)

random_forest = ExtraTreesClassifier(n_estimators=200)
print(train.shape, train_y.shape)
random_forest = random_forest.fit(train, train_y)

importances = random_forest.feature_importances_
importances = importances.reshape((100, 100))

plt.matshow(importances, cmap=plt.cm.hot)
plt.title("plt")
plt.show()

validate_y = np.concatenate((np.ones(85), np.zeros(106)))
predicted_y = random_forest.predict(validate)
# print(validate_y == predicted_y)

from sklearn.metrics.classification import accuracy_score
print(accuracy_score(validate_y, predicted_y))

students_faces = get_imgs("students")
st_predicted = random_forest.predict(students_faces)
print(os.listdir("students"))
print(st_predicted)

