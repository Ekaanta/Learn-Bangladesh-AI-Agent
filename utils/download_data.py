from datasets import load_dataset
import os

# Create data directory 
os.makedirs("data", exist_ok=True)

datasets_info = [
    (
        "Mahadih534/Institutional-Information-of-Bangladesh",
        "institutions.csv",
    ),
    (
        "Mahadih534/all-bangladeshi-hospitals",
        "hospitals.csv",
    ),
    (
        "Mahadih534/Bangladeshi-Restaurant-Data",
        "restaurants.csv",
    ),
]

for dataset_name, output_file in datasets_info:
    print(f"Downloading {dataset_name}...")

    dataset = load_dataset(dataset_name)

    dataset["train"].to_csv(
        os.path.join("data", output_file),
        index=False,
    )

    print(f"Saved: data/{output_file}")

print("\nAll datasets downloaded successfully!")