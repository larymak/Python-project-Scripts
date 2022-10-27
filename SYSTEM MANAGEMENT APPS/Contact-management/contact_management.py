from prettytable import PrettyTable
import sqlite3
import os
os.chdir('E:\project')
#--------------------------------------------------
my_database = sqlite3.connect('contact.db')
try: 
    my_database.execute('select * from contact')
except:
    my_database.execute('''CREATE TABLE CONTACT
         (NAME          char(30)   primary key  NOT NULL,
         Phone_no       INT   NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL_ID       CHAR(50));''')
#--------------------------------------------------------
#print(my_database.execute('select * from contact'))
class contacts:
    Name = str()
    Mobile_no = str()
    Address = str()
    Email = str()
    def __init__(self):#constructor used for declaring variable
       self.Name =  ''
       self.Mobile_no = ''
       self.Address =''
       self.Email = ''
    def show_table_format(self,contact_detail):
        myview = PrettyTable(['Name','Phone no.','Address','Email Id'])
        data = []
        for i in contact_detail:
            data.append(i)
        if(not data):
            print('oops no data found !!! :(')
            return
        myview.add_rows(data)
        print(myview)
        return

    def Add_contact(self):
        self.Name = input('Enter the name: ')
        self.Mobile_no = input('Enter the number: ')
        self.Address = input('Enter the address: ')
        self.Email = input('Enter the email: ')

        my_database.execute('Insert into contact values("{}","{}","{}","{}")'.format(self.Name,self.Mobile_no,self.Address,self.Email))
        my_database.commit()
        print('Data saved succesfully')
        return

    def show_contacts(self):
        contact_detail = my_database.execute('select * from contact')
        self.show_table_format(contact_detail)
       
    def Edit_contacts(self):
        self.Delete_contacts()
        self.Add_contact()
    def Delete_contacts(self):
        delete_name = input('Enter the name of contact to edit/delete: ')

        my_database.execute('Delete from contact where NAME = "{}" COLLATE NOCASE'.format(delete_name))
        my_database.commit()
        print('Data deleted succefully')

    def search_contacts(self):
        search_name = input('Enter the name of contact to search: ')
        data =  my_database.execute("select * from contact where name = '{}' COLLATE NOCASE".format(search_name))
        self.show_table_format(data)

def start_up():
    print(' '*15,'1. Press a to add new contact')
    print(' '*15,'2. Press s to show contacts')
    print(' '*15,'3. Press e to edit contacts')
    print(' '*15,'4. Press d to delete contacts')
    print(' '*15,'5. Press g to search contacts')

if __name__ == "__main__":
    person = contacts()
    print('----------------:Welcome to contact list management system:-------------')
    
    answer = 'y'
    while answer in ['y','Y']:
        start_up()
        choice = input('Enter your choice: ')
        if choice in ['a','A']:
            person.Add_contact()
        elif choice in ['s','S']:
            person.show_contacts()
        elif choice in ['e','E']:
            person.Edit_contacts()
        elif choice in ['d','D']:
            person.Delete_contacts()
        elif choice in ['g','G']:
            person.search_contacts()
        else:
            print('oops invalid choice !!! ')
        answer = input('Want to perform more operation y/n !!')
    print('Programme closed succesfully')




    