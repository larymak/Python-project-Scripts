import csv
import pandas as pd


 

def write_to_csv_files_using_DictWriter_class(data,fields,filename):
   
    with open(filename, 'w') as csvfile: 
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
            
        # writing headers (field names) 
        writer.writeheader() 
            
        # writing data rows 
        writer.writerows(data) 

def write_by_pandas(name_dict):
        df = pd.DataFrame(name_dict)
        return df

if __name__=="__main__":
     # my data rows as dictionary objects 
    mydata =[{'name': 'Noura', 'course': 'python40python401'}, 
            {'name': 'Mahmoud', 'course': 'python401'}, 
            {'name': 'Nizar', 'course': 'python401'}, 
            {'name': 'Raneem', 'course': 'python401'}, 
            {'name': 'Omer', 'course': 'python401'}, ] 
        
    # field names 
    fields = ['name','course'] 
        
    # name of csv file 
    filename = "assets/course_name.csv"
        
    # writing to csv file 
    print(write_to_csv_files_using_DictWriter_class(mydata,fields,filename))


    name_dict = {
        'Name': ['Omar','Mahmoud','Noura','Raneem'],
        'Score': [82,86,84,65]
        }
    print(write_by_pandas(name_dict))