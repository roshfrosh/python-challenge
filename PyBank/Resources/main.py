import os
import csv

#Path to collect data 
budget_data = os.path.join('..', 'Resources','budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
#Count the number of months 
    num_months = list(csvreader)
    months = len(num_months)
    print(f"Total Number of Months: {str(months)}")
#total loss/profits
    #total = 0
    #for row in csvreader:
       # _total = row[1]
       # try:
       #     _total = float(_total)
       ## except ValueError:
           # _total = 0
       # total += _total
       
    #print(f'Total: $ {str(total)}')
    #total = 0
    
#for row in csvreader:
   
        #total += int(row[1])
    #print (total) 
for num in csvreader[1]:
    if num >= 0:
        profits = sum(num)
     
    if num < 0:
        losses = sum(num)
print (profits)
print (losses)
