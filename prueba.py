import csv
import random

# Define possible districts in Madrid
districts = [
    "Chamberí", "Salamanca", "Arganzuela", "Moncloa-Aravaca", 
    "Retiro", "Centro", "Chamartín", "Tetuán", 
    "Fuencarral-El Pardo", "Carabanchel"
]

# Open a CSV file for writing
with open("madrid_housing_1000.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    writer.writerow(["Price", "Year_of_Building", "Square_Meters", "District"])
    
    # Generate 1000 rows of data
    for _ in range(1000):
        price = random.randint(200000, 800000)
        year = random.randint(1900, 2020)
        area = random.randint(50, 200)
        district = random.choice(districts)
        writer.writerow([price, year, area, district])

print("CSV file 'madrid_housing_1000.csv' with 1,000 rows has been created.")
