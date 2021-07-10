import csv
import pandas as pd
 
def read_using_DictReader(path):
    # opening the CSV file
    with open(path, mode ='r') as file:   
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       for lines in csvFile:
            return lines

def read_by_pandas_head():
    data=pd.read_csv('CSV_files/assets/addresses.csv')
    return data.head()       

def read_by_pandas_tail():
    data=pd.read_csv('CSV_files/assets/addresses.csv')
    return data.tail() 
  
if __name__=="__main__":
    print(read_using_DictReader('assets/addresses.csv'))
    print(read_using_DictReader())
    print(read_by_pandas_head())
    print(read_by_pandas_tail())

