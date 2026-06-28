import sqlite3
import pandas as pd
import os

os.makedirs("databases", exist_ok=True)


# Institutions Database
institutions = pd.read_csv("data/institutions.csv")

institutions = institutions.rename(columns={
    "INSTITUTE NAME": "name",
    "EIIN": "eiin",
    "INSTITUTE_TYPE": "institution_type",
    "DIVISION_ID": "division_id",
    "DIVISION": "division",
    "DISTRICT_ID": "district_id",
    "DISTRICT": "district",
    "THANA_ID": "thana_id",
    "THANA": "thana",
    "UNION_ID": "union_id",
    "UNION_NAME": "union_name",
    "MAUZA_ID": "mauza_id",
    "MAUZA_NAME": "mauza_name",
    "AREA_STATUS": "area_status",
    "GEOGRPYCAL_STATUS": "geographical_status",
    "ADDRESS": "address",
    "POST": "post",
    "MANAGEMENT_TYPE": "management_type",
    "MOBILE": "mobile",
    "STUDENT_TYPE": "student_type",
    "EDUCATION_LEVEL": "education_level",
    "AFFILIATION": "affiliation",
    "MPO_STATUS": "mpo_status"
})

conn = sqlite3.connect("databases/institutions.db")
institutions.to_sql(
    "institutions",
    conn,
    if_exists="replace",
    index=False
)
conn.close()

print("✓ institutions.db created")



# Hospitals Database
hospitals = pd.read_csv("data/hospitals.csv")

hospitals = hospitals.rename(columns={
    "Id": "id",
    "Name": "name",
    "Name (Bangla)": "name_bangla",
    "Code": "code",
    "Agency": "agency",
    "Type": "type",
    "Division": "division",
    "District": "district",
    "City Corporation": "city_corporation",
    "Upazila": "upazila",
    "Paurasava": "paurasava",
    "Union": "union_name",
    "Private": "private"
})

conn = sqlite3.connect("databases/hospitals.db")
hospitals.to_sql(
    "hospitals",
    conn,
    if_exists="replace",
    index=False
)
conn.close()

print("✓ hospitals.db created")


# Restaurants Database
restaurants = pd.read_csv("data/restaurants.csv")

restaurants = restaurants.rename(columns={
    "place_id": "place_id",
    "name": "name",
    "latitude": "latitude",
    "longitude": "longitude",
    "rating": "rating",
    "number_of_reviews": "number_of_reviews",
    "affluence": "affluence",
    "address": "address"
})

conn = sqlite3.connect("databases/restaurants.db")
restaurants.to_sql(
    "restaurants",
    conn,
    if_exists="replace",
    index=False
)
conn.close()

print("✓ restaurants.db created")

print("\nAll databases created successfully.")