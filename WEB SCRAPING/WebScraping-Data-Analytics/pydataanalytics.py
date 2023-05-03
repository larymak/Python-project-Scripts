import csv
import requests 
from bs4 import BeautifulSoup

#Url to the jobsite (using tottal job as an examples)
url =  'https://www.totaljobs.com/jobs/in-london'

r = requests.get(url)

# parsing the html to beautiful soup
html_soup= BeautifulSoup(r.content, 'html.parser')

# Targeting the jobs container
job_details = html_soup.find('div', class_='ResultsContainer-sc-1rtv0xy-2')

# Pulling out the needed tags
job_titles =job_details.find_all(['h2','li','dl'])
company_name =job_details.find_all('div', class_='sc-fzoiQi')

total_job_info = job_titles + company_name

# Writing the data to a CSV file
with open('job_data_2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Location', 'Salary', 'Company Name']) # header row
    for i in range(0, len(job_titles), 3):
        job_title = job_titles[i].text.strip()
        location = job_titles[i+1].text.strip()
        salary = job_titles[i+2].text.strip()
        company = company_name[i//3].text.strip()
        writer.writerow([job_title, location, salary, company])
        print(job_title)
