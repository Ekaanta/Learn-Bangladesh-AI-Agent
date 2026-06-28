import pandas as pd

files = [
    "data/institutions.csv",
    "data/hospitals.csv",
    "data/restaurants.csv"
]

for file in files:
    print("=" * 80)
    print(file)

    df = pd.read_csv(file)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 3 Rows:")
    print(df.head(3))

    print("\n")