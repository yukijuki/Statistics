import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import csv

iris = load_iris()
#sklearnは機械学習のオープンソースライブラリ
#irisはデータセット

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df.rename(columns = {
    "sepal length (cm)": "sepal_l",
    "sepal width (cm)": "sepal_w",
    "petal length (cm)": "petal_l",
    "petal width (cm)": "petal_w"    
}, inplace = True
)

df.to_csv("new_names.csv", index=False)

# with open("new_names.csv", "w") as new_file:
#     fieldnames = ["sepal_l", "sepal_w", "   ", "sepal_l2", "sepal_w2", "petal_l2"]
#     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
#     csv_writer.writeheader()
        
#     print("for loop start")
#     for line in csv_reader:
#         print(line)
#         csv_writer.writerow(line)

df1 = pd.read_csv("new_names.csv")
print(df1)