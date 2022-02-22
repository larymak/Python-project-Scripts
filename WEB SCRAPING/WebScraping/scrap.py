from bs4 import BeautifulSoup
import requests
import time

print('Please Enter Skills You are not familiar with')
unfamiliar_skill = input(' > ')
print(f'Filtering Out {unfamiliar_skill}')

def find_jobs():
     html_text = requests.get(' https://www.myjobmag.co.ke/search/jobs?q=python ').text
     soup = BeautifulSoup( html_text, 'lxml' )
     jobs = soup.find_all('li', class_ = 'job-list-li')
     for index, job in enumerate(jobs):
          published_date = job.find('li', class_ = 'job-item')
          company_name = job.find('h2').text.replace('  ', '  ')
          skills = job.find('li', class_ = 'job-desc').text.replace('  ', '  ')
          more_info = job.h2.a['href']
          if unfamiliar_skill not in skills:
               with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
               print('File Save Succesfully: {index}')

if __name__ == "__main__":
     while True:
          find_jobs()
          time.sleep(600)