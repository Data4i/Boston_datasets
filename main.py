import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


def load_boston_dataset():
    data = datasets.load_boston()
    df = pd.DataFrame(data['data'], columns=data['feature_names'])
    return df


boston = load_boston_dataset()
print(boston.info())
non_racial_boston = boston.drop('B', axis=1)
print(non_racial_boston.info())

print(non_racial_boston.AGE.agg({'min', 'max', 'mean'}))

age = non_racial_boston['AGE']
bins_for_age = [0, 10, 30, 50, 70, 80, 100]
age_bracket = pd.cut(age, bins_for_age)
print(age_bracket.value_counts())
# This certifies that most people are old persons with the highest interval between 80-100

plt.figure(figsize=(20, 20))
non_racial_boston.AGE.plot(kind='hist', bins=[0, 10, 30, 50, 70, 80, 100])
plt.show()
# And this plot solidifies the fact that most people are old



def plot_price_to_age():
    fig = plt.figure(figsize=(10,7))

