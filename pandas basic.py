import numpy as np
import pandas as  pd
from sklearn.datasets import load_iris

iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, column=iris.feature_names)
iris_df.head()