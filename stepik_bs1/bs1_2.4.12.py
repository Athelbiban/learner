import pandas as pd
from scipy import stats

URL = 'https://stepik.org/media/attachments/lesson/8083/genetherapy.csv'
data = pd.read_csv(URL)
samples = [list(frame) for group, frame in data.groupby('Therapy')['expr']]
print(stats.f_oneway(*samples))
