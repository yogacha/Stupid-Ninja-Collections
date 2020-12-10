# %%
import pandas as pd
from worksheet import WorkSheet

df1 = pd.DataFrame(
    data=[ [1, 2],
           [3, 4],
           [8, 7] ],
    index = ['001', '002', '003']
)

frames = WorkSheet()

frames['Data1'] = df1.copy()
frames['Data2'] = df1 + 8

frames.sum(axis=1).loc['001':'002'].max()
# %%
