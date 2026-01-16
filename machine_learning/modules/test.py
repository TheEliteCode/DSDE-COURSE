'''import sqlite3

# Absolute path to your database file
db_path = r"C:\Users\davod\OneDrive\Desktop\DSDE COURSE\machine_learning\modules\Maji_Ndogo_farm_survey_small.db"

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # List all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("The database exists but contains no tables.")
    
    conn.close()
except sqlite3.DatabaseError as e:
    print("Error: This file is not a valid SQLite database.")
    print("Details:", e) '''


import sqlite3
import pandas as pd

# --- Step 1: Set the path to your new database (raw string to avoid Unicode errors) ---
db_path = r"C:\Users\davod\OneDrive\Desktop\DSDE COURSE\machine_learning\modules\Maji_Ndogo_farm_survey_small.db"

# Connect to (or create) the database
conn = sqlite3.connect(db_path)
print(f"Database created at: {db_path}")

# --- Step 2: Define CSV URLs from Explore-AI repo ---
csv_files = {
    "geographic_features": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/geographic_features.csv",
    "weather_features": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/weather_features.csv",
    "soil_and_crop_features": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/soil_and_crop_features.csv",
    "farm_management_features": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/farm_management_features.csv"
}

# --- Step 3: Download CSVs and write them into the database ---
for table_name, csv_url in csv_files.items():
    print(f"Processing {table_name}...")
    df = pd.read_csv(csv_url)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded table: {table_name} ({len(df)} rows)")

# Close the connection
conn.close()
print("Database created and all tables loaded successfully!")
