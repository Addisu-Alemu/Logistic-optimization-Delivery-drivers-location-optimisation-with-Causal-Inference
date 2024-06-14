#create an empty structure model.import warnings

from causalnex.structure import StructureModel

warnings.filterwarnings("ignore")  # silence warnings

sm = StructureModel()


# import the dataset
import pandas as pd

data = pd.read_csv('../data/merged_result.csv')
data.head(5)

# choose non-numeric columns
import numpy as np

struct_data = data.copy()
non_numeric_columns = list(struct_data.select_dtypes(exclude=[np.number]).columns)

print(non_numeric_columns)

drop_col = ['trip_origin','trip_destination','trip_start_date','order_id']
data = data.drop(columns=drop_col)
data.head(5)
# Replace 'rejected' with 0 and 'accepted' with 1 in the 'driver_action' column
data['driver_action'] = data['driver_action'].replace({'rejected': 0, 'accepted': 1})

# Save the modified DataFrame to a new CSV file
data.to_csv("merged.csv", index=False)
data = pd.read_csv('../data/merged.csv')
data.head(5)

 #  use label encoding non-numeric variables to make data numeric
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in non_numeric_columns:
    struct_data[col] = le.fit_transform(struct_data[col])

struct_data.head(5)
import pandas as pd
import numpy as np

# Impute NaN with column means
for col in struct_data.columns:
    if struct_data[col].isnull().any():
        mean_value = struct_data[col].mean()
        struct_data[col].fillna(mean_value, inplace=True)

#apply the NOTEARS algorithm to learn the structure.

from causalnex.structure.notears import from_pandas
sm = from_pandas(struct_data)