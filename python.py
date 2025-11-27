import pandas as pd

# Ask the user for file name
file_name = input("Enter CSV file name: ")

# Read the CSV file
try:
    df = pd.read_csv(file_name)
    print("\nCSV File Data:")
    print(df)

except FileNotFoundError:
    print("❌ File not found. Please check the file name.")

print(df["home_team"])

print(df[df["home_score"]>8])

print(df[df["tournament"]!="Friendly"])

print(df[df["date"]>"2025-10-13"])

print(df[df["country"]=="japan"])
