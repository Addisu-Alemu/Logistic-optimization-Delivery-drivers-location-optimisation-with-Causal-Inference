import warnings
from causalnex.structure import StructureModel
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from causalnex.structure.notears import from_pandas

def create_structure_model(data_path):
  """
  Creates a causal structure model using the NOTEARS algorithm.

  Args:
      data_path (str): Path to the CSV file containing the data.

  Returns:
      StructureModel: The learned causal structure model.
  """

  warnings.filterwarnings("ignore")  # silence warnings

  sm = StructureModel()

  # Import the dataset
  data = pd.read_csv(data_path)

  # Choose non-numeric columns
  non_numeric_columns = list(data.select_dtypes(exclude=[np.number]).columns)

  # Drop irrelevant columns
  drop_col = ['trip_origin', 'trip_destination', 'trip_start_date', 'order_id']
  data = data.drop(columns=drop_col)

  # Replace 'rejected' with 0 and 'accepted' with 1 in the 'driver_action' column
  data['driver_action'] = data['driver_action'].replace({'rejected': 0, 'accepted': 1})

  # Save the modified DataFrame to a new CSV file
  data.to_csv("merged.csv", index=False)
  data = pd.read_csv('../data/merged.csv')

  # Use label encoding for non-numeric variables
  struct_data = data.copy()
  le = LabelEncoder()
  for col in non_numeric_columns:
    struct_data[col] = le.fit_transform(struct_data[col])

  # Impute NaN with column means
  for col in struct_data.columns:
    if struct_data[col].isnull().any():
      mean_value = struct_data[col].mean()
      struct_data[col].fillna(mean_value, inplace=True)

  # Apply the NOTEARS algorithm to learn the structure
  sm = from_pandas(struct_data)

  return sm