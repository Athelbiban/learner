from pydoc import help
from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'x': [4, 5, 2, 3, 1],
    'y': [2, 1, 4, 3, 5]
}

df = pd.DataFrame(data)

# help(pearsonr)

plt.scatter(data['x'], data['y'])
plt.show()

res = pearsonr(data['x'], data['y'])
print(res)

'''Коэффициент Пирсона, посчитанный вручную'''

# mean_x = sum(data['x']) / len(data['x'])
# mean_y = sum(data['y']) / len(data['y'])
#
# n = len(data['x'])
# sum_mean_xy = 0
# sum_mean_xq = 0
# sum_mean_yq = 0
#
# for i in range(n):
#     sum_mean_x = (data['x'][i] - mean_x)
#     sum_mean_xq += sum_mean_x ** 2
#     sum_mean_y = (data['y'][i] - mean_y)
#     sum_mean_yq += sum_mean_y ** 2
#     sum_mean_xy += sum_mean_x * sum_mean_y
# cov = sum_mean_xy / (n - 1)
#
# sd_x = (sum_mean_xq / (n-1)) ** 0.5
# sd_y = (sum_mean_yq / (n-1)) ** 0.5
# r_xy = cov / (sd_x * sd_y)
# print(r_xy)
