import pandas as pd
import numpy as np

# creating a series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# creating a series from a dictionary
s = pd.Series({'a': 1, 'b': 2, 'c': 5})
print(s)

# Extracing a column from a dataframe
df = pd.DataFrame({'col1:': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})
s = df['col1:']
print(s)
print(df['col1:'])  # Extracting the values of a column
# this does not work print(df.col1)  # Extracting the values of a column

# setting the index of a dataframe
df.index = ['row1', 'row2', 'row3', 'row4']
print (df.loc['row2'])

print(df.iloc[0:4, 0])  # Extracting the values of a row

print(df[df['col1:'] > 2])  # Extracting the values of a column based on a condition

# data-preprocessing
# Creating sample dataframe

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5, 6, 7, 8],
    'B': ['one', 'two', np.nan, 'four', 'five', 'six', 'seven', 'eight'],
    'C': [True, False, np.nan, False, True, False, True, False]
    })

#displaying the dataframe
print("Original DataFrame:")
print(df)

# displaying missing values
print("\nMissing Values:")
print(df.isnull())
print(df.isna().sum())  # Count of missing values in each column

# filling missing values with a constant value (0)
df_fillna = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_fillna)

# dropping rows with missing values
df_dropna = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropna)

#dropping columns with missing values
df_dropna_col = df.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_dropna_col)
#this above is empty

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3],
    'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
    })

# displaying the dataframe
print("Original DataFrame:")
print(df)

# Identiyfying duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())  # Returns a boolean series indicating duplicate rows
print("\nDuplicate Rows Count:")
print(df.duplicated().sum())  # Returns the count of duplicate rows
# Dropping duplicate rows
df_drop_duplicates = df.drop_duplicates()
print("\nDataFrame after dropping duplicate rows:")
print(df_drop_duplicates)

# testing concatenation and/or join

#create two dataframes
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
    })
df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3','C4'],
    'D': ['D0', 'D1', 'D2', 'D3', 'D4'],
    'key': ['K0', 'K1', 'K2', 'K3', 'K4']
    })
# displaying the dataframes
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
# Concatenating the dataframes
df_concat = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame:")
print(df_concat)
# Merging the dataframes on key column inner join
df_merge = pd.merge(df1, df2, on='key', how='inner')
print("\nMerged inner join DataFrame:")
print(df_merge)
# Merging the dataframes on key column left join
df_merge = pd.merge(df1, df2, on='key', how='left')  # left join
print("\nMerged left join DataFrame:")
print(df_merge)
# Joining the dataframes on key column right join
df_join = pd.merge(df1, df2, on='key', how='right')  # right join
print("\nMerged right join DataFrame:")
print(df_join)
# Joining the dataframes on key column outer join
df_join = pd.merge(df1, df2, on='key', how='outer')  # outer join
print("\nMerged outer join DataFrame:")
print(df_join)

#Advanced dataframe operations like encoding, normalization

# creating a dataframe
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'foo', 'bar', 'baz'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': [1, 2, 3, 4, 5, 6],
    'D': [10, 20, 30, 40, 50, 60]
})

# displaying the dataframe
print("Original DataFrame:")
print(df)
# Encoding categorical variables
df['A_encoded'] = df['A'].astype('category').cat.codes
df['B_encoded'] = df['B'].astype('category').cat.codes
print("\nDataFrame after encoding categorical variables:")
print(df)
# Normalizing Min - Max scaling (range 0-1)
df['C_normalized'] = (df['C'] - df['C'].min()) / (df['C'].max() - df['C'].min())
df['D_normalized'] = (df['D'] - df['D'].min()) / (df['D'].max() - df['D'].min())
print("\nDataFrame after normalization:")
print(df)

# advanced groupby operations
group_df = df.groupby(['A', 'B']).agg({'C_normalized': ['mean'], 'D_normalized': ['sum']}).reset_index()
print("\nGrouped DataFrame:")
print(group_df) 