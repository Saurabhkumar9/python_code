import pandas as pd
import numpy as np

# ===========================================================
# PANDAS - COMPLETE GUIDE: BASIC TO ADVANCED
# Hindi + English Comments | All Functions Covered
# ===========================================================

# ======================
# SECTION 1: DATA STRUCTURES BANANA (CREATION)
# ======================

# 1. Series banana (1D data) | Create a 1D labeled array called Series
s = pd.Series([10, 20, 30, 40, 50])

# 2. Custom index ke saath Series | Series with custom labels as index
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# 3. Dictionary se Series banana | Create Series from dictionary
s3 = pd.Series({'name': 'Rahul', 'age': 25, 'city': 'Delhi'})

# 4. DataFrame banana (2D table) | Create a 2D table (like Excel sheet)
df = pd.DataFrame({
    'Name':   ['Rahul', 'Priya', 'Amit', 'Neha', 'Ravi'],
    'Age':    [25, 30, 22, 28, 35],
    'City':   ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Pune'],
    'Salary': [50000, 70000, 40000, 60000, 80000],
    'Score':  [85.5, 90.0, 78.3, 88.7, 92.1]
})

# 5. List of lists se DataFrame | Create DataFrame from list of rows
df2 = pd.DataFrame(
    [['Alice', 25], ['Bob', 30], ['Carol', 28]],
    columns=['Name', 'Age']
)

# 6. Dictionary list se DataFrame | Create DataFrame from list of dicts
df3 = pd.DataFrame([
    {'product': 'Apple',  'price': 50,  'qty': 100},
    {'product': 'Banana', 'price': 20,  'qty': 200},
    {'product': 'Mango',  'price': 80,  'qty': 150},
])

# 7. NumPy array se DataFrame | Create DataFrame from NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df4 = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# 8. Empty DataFrame banana | Create an empty DataFrame with column names only
df_empty = pd.DataFrame(columns=['Name', 'Age', 'City'])

# 9. Range index wala DataFrame | DataFrame with numeric range as index
df5 = pd.DataFrame({'x': range(5), 'y': range(5, 10)})

# 10. from_dict se DataFrame | Create DataFrame using from_dict method
df6 = pd.DataFrame.from_dict({'col1': [1, 2], 'col2': [3, 4]})

# 11. from_records se DataFrame | Create DataFrame from list of tuples/records
df7 = pd.DataFrame.from_records([(1, 'A'), (2, 'B'), (3, 'C')], columns=['id', 'val'])


# ======================
# SECTION 2: DATA DEKHNA (VIEWING DATA)
# ======================

# 12. Pehli 5 rows dekhna | Show first 5 rows of DataFrame
df.head()

# 13. Pehli N rows dekhna | Show first N rows (here 3)
df.head(3)

# 14. Aakhri 5 rows dekhna | Show last 5 rows of DataFrame
df.tail()

# 15. Aakhri N rows dekhna | Show last N rows (here 2)
df.tail(2)

# 16. DataFrame ka shape dekhna | Check (rows, columns) count
df.shape

# 17. Column names dekhna | Get list of all column names
df.columns

# 18. Index dekhna | View the row index of DataFrame
df.index

# 19. Data types dekhna | Check data type of each column
df.dtypes

# 20. Summary info dekhna | Show column names, types, non-null counts
df.info()

# 21. Statistical summary dekhna | Show count, mean, std, min, max for numbers
df.describe()

# 22. Sabhi columns ka describe | Include non-numeric columns too
df.describe(include='all')

# 23. Total values count karna | Count total number of elements
df.size

# 24. Kitne dimensions hain | Check number of dimensions (always 2 for DataFrame)
df.ndim

# 25. Column ki values dekhna | Get all values of one column as Series
df['Name']

# 26. Multiple columns dekhna | Select multiple columns at once
df[['Name', 'Salary']]

# 27. Values as NumPy array | Get all data as a NumPy array
df.values

# 28. Axes dekhna | Get list of [row index, column index]
df.axes

# 29. DataFrame khali hai ya nahi | Check if DataFrame is empty
df.empty

# 30. Attributes dekhna | View/set custom metadata on DataFrame
df.attrs


# ======================
# SECTION 3: DATA SELECT KARNA (SELECTION & INDEXING)
# ======================

# 31. loc se row select karna (label based) | Select row by label/index name
df.loc[0]

# 32. loc se row aur column | Select specific row and column by label
df.loc[0, 'Name']

# 33. loc se range select | Select row 0 to 2, specific columns
df.loc[0:2, ['Name', 'Age']]

# 34. iloc se row select (position based) | Select row by position number
df.iloc[0]

# 35. iloc se specific cell | Select cell by row and column position
df.iloc[0, 1]

# 36. iloc se slice | Select rows 0-2, columns 0-2 by position
df.iloc[0:3, 0:2]

# 37. at se single value | Fast access to single value by label
df.at[0, 'Name']

# 38. iat se single value | Fast access to single value by position
df.iat[0, 1]

# 39. Boolean filter | Filter rows where Age > 25
df[df['Age'] > 25]

# 40. Multiple conditions filter | Filter with AND condition
df[(df['Age'] > 25) & (df['Salary'] > 55000)]

# 41. OR condition filter | Filter with OR condition
df[(df['City'] == 'Delhi') | (df['City'] == 'Mumbai')]

# 42. query se filter karna | Filter using SQL-like query string
df.query('Age > 25 and Salary > 50000')

# 43. isin se filter karna | Filter rows where City is in given list
df[df['City'].isin(['Delhi', 'Mumbai'])]

# 44. between se filter | Filter numeric values in a range
df[df['Age'].between(25, 30)]

# 45. xs se cross-section | Select data using cross-section (for MultiIndex)
df.xs(0)

# 46. get se column lena | Get column safely (returns None if missing)
df.get('Name')

# 47. keys dekhna | Get column names (same as df.columns)
df.keys()

# 48. items iterate karna | Iterate over (column_name, Series) pairs
for col_name, series in df.items():
    pass  # use col_name and series here

# 49. iterrows karna | Iterate over rows as (index, Series) pairs
for idx, row in df.iterrows():
    pass  # use idx and row['Name'] etc.

# 50. itertuples karna | Iterate rows as named tuples (faster than iterrows)
for row in df.itertuples():
    pass  # use row.Name, row.Age etc.


# ======================
# SECTION 4: DATA BADALNA (MODIFICATION)
# ======================

# 51. Naya column add karna | Add a new column to DataFrame
df['Tax'] = df['Salary'] * 0.1

# 52. Column ki value update karna | Update all values in a column
df['Tax'] = df['Salary'] * 0.15

# 53. assign se naya column | Add new column using assign (returns new df)
df = df.assign(Net_Salary=df['Salary'] - df['Tax'])

# 54. Column rename karna | Rename one or more columns
df = df.rename(columns={'Net_Salary': 'Take_Home'})

# 55. Index rename karna | Rename the index axis
df = df.rename_axis('Employee_ID')

# 56. Column delete karna (drop) | Remove a column from DataFrame
df = df.drop(columns=['Tax'])

# 57. Row delete karna | Remove a row by index
df = df.drop(index=0)
df = df.reset_index(drop=True)  # Re-number index after drop

# 58. Multiple columns drop karna | Remove multiple columns at once
df_temp = df.drop(columns=['Take_Home', 'Score'])

# 59. Column insert karna specific position pe | Insert column at exact position
df.insert(2, 'Department', ['IT', 'HR', 'Finance', 'IT'])

# 60. pop se column nikalna | Remove and return a column
dept_col = df.pop('Department')

# 61. set_index karna | Set a column as the row index
df_indexed = df.set_index('Name')

# 62. reset_index karna | Reset index back to default numbers
df_reset = df_indexed.reset_index()

# 63. loc se value set karna | Set a specific cell value using loc
df.loc[1, 'Age'] = 31

# 64. iloc se value set karna | Set a specific cell value using iloc
df.iloc[0, 1] = 26

# 65. isetitem se column set karna | Set column values using isetitem
df.isetitem(1, [26, 31, 22, 28])

# 66. update karna | Update values from another DataFrame (only non-NaN)
df_update = pd.DataFrame({'Age': [99, 99]}, index=[0, 1])
df.update(df_update)
df.loc[[0, 1], 'Age'] = [25, 30]  # restore original

# 67. replace karna | Replace specific value with another
df['City'] = df['City'].replace('Delhi', 'New Delhi')

# 68. map se values transform karna | Apply a mapping/function to each value
df['City'] = df['City'].map({'New Delhi': 'Delhi', 'Mumbai': 'Mumbai',
                              'Chennai': 'Chennai', 'Kolkata': 'Kolkata'})

# 69. apply se function lagana (column-wise) | Apply function to each column
df['Salary'].apply(lambda x: x * 1.1)

# 70. apply axis=1 (row-wise) | Apply function to each row
df.apply(lambda row: row['Salary'] / row['Age'], axis=1)

# 71. applymap / map (element-wise on DataFrame) | Apply function to every cell
df[['Age', 'Salary', 'Score']].map(lambda x: round(x, 0))

# 72. transform se aggregate karna | Apply function and return same-shape result
df[['Salary', 'Age']].transform(lambda x: (x - x.mean()) / x.std())

# 73. eval se expression | Compute expression on DataFrame columns
df.eval('Salary + Score')

# 74. astype se datatype change | Change column data type
df['Age'] = df['Age'].astype(float)
df['Age'] = df['Age'].astype(int)

# 75. convert_dtypes karna | Auto-convert to best possible dtypes
df.convert_dtypes()


# ======================
# SECTION 5: MISSING DATA HANDLE KARNA
# ======================

# 76. Missing values wala DataFrame banana | Create DataFrame with NaN values
df_nan = pd.DataFrame({
    'A': [1, 2, np.nan, 4, np.nan],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
})

# 77. isna / isnull se NaN dhundhna | Check which cells are NaN (True/False)
df_nan.isna()

# 78. notna / notnull | Check which cells are NOT NaN
df_nan.notna()

# 79. NaN count per column | Count missing values in each column
df_nan.isna().sum()

# 80. Koi bhi NaN hai check karna | Check if any value is NaN anywhere
df_nan.isna().any()

# 81. Sabhi NaN hain check | Check if all values in column are NaN
df_nan.isna().all()

# 82. NaN rows drop karna | Remove rows that have any NaN value
df_nan.dropna()

# 83. NaN columns drop karna | Remove columns that have any NaN value
df_nan.dropna(axis=1)

# 84. Minimum non-NaN threshold | Keep rows with at least 2 non-NaN values
df_nan.dropna(thresh=2)

# 85. NaN ko value se fill karna | Replace all NaN with a specific value (e.g. 0)
df_nan.fillna(0)

# 86. NaN ko column mean se fill | Fill NaN with that column's mean value
df_nan.fillna(df_nan.mean(numeric_only=True))

# 87. Forward fill (ffill) | Fill NaN using the previous valid value
df_nan.ffill()

# 88. Backward fill (bfill) | Fill NaN using the next valid value
df_nan.bfill()

# 89. Interpolate karna | Fill NaN using linear interpolation between values
df_nan.interpolate()

# 90. NaN ko specific column value se fill | Fill each column with its own value
df_nan.fillna({'A': 0, 'B': df_nan['B'].mean()})


# ======================
# SECTION 6: SORTING
# ======================

# 91. Column ke basis pe sort karna | Sort DataFrame by column values
df.sort_values('Salary')

# 92. Descending order me sort | Sort from highest to lowest
df.sort_values('Salary', ascending=False)

# 93. Multiple columns se sort | Sort by Age first, then Salary
df.sort_values(['Age', 'Salary'], ascending=[True, False])

# 94. Index ke basis pe sort | Sort rows by their index labels
df.sort_index()

# 95. Index descending sort | Sort index from high to low
df.sort_index(ascending=False)

# 96. nlargest - top N values | Get top 3 rows by Salary
df.nlargest(3, 'Salary')

# 97. nsmallest - bottom N values | Get bottom 3 rows by Salary
df.nsmallest(3, 'Salary')

# 98. rank nikalna | Assign rank to each value (1 = smallest)
df['Salary'].rank()

# 99. rank descending | Rank from highest (1 = biggest)
df['Salary'].rank(ascending=False)


# ======================
# SECTION 7: GROUPBY & AGGREGATION
# ======================

# 100. groupby se group banana | Group rows by City column
grouped = df.groupby('City')

# 101. Group ka sum nikalna | Sum of Salary for each City
df.groupby('City')['Salary'].sum()

# 102. Group ka mean nikalna | Average Salary per City
df.groupby('City')['Salary'].mean()

# 103. Group ka count nikalna | Count of people in each City
df.groupby('City')['Name'].count()

# 104. Multiple aggregation | Apply multiple functions at once
df.groupby('City')['Salary'].agg(['sum', 'mean', 'count', 'min', 'max'])

# 105. agg with dict | Different aggregation for different columns
df.groupby('City').agg({'Salary': 'sum', 'Age': 'mean', 'Score': 'max'})

# 106. Named aggregation | Give custom names to aggregated columns
df.groupby('City').agg(
    Total_Salary=('Salary', 'sum'),
    Avg_Age=('Age', 'mean')
)

# 107. transform with groupby | Add group mean as new column (same shape)
df['City_Avg_Salary'] = df.groupby('City')['Salary'].transform('mean')
df = df.drop(columns=['City_Avg_Salary'])

# 108. filter with groupby | Keep only groups where mean salary > 50000
df.groupby('City').filter(lambda x: x['Salary'].mean() > 50000)

# 109. value_counts | Count frequency of each unique value
df['City'].value_counts()

# 110. value_counts normalize | Show as percentage/proportion
df['City'].value_counts(normalize=True)

# 111. nunique | Count of unique values per column
df.nunique()

# 112. unique values | Get all unique values in a column
df['City'].unique()

# 113. crosstab banana | Cross-tabulation frequency table of two columns
pd.crosstab(df['City'], df['Age'])

# 114. pivot table banana | Pivot table like Excel (aggregated)
df_pt = pd.DataFrame({
    'City':   ['Delhi','Delhi','Mumbai','Mumbai','Chennai'],
    'Dept':   ['IT','HR','IT','HR','IT'],
    'Salary': [50000,45000,70000,60000,40000]
})
pd.pivot_table(df_pt, values='Salary', index='City',
               columns='Dept', aggfunc='mean', fill_value=0)

# 115. pivot (reshape) | Reshape without aggregation (unique combos only)
df_piv = pd.DataFrame({
    'date': ['Jan','Jan','Feb','Feb'],
    'item': ['A','B','A','B'],
    'val':  [10, 20, 30, 40]
})
df_piv.pivot(index='date', columns='item', values='val')


# ======================
# SECTION 8: JOINING & MERGING
# ======================

# 116. concat rows | Stack two DataFrames vertically (add rows)
df_a = pd.DataFrame({'Name': ['Rahul', 'Priya'], 'Score': [85, 90]})
df_b = pd.DataFrame({'Name': ['Amit', 'Neha'],  'Score': [78, 88]})
pd.concat([df_a, df_b], ignore_index=True)

# 117. concat columns | Join two DataFrames side by side (add columns)
df_c = pd.DataFrame({'Tax': [5000, 7000], 'Bonus': [2000, 3000]})
pd.concat([df_a, df_c], axis=1)

# 118. merge (inner join) | Keep only matching rows from both DataFrames
df_left  = pd.DataFrame({'id': [1,2,3,4], 'Name': ['A','B','C','D']})
df_right = pd.DataFrame({'id': [1,2,5],   'Dept': ['IT','HR','Finance']})
pd.merge(df_left, df_right, on='id')

# 119. left join | Keep all left rows, match right rows where possible
pd.merge(df_left, df_right, on='id', how='left')

# 120. right join | Keep all right rows, match left rows where possible
pd.merge(df_left, df_right, on='id', how='right')

# 121. outer join | Keep all rows from both, fill NaN where no match
pd.merge(df_left, df_right, on='id', how='outer')

# 122. merge on different column names | Join when key columns have different names
df_r2 = pd.DataFrame({'emp_id': [1,2], 'Salary': [50000, 70000]})
pd.merge(df_left, df_r2, left_on='id', right_on='emp_id')

# 123. join method | Join using index alignment
df_j1 = pd.DataFrame({'A': [1,2,3]}, index=[0,1,2])
df_j2 = pd.DataFrame({'B': [4,5,6]}, index=[0,1,2])
df_j1.join(df_j2)

# 124. merge_asof | Merge on nearest key (used for time-series / sorted data)
df_prices  = pd.DataFrame({'time': [1,3,5,7], 'price': [100,110,105,120]})
df_trades  = pd.DataFrame({'time': [2,4,6],   'qty':   [10, 20, 15]})
pd.merge_asof(df_trades, df_prices, on='time')

# 125. merge_ordered | Merge and sort by key (useful for time-series)
pd.merge_ordered(df_a, df_b, on='Name')

# 126. combine | Combine two DataFrames using a custom function
df_x = pd.DataFrame({'A': [1, np.nan], 'B': [3, 4]})
df_y = pd.DataFrame({'A': [5, 6],      'B': [np.nan, 8]})
df_x.combine(df_y, lambda s1, s2: s1.where(s1.notna(), s2))

# 127. combine_first | Fill NaN in df_x using values from df_y
df_x.combine_first(df_y)

# 128. align | Align two DataFrames on same index/columns
df_x.align(df_y)

# 129. compare | Show differences between two DataFrames
df_orig    = pd.DataFrame({'A': [1, 2, 3]})
df_changed = pd.DataFrame({'A': [1, 5, 3]})
df_orig.compare(df_changed)

# 130. update | Update df_x values from df_y (only where df_x is NaN)
df_x.update(df_y)


# ======================
# SECTION 9: RESHAPING DATA
# ======================

# 131. melt karna | Convert wide format to long format (unpivot)
df_wide = pd.DataFrame({'Name': ['Rahul','Priya'], 'Math': [90,85], 'Science': [80,88]})
pd.melt(df_wide, id_vars='Name', value_vars=['Math','Science'],
        var_name='Subject', value_name='Marks')

# 132. stack karna | Move column headers into row index (wide to long)
df_wide.set_index('Name').stack()

# 133. unstack karna | Move inner row index back to columns (long to wide)
df_wide.set_index('Name').stack().unstack()

# 134. transpose karna (.T) | Swap rows and columns
df.T

# 135. transpose method | Same as .T but as a method call
df.transpose()

# 136. explode karna | Expand list values in a column into separate rows
df_explode = pd.DataFrame({'Name': ['Rahul', 'Priya'], 'Hobbies': [['Cricket','Chess'], ['Reading']]})
df_explode.explode('Hobbies')

# 137. wide_to_long | Reshape wide format with repeated column patterns
df_w = pd.DataFrame({'id':[1,2],'math_2020':[90,85],'math_2021':[92,88]})
pd.wide_to_long(df_w, stubnames='math', i='id', j='year', sep='_')

# 138. lreshape | Reshape from wide format using group mapping
df_lr = pd.DataFrame({'id':[1,2],'jan_sales':[100,200],'feb_sales':[150,250]})
pd.lreshape(df_lr, {'sales': ['jan_sales','feb_sales']})

# 139. pivot karna (top-level) | Pivot using top-level pd.pivot function
pd.pivot(df_piv, index='date', columns='item', values='val')

# 140. squeeze karna | Convert single-column DataFrame to Series
pd.DataFrame({'A': [1,2,3]}).squeeze()

# 141. swaplevel | Swap two levels in MultiIndex
arrays = [['A','A','B','B'], [1,2,1,2]]
idx = pd.MultiIndex.from_arrays(arrays, names=['letter','number'])
s_multi = pd.Series([10,20,30,40], index=idx)
s_multi.swaplevel()

# 142. reorder_levels | Reorder MultiIndex levels
s_multi.reorder_levels(['number','letter'])

# 143. droplevel | Remove one level from MultiIndex
s_multi.droplevel('number')

# 144. from_dummies | Convert dummy/one-hot columns back to single column
df_dummies = pd.DataFrame({'City_Delhi':[1,0,0],'City_Mumbai':[0,1,0],'City_Pune':[0,0,1]})
pd.from_dummies(df_dummies, sep='_')

# 145. get_dummies | Convert categorical column to dummy/one-hot columns
pd.get_dummies(df['City'], prefix='City')


# ======================
# SECTION 10: STRING OPERATIONS
# ======================

# 146. str.upper | Convert all strings to uppercase
df['Name'].str.upper()

# 147. str.lower | Convert all strings to lowercase
df['Name'].str.lower()

# 148. str.strip | Remove leading and trailing whitespace
df['Name'].str.strip()

# 149. str.replace | Replace part of string with another string
df['City'].str.replace('Delhi', 'New Delhi')

# 150. str.contains | Check if string contains a pattern (True/False)
df['Name'].str.contains('a', case=False)

# 151. str.startswith | Check if string starts with given text
df['Name'].str.startswith('R')

# 152. str.endswith | Check if string ends with given text
df['Name'].str.endswith('a')

# 153. str.len | Get length of each string
df['Name'].str.len()

# 154. str.split | Split string into list by separator
df['City'].str.split('a')

# 155. str.join | Join list elements with a separator
pd.Series([['a','b'], ['c','d']]).str.join('-')

# 156. str.get | Get character at specific position
df['Name'].str.get(0)

# 157. str.slice | Slice string characters by position
df['Name'].str.slice(0, 3)

# 158. str.count | Count how many times pattern appears in each string
df['Name'].str.count('a')

# 159. str.find | Find position of first occurrence of pattern
df['Name'].str.find('a')

# 160. str.extract | Extract pattern using regex groups
df['Name'].str.extract(r'([A-Z][a-z]+)')

# 161. str.extractall | Extract all matches of regex pattern
df['Name'].str.extractall(r'([aeiou])')

# 162. str.match | Check if string matches pattern from start
df['Name'].str.match(r'R[a-z]+')

# 163. str.fullmatch | Check if entire string matches pattern
df['Name'].str.fullmatch(r'[A-Za-z]+')

# 164. str.pad | Pad string to given width with fill character
df['Name'].str.pad(10, side='right', fillchar='*')

# 165. str.zfill | Pad numeric string with zeros on left
pd.Series(['1', '42', '100']).str.zfill(5)

# 166. str.title | Convert string to title case
df['Name'].str.title()

# 167. str.capitalize | Capitalize first letter only
df['Name'].str.capitalize()

# 168. str.cat | Concatenate all strings in Series
df['Name'].str.cat(sep=', ')

# 169. str.wrap | Wrap long strings to given width
pd.Series(['This is a long string that needs wrapping']).str.wrap(15)

# 170. str.normalize | Unicode normalize strings (NFKD, NFC etc.)
df['Name'].str.normalize('NFKD')


# ======================
# SECTION 11: DATETIME OPERATIONS
# ======================

# 171. to_datetime se convert karna | Convert string/numbers to datetime
pd.to_datetime(['2024-01-01', '2024-06-15', '2024-12-31'])

# 172. date_range banana | Create sequence of dates
pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')

# 173. Period range banana | Create range of periods (months, quarters)
pd.period_range(start='2024-01', periods=6, freq='M')

# 174. Timedelta banana | Create time difference object
pd.Timedelta('5 days 3 hours')

# 175. timedelta_range | Create range of timedeltas
pd.timedelta_range(start='1 day', periods=5, freq='D')

# 176. dt accessor - year nikalna | Extract year from datetime column
df_time = pd.DataFrame({'date': pd.date_range('2024-01-01', periods=4, freq='ME')})
df_time['date'].dt.year

# 177. dt.month nikalna | Extract month from datetime
df_time['date'].dt.month

# 178. dt.day nikalna | Extract day from datetime
df_time['date'].dt.day

# 179. dt.hour nikalna | Extract hour from datetime
df_time['date'].dt.hour

# 180. dt.day_name | Get day name (Monday, Tuesday etc.)
df_time['date'].dt.day_name()

# 181. dt.month_name | Get month name (January, February etc.)
df_time['date'].dt.month_name()

# 182. dt.dayofweek | Get day of week as number (0=Monday, 6=Sunday)
df_time['date'].dt.dayofweek

# 183. dt.is_month_end | Check if date is last day of month
df_time['date'].dt.is_month_end

# 184. dt.quarter | Get quarter number (1 to 4)
df_time['date'].dt.quarter

# 185. dt.weekofyear | Get week number of year
df_time['date'].dt.isocalendar().week

# 186. tz_localize | Assign timezone to datetime (make it timezone-aware)
df_time['date'].dt.tz_localize('Asia/Kolkata')

# 187. tz_convert | Convert from one timezone to another
df_time['date'].dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')

# 188. to_period | Convert datetime to period (e.g., monthly period)
df_time['date'].dt.to_period('M')

# 189. to_timestamp | Convert period back to timestamp
df_time['date'].dt.to_period('M').dt.to_timestamp()

# 190. infer_freq | Automatically detect frequency of datetime index
pd.infer_freq(pd.date_range('2024-01-01', periods=5, freq='D'))


# ======================
# SECTION 12: STATISTICAL FUNCTIONS
# ======================

# 191. sum nikalna | Sum of all values column-wise
df[['Age', 'Salary', 'Score']].sum()

# 192. mean nikalna | Average of each column
df[['Age', 'Salary', 'Score']].mean()

# 193. median nikalna | Middle value of each column
df[['Age', 'Salary', 'Score']].median()

# 194. min nikalna | Minimum value in each column
df[['Age', 'Salary', 'Score']].min()

# 195. max nikalna | Maximum value in each column
df[['Age', 'Salary', 'Score']].max()

# 196. std nikalna | Standard deviation of each column
df[['Age', 'Salary', 'Score']].std()

# 197. var nikalna | Variance of each column
df[['Age', 'Salary', 'Score']].var()

# 198. sem nikalna | Standard error of the mean
df[['Age', 'Salary', 'Score']].sem()

# 199. skew nikalna | Skewness (asymmetry) of distribution
df[['Age', 'Salary', 'Score']].skew()

# 200. kurt / kurtosis nikalna | Kurtosis (tail heaviness) of distribution
df[['Age', 'Salary', 'Score']].kurt()

# 201. quantile nikalna | Value at given quantile (0.25 = 25th percentile)
df[['Age', 'Salary', 'Score']].quantile(0.25)

# 202. mode nikalna | Most frequently occurring value
df[['Age', 'Salary', 'Score']].mode()

# 203. abs nikalna | Absolute (positive) value of each element
df[['Age', 'Salary', 'Score']].abs()

# 204. cumsum nikalna | Cumulative (running) sum
df['Salary'].cumsum()

# 205. cumprod nikalna | Cumulative product
df['Score'].cumprod()

# 206. cummax nikalna | Cumulative maximum (running max so far)
df['Salary'].cummax()

# 207. cummin nikalna | Cumulative minimum (running min so far)
df['Salary'].cummin()

# 208. diff nikalna | Difference between consecutive rows
df['Salary'].diff()

# 209. pct_change nikalna | Percentage change between consecutive rows
df['Salary'].pct_change()

# 210. corr nikalna | Correlation matrix of all numeric columns
df[['Age', 'Salary', 'Score']].corr()

# 211. corrwith nikalna | Correlation of each column with a specific Series
df[['Age', 'Salary', 'Score']].corrwith(df['Salary'])

# 212. cov nikalna | Covariance matrix of numeric columns
df[['Age', 'Salary', 'Score']].cov()

# 213. count nikalna | Count of non-NaN values per column
df.count()

# 214. prod nikalna | Product of all values in each column
df[['Age', 'Score']].prod()

# 215. round karna | Round all values to 2 decimal places
df[['Score']].round(2)

# 216. clip karna | Limit values between a min and max
df[['Salary']].clip(lower=45000, upper=75000)

# 217. add karna | Add a number or another DataFrame (element-wise)
df[['Age', 'Salary']].add(1000)

# 218. sub karna | Subtract element-wise
df[['Age', 'Salary']].sub(100)

# 219. mul karna | Multiply element-wise
df[['Score']].mul(2)

# 220. div / truediv karna | Divide element-wise
df[['Salary']].div(1000)

# 221. floordiv karna | Integer (floor) division element-wise
df[['Salary']].floordiv(10000)

# 222. mod karna | Modulo (remainder) element-wise
df[['Age']].mod(5)

# 223. pow karna | Raise to power element-wise
df[['Score']].pow(2)

# 224. dot product | Matrix dot product with another DataFrame
df_num = df[['Age', 'Salary']].head(2)
df_num.dot(df_num.T)

# 225. idxmax | Index label of maximum value in each column
df[['Age', 'Salary', 'Score']].idxmax()

# 226. idxmin | Index label of minimum value in each column
df[['Age', 'Salary', 'Score']].idxmin()


# ======================
# SECTION 13: WINDOW FUNCTIONS
# ======================

# 227. rolling mean | Moving average over last N rows
df['Salary'].rolling(window=2).mean()

# 228. rolling sum | Rolling sum over last N rows
df['Salary'].rolling(window=2).sum()

# 229. rolling std | Rolling standard deviation
df['Salary'].rolling(window=2).std()

# 230. rolling min/max | Rolling minimum and maximum
df['Salary'].rolling(window=2).min()
df['Salary'].rolling(window=2).max()

# 231. rolling custom function | Apply any function on rolling window
df['Salary'].rolling(window=2).apply(lambda x: x.max() - x.min())

# 232. expanding mean | Average of all values up to current row
df['Salary'].expanding().mean()

# 233. expanding sum | Cumulative sum using expanding window
df['Salary'].expanding().sum()

# 234. ewm (exponentially weighted mean) | Weighted moving average, recent values matter more
df['Salary'].ewm(span=3).mean()

# 235. ewm std | Exponentially weighted standard deviation
df['Salary'].ewm(span=3).std()


# ======================
# SECTION 14: DUPLICATES & SAMPLING
# ======================

# 236. duplicated check karna | Mark duplicate rows as True
df_dup = pd.DataFrame({'A': [1,2,2,3,3], 'B': ['x','y','y','z','z']})
df_dup.duplicated()

# 237. drop_duplicates | Remove all duplicate rows
df_dup.drop_duplicates()

# 238. keep last duplicate | Keep last occurrence, drop earlier duplicates
df_dup.drop_duplicates(keep='last')

# 239. subset pe duplicates | Find duplicates based on specific columns only
df_dup.drop_duplicates(subset=['A'])

# 240. sample lena (rows) | Randomly select N rows
df.sample(n=2)

# 241. sample fraction | Randomly select 50% of rows
df.sample(frac=0.5)

# 242. sample with seed | Random sample with fixed seed (reproducible)
df.sample(n=2, random_state=42)

# 243. take karna | Select rows by their positional integer locations
df.take([0, 2])


# ======================
# SECTION 15: ADVANCED OPERATIONS
# ======================

# 244. pipe karna | Chain custom functions on DataFrame
def add_bonus(df, pct=0.1):
    df = df.copy()
    df['Bonus'] = df['Salary'] * pct
    return df
df.pipe(add_bonus, pct=0.15)

# 245. agg / aggregate | Apply multiple aggregation functions at once
df[['Salary', 'Age']].agg(['mean', 'std', 'min', 'max'])

# 246. select_dtypes | Select columns by data type
df.select_dtypes(include='number')
df.select_dtypes(include='str')

# 247. filter rows/columns | Filter columns by name pattern
df.filter(like='a', axis=1)
df.filter(regex='^[NS]', axis=1)

# 248. reindex karna | Reindex to new index, fill missing with NaN
df.reindex([0, 1, 2, 3, 10, 11])

# 249. reindex_like | Reindex to match another DataFrame's shape
df2_reindexed = df.reindex_like(df.head(3))

# 250. add_prefix | Add a prefix string to all column names
df.add_prefix('col_')

# 251. add_suffix | Add a suffix string to all column names
df.add_suffix('_data')

# 252. equals karna | Check if two DataFrames are exactly equal
df.equals(df.copy())

# 253. memory_usage | Show memory used by each column in bytes
df.memory_usage()

# 254. infer_objects | Convert object columns to more specific types
df.infer_objects()

# 255. copy banana | Create a completely independent copy of DataFrame
df_copy = df.copy()

# 256. between_time | Filter rows between two times (for time-indexed df)
df_ts = pd.DataFrame(
    {'val': range(24)},
    index=pd.date_range('2024-01-01', periods=24, freq='h')
)
df_ts.between_time('08:00', '12:00')

# 257. at_time | Select rows at exact time (for time-indexed df)
df_ts.at_time('09:00')

# 258. first_valid_index | Get index of first non-NaN value
df_nan.first_valid_index()

# 259. last_valid_index | Get index of last non-NaN value
df_nan.last_valid_index()

# 260. truncate karna | Cut DataFrame before/after given index values
df.truncate(before=1, after=3)


# ======================
# SECTION 16: CATEGORICAL DATA
# ======================

# 261. Categorical dtype banana | Convert column to memory-efficient Categorical type
df['City'] = df['City'].astype('category')

# 262. cat.categories dekhna | View all category labels
df['City'].cat.categories

# 263. cat.codes dekhna | View integer code for each category
df['City'].cat.codes

# 264. cat.add_categories | Add new category without adding data
df['City'].cat.add_categories(['Hyderabad'])

# 265. cat.remove_categories | Remove a category label entirely
df['City'].cat.add_categories(['Hyderabad']).cat.remove_categories(['Hyderabad'])

# 266. cat.rename_categories | Rename existing category labels
df['City'].cat.rename_categories({'Delhi': 'New Delhi'})
df['City'] = df['City'].cat.rename_categories({'New Delhi': 'Delhi'})  # restore

# 267. cat.reorder_categories | Set a specific order for categories
df['City'].cat.reorder_categories(
    [c for c in ['Delhi','Mumbai','Chennai','Kolkata','Pune'] if c in df['City'].cat.categories]
)

# 268. cut karna | Divide continuous values into equal-width bins
pd.cut(df['Age'], bins=3)

# 269. cut with labels | Create bins with custom label names
pd.cut(df['Age'], bins=3, labels=['Young', 'Mid', 'Senior'])

# 270. qcut karna | Divide values into equal-frequency quantile bins
pd.qcut(df['Salary'], q=3, labels=['Low', 'Medium', 'High'])

# 271. factorize karna | Encode string labels as integer codes
codes, uniques = pd.factorize(df['City'])


# ======================
# SECTION 17: FILE I/O (READ & WRITE)
# ======================

# 272. CSV file save karna | Write DataFrame to CSV file
df.to_csv('/tmp/data.csv', index=False)

# 273. CSV file padhna | Read CSV file into DataFrame
df_csv = pd.read_csv('/tmp/data.csv')

# 274. CSV with separator | Read CSV using custom separator
df.to_csv('/tmp/data_sep.csv', sep='|', index=False)
pd.read_csv('/tmp/data_sep.csv', sep='|')

# 275. JSON save karna | Write DataFrame to JSON file
df.to_json('/tmp/data.json')

# 276. JSON padhna | Read JSON file into DataFrame
pd.read_json('/tmp/data.json')

# 277. Excel save karna | Write DataFrame to Excel file
df.to_excel('/tmp/data.xlsx', index=False)

# 278. Excel padhna | Read Excel file into DataFrame
pd.read_excel('/tmp/data.xlsx')

# 279. Pickle save karna | Save DataFrame as binary pickle (fast, preserves types)
df.to_pickle('/tmp/data.pkl')

# 280. Pickle padhna | Load DataFrame from pickle file
pd.read_pickle('/tmp/data.pkl')

# 281. HTML save karna | Convert DataFrame to HTML table string
df.to_html('/tmp/data.html', index=False)

# 282. to_dict karna | Convert DataFrame to Python dictionary
df.to_dict()

# 283. to_dict orient records | Convert to list of row dictionaries
df.to_dict(orient='records')

# 284. to_records karna | Convert DataFrame to NumPy record array
df.to_records()

# 285. to_numpy karna | Convert DataFrame values to NumPy array
df.to_numpy()

# 286. to_string karna | Convert DataFrame to formatted string
df.to_string()

# 287. to_markdown karna | Convert DataFrame to Markdown table string
df.to_markdown()

# 288. json_normalize karna | Flatten nested JSON/dict into DataFrame
nested = [{'id': 1, 'info': {'name': 'Rahul', 'city': 'Delhi'}},
          {'id': 2, 'info': {'name': 'Priya', 'city': 'Mumbai'}}]
pd.json_normalize(nested, sep='_')

# 289. read_table karna | Read any delimited text file
pd.read_table('/tmp/data_sep.csv', sep='|')


# ======================
# SECTION 18: MULTIINDEX
# ======================

# 290. MultiIndex banana | Create DataFrame with two-level row index
arrays = [['Delhi','Delhi','Mumbai','Mumbai'], ['Q1','Q2','Q1','Q2']]
idx = pd.MultiIndex.from_arrays(arrays, names=['City','Quarter'])
df_multi = pd.DataFrame({'Sales': [100,150,200,180], 'Cost': [80,120,160,140]}, index=idx)

# 291. MultiIndex from_tuples | Create MultiIndex from list of tuples
tuples = [('A',1),('A',2),('B',1),('B',2)]
pd.MultiIndex.from_tuples(tuples, names=['letter','number'])

# 292. MultiIndex from_product | Create MultiIndex from cartesian product
pd.MultiIndex.from_product([['A','B'],['x','y']], names=['alpha','greek'])

# 293. xs - cross section | Select data for one level value in MultiIndex
df_multi.xs('Delhi', level='City')

# 294. loc on MultiIndex | Select specific level combination
df_multi.loc['Delhi']

# 295. IndexSlice | Slice MultiIndex using pd.IndexSlice for clarity
idx_sl = pd.IndexSlice
df_multi.loc[idx_sl['Delhi', 'Q1'], :]

# 296. swaplevel MultiIndex | Swap the two index levels
df_multi.swaplevel()

# 297. sort_index MultiIndex | Sort MultiIndex for proper slicing
df_multi.sort_index()

# 298. reset_index MultiIndex | Convert MultiIndex levels back to columns
df_multi.reset_index()

# 299. stack MultiIndex | Stack column level into row MultiIndex
df_multi.stack()

# 300. unstack MultiIndex | Move inner row index to column MultiIndex
df_multi.unstack()


# ======================
# SECTION 19: RESAMPLING & TIME SERIES
# ======================

# 301. resample karna | Group time-series data by time frequency
df_daily = pd.DataFrame(
    {'value': range(30)},
    index=pd.date_range('2024-01-01', periods=30, freq='D')
)
df_daily.resample('W').mean()

# 302. resample sum | Weekly sum of daily data
df_daily.resample('W').sum()

# 303. resample OHLC | Open-High-Low-Close aggregation (for financial data)
df_daily.resample('W').ohlc()

# 304. asfreq karna | Change frequency, fill gaps with NaN or specific method
df_daily.resample('W').asfreq()

# 305. shift karna | Shift data forward or backward by N rows/periods
df['Salary'].shift(1)

# 306. shift backward | Shift data backward by 1 row
df['Salary'].shift(-1)

# 307. asof karna | Get most recent value up to given label (for sorted index)
s_ts = pd.Series([1,2,3], index=pd.to_datetime(['2024-01-01','2024-01-03','2024-01-05']))
s_ts.asof(pd.Timestamp('2024-01-04'))

# 308. bdate_range | Create range of business days only (no weekends)
pd.bdate_range(start='2024-01-01', end='2024-01-15')

# 309. interval_range | Create range of intervals (useful for binning)
pd.interval_range(start=0, end=10, periods=5)

# 310. to_timedelta | Convert string/numbers to timedelta objects
pd.to_timedelta(['1 day', '2 hours', '30 minutes'])

# 311. to_numeric karna | Convert column values to numeric, coerce errors to NaN
pd.to_numeric(['1', '2', 'abc', '4'], errors='coerce')


# ======================
# SECTION 20: ADVANCED & MISC
# ======================

# 312. eval karna (DataFrame level) | Evaluate expression using column names
df.eval('Salary * 0.9 + Score * 100')

# 313. mask karna | Replace values where condition is True with NaN or value
df[['Salary']].mask(df['Salary'] > 60000, other=60000)

# 314. where karna | Keep values where condition is True, replace rest with NaN
df[['Salary']].where(df['Salary'] > 50000)

# 315. lookup karna | Look up values by row and column labels
row_idx = [0, 1, 2]
col_lbl = ['Age', 'Salary', 'Score']
[df.at[r, c] for r, c in zip(row_idx, col_lbl)]  # manual lookup

# 316. style karna | Apply color/style formatting for display in notebooks
df.style.highlight_max(color='lightgreen')

# 317. pipe with style | Chain style operations
df.style.highlight_min(color='lightcoral').format({'Salary': '{:,.0f}'})

# 318. set_option | Change global pandas display settings
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20)

# 319. get_option | Read current value of pandas option
pd.get_option('display.max_columns')

# 320. describe_option | Print description of a pandas option
pd.describe_option('display.max_rows')

# 321. reset_option | Reset a pandas option back to default
pd.reset_option('display.max_columns')

# 322. option_context | Temporarily change option only inside this block
with pd.option_context('display.max_rows', 5):
    pass  # display with max 5 rows here

# 323. set_flags | Set immutable flags like allows_duplicate_labels
df.set_flags(allows_duplicate_labels=True)

# 324. flags dekhna | View current flags on DataFrame
df.flags

# 325. array method | Get underlying ExtensionArray of a column
df['City'].array

# 326. pd.array | Create pandas ExtensionArray from list
pd.array([1, 2, 3, pd.NA], dtype='Int64')

# 327. unique (top-level) | Get unique values from any array-like
pd.unique(df['City'])

# 328. factorize (top-level) | Encode values as integers (label encoding)
pd.factorize(pd.array(['Delhi','Mumbai','Delhi','Chennai']))

# 329. Timestamp banana | Create a single timestamp object
pd.Timestamp('2024-06-15 10:30:00')

# 330. DateOffset banana | Create a date offset (e.g., add 1 month)
pd.Timestamp('2024-01-31') + pd.DateOffset(months=1)

# 331. Period banana | Represent a time span (year, month, quarter etc.)
pd.Period('2024-Q1', freq='Q')

# 332. Interval banana | Represent a closed or open numeric/date interval
pd.Interval(0, 5, closed='right')

# 333. NA value | Pandas missing value (works with nullable integer/string)
pd.NA

# 334. NaT value | Missing value for datetime (Not a Time)
pd.NaT

# 335. show_versions | Print installed versions of pandas and dependencies
pd.show_versions()