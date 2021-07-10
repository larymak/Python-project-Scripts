import csv
 
def read_using_DictReader():
    # opening the CSV file
    with open('CSV_files/assets/addresses.csv', mode ='r') as file:   
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       for lines in csvFile:
            return lines


            

if __name__=="__main__":
    print(read_using_DictReader())