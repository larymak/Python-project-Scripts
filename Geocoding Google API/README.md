## HOW TO USE:
1. Simply just grab an api key from the google maps api/geocode.
2. Create an excel workbook with a name of your choosing.
3. Create a sheet name in this excel workbook with a name of your choosing.
4a. Create a column labeled address where your addresses will be listed
4b. If you want to label your column something else, you can do so, but make sure to change it in the geo.py file
5. The program will then grab each address and convert it to fit the url format and then fetch the corresponding latitude 
& longitutde to be returned
6. It will be then outputed to a new excel file called output and saved.

'''
'''
if there is an error in retrieving the lat or long, the program
will instead put a 0,0. this is because the program doesn't account for errors on the request 
of which it responds with a 200 success, but results in an index out of bounds error 
because the return specifies the api key is wrong yet it is right.
for the few entries this problem occurs it can be done manually or programmed further to account for

