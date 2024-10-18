import pandas as pd

dataset = pd.read_csv("dataset.csv")

# Print out the dataset
# for index, row in dataset.iterrows():
#     print(f"Row: {row}, Index: {index}")

# # Print a  column
# for row in dataset["Device Model"]:
#     print(f"Row: {row}")

#Print just a row
for row in dataset.iterrows():
    print(f"Row: {row}")