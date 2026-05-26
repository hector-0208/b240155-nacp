import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3], [3, 4, 5]])
print(f"dims = {arr.ndim}, shape = {arr.shape}")
col_sum = arr.sum(axis=0)
row_sum = arr.sum(axis=1)
print(f"col sum = {col_sum}, row sum = {row_sum}")
set_a = {1, 2, 3}
set_b = {1, 2}
print(
    f"Is {set_a} disjoint of {set_b}? \
    {set_a.isdisjoint(set_b)}"
)
grades_dict = {'a':91, 'b':23, 'v':34}
grades_series = pd.Series(grades_dict)
print(f"{grades_series}")
