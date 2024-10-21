import pandas as pd


adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
adv1_df.head(10)

adv1_df.loc[8, 'Daily Internet Usage']

adv2_df = pd.read_csv('advertising_2.csv', index_col='Number')
adv2_df.loc[533:536]