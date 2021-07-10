import csv
import pandas as pd
 
def read_using_DictReader():
    # opening the CSV file
    with open('CSV_files/assets/addresses.csv', mode ='r') as file:   
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       for lines in csvFile:
            return lines

def read_by_pandas():
    data=pd.read_csv('CSV_files/assets/addresses.csv')
    return data.head()       

if __name__=="__main__":
    print(read_using_DictReader())
    print(read_by_pandas())