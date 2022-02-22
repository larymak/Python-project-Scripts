import pandas as pd
import requests
import openpyxl
from requests.models import HTTPError
import xlsxwriter
'''
HOW TO USE:
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


'''
my_new_data = []

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

# editable
COLUMN_IDX_START = 10  # -> corresponds to the latitude column
COLUMN_IDX_START_2 = 11  # -> corresponds to the longitude column
WORKBOOK_NAME = 'YOURWORKBOOKNAMEHERE.xlsx'
SHEET_NAME = 'YOURSHEETNAMEHERE'
COLUMN_NAME = 'address'
MAPS_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='
GOOGLE_API_KEY = 'YOURAPI_KEY HERE'
API_KEY = '&key=' + GOOGLE_API_KEY


def getGeoCodeFromAddress():
    wb = openpyxl.load_workbook(WORKBOOK_NAME)
    ws = wb[SHEET_NAME]
    excel_data_df = pd.read_excel(WORKBOOK_NAME, sheet_name=SHEET_NAME)
    list_data = excel_data_df[COLUMN_NAME].tolist()
    for address in list_data:
        sanitized_add = address.replace(" ", "+")
        my_new_data.append(sanitized_add)
    for row_num, data in enumerate(my_new_data, start=1):
        try:
            lat, long = getLatAndLong(data)
        except:
            lat, long = 0, 0
        worksheet.write(row_num, COLUMN_IDX_START, lat)
        worksheet.write(row_num, COLUMN_IDX_START_2, long)
    workbook.close()


def getLatAndLong(url):
    url = MAPS_URL + url + API_KEY
    try:
        response = requests.get(url)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

    json_response = response.json()
    data = json_response['results'][0]['geometry']['location']
    latitude = data['lat']
    longitutde = data['lng']
    # print(str(latitude) + 'lat')
    # print(str(longitutde) + 'long')
    return latitude, longitutde


getGeoCodeFromAddress()