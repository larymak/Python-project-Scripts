import csv
import pandas as pd
 
def read_using_DictReader(path):
    # opening the CSV file
    with open(path, mode ='r') as file:   
       # reading the CSV file
       csvFile = csv.DictReader(file)
       main_dic=[]
       # displaying the contents of the CSV file
       for lines in csvFile:
           main_dic.append(lines)
       return main_dic

#retrun the top 5 rows in CSV file
def read_by_pandas_head(path):
    data=pd.read_csv(path)
    return data.head()       


#retrun the bottom 5 rows in CSV file
def read_by_pandas_tail(path):
    data=pd.read_csv(path)
    return data.tail() 
  
if __name__=="__main__":
    
    path='./assets/addresses.csv'
    print(read_using_DictReader(path))
    print(read_by_pandas_head(path))
    print(read_by_pandas_tail(path))

