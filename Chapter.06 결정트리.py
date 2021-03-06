from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


iris = load_iris()
X = iris.data[:, 2:] # 꽃잎 길이와 너비
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_clf.fit(X, y)


pip install graphviz
from graphviz import Source
from sklearn.tree import export_graphviz

import os
os.environ["PATH"]+=os.pathsep+'C:/Program Files (x86)/Graphviz2.38/bin/'
IMAGES_PATH = r'C:\Users\hwang\OneDrive - 고려대학교\바탕 화면\big_py'

export_graphviz(
        tree_clf,
        out_file=os.path.join(IMAGES_PATH, "iris_tree.dot"),
        feature_names=iris.feature_names[2:],
        class_names=iris.target_names,
        rounded=True,
        filled=True
    )

Source.from_file(os.path.join(IMAGES_PATH, "iris_tree.dot"))

# 특성 클래스 k에 속할 확률을 추정
tree_clf.predict_proba([[5, 1.5]]) # 확률 추정
tree_clf.predict([[5, 1.5]]) # 클래스 추정 











