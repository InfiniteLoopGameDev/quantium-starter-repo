import csv

pink_morsel = []

for i in range(3):  # Iterate through all 3 files
    with open(f"data/daily_sales_data_{i}.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:  # Iterate through each row
            if row[0] == "pink morsel":  # Check if the row is for pink morsel
                formatted_row = []
                formatted_row.append(row[4])  # Append date
                formatted_row.append(row[3])  # Append region
                sales = float(row[1].strip("$")) * int(row[2])  # Calculate sales
                formatted_row.append(f"${sales}")  # Append sales
                pink_morsel.append(formatted_row)

with open("data/pink_morsel.csv", "w") as csvfile:  # Create new file
    fieldnames = ["date", "region", "sales"]
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(fieldnames)  # Write header
    writer.writerows(pink_morsel)  # Write data
