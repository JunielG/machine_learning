from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

# Option 1: Encode each column separately (recommended)
encoded_columns = {}
columns_to_encode = ['State_gov', 'Bachelors', 'Never_married', 'Adm_clerical', 
                     'Not_in_family', 'Race', 'Gender', 'Country']

for col in columns_to_encode:
    encoded_columns[col] = le.fit_transform(df2[col])

# Create a new dataframe with encoded values
enc_df = pd.DataFrame(encoded_columns)

# Option 2: If you want to encode multiple columns at once
# You'll need to use a different approach since LabelEncoder works on 1D arrays
from sklearn.preprocessing import LabelEncoder
import pandas as pd

le_dict = {}
enc_df = df2[columns_to_encode].copy()

for col in columns_to_encode:
    le_dict[col] = LabelEncoder()
    enc_df[col] = le_dict[col].fit_transform(df2[col])