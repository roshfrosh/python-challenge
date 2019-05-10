import os
import csv

#Path to collect data 
budget_data = os.path.join('..', 'Resources','budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    data = list(csvreader)
    row_count = len(data)
    print(f"Total Number of Months: {str(row_count)}")