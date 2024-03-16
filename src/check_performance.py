import pandas as pd
from memory_profiler import memory_usage


def my_function():
    data = pd.read_csv('src/train.csv')
    return data
print(memory_usage((my_function)))