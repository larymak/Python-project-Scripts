# Author: Asib Hossen
# Date: May 20, 2024
# Description: This script scrapes job listings from a website based on user input,
#              displays the job details, and optionally saves them as CSV and/or TXT files.
# Version: 1.0

import os
import re
import csv
import time
import requests
from bs4 import BeautifulSoup

def get_user_input():
    """
    Prompt user for job title, remote job preference, sorting preference,
    and save option.

    Returns:
        tuple: A tuple containing job title (str), remote job preference (bool),
               save option (str), and sorting preference (str).
    """
    job = input("Enter the job title: ")
    remote = input("Do you want remote jobs only? (yes/no): ").lower() == 'yes'
    sort_options = ['matches', 'newest', 'salary']
    print(f"Sort options: {sort_options}")
    sort_by = input("Enter the sorting preference (matches/newest/salary): ")
    save_option = input("Do you want to save the output as CSV, TXT, or both of them? (csv/txt/both): ").lower()
    return job, remote, save_option, sort_by

def construct_url(job, remote, sort_by):
    """
    Construct the URL based on the job title, remote preference, and sorting preference.

    Args:
        job (str): The job title.
        remote (bool): True if user wants remote jobs only, False otherwise.
        sort_by (str): The sorting preference.

    Returns:
        str: The constructed URL.
    """
    base_url = "https://www.devjobsscanner.com/search/"
    search_params = f"?search={job}"
    if remote is not None:
        search_params += f"&remote={str(remote).lower()}"
    if sort_by is not None:
        search_params += f"&sort={sort_by}"
    url = base_url + search_params
    return url

def scrape_jobs(url):
    """
    Scrape job listings from the provided URL.

    Args:
        url (str): The URL to scrape job listings from.

    Returns:
        list: A list of dictionaries containing job details.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        time.sleep(5)  # Delay to avoid hitting the server too frequently
        soup = BeautifulSoup(response.content, 'html.parser')

        job_divs = soup.find_all('div', class_='flex p-3 rounded group relative overflow-hidden')
        jobs = []
        for job_div in job_divs:
            title = job_div.find('h2').text.strip()
            company = job_div.find('div', class_='jbs-dot-separeted-list').find('a').text.strip()
            tags = [tag.text.strip() for tag in job_div.find_all('a', class_='tag')]
            date_posted = job_div.find('span', class_='text-primary-text').text.strip()
            salary = job_div.find('span', class_='text-gray-text').text.strip()

            # Check if the salary contains at least two digits
            if not re.search(r'\d{2}', salary):
                salary = "Not mentioned"

            job_url = job_div.find('a', class_='jbs-text-hover-link')['href']

            jobs.append({
                'title': title,
                'company': company,
                'company_url': f"https://www.devjobsscanner.com/company/{company.lower()}",
                'tags': tags,
                'date_posted': date_posted,
                'salary': salary,
                'job_url': job_url
            })
        return jobs
    except requests.RequestException as e:
        print("Error scraping jobs:", e)
        return []

def display_jobs(jobs):
    """
    Display job details to the console.

    Args:
        jobs (list): A list of dictionaries containing job details.
    """
    for job in jobs:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Company URL: {job['company_url']}")
        print(f"Tags: {', '.join(job['tags'])}")
        print(f"Date Posted: {job['date_posted']}")
        print(f"Salary: {job['salary']}")
        print(f"Job URL: {job['job_url']}")
        print("-" * 40)

def save_as_csv(jobs, filename):
    """
    Save job details as CSV file.

    Args:
        jobs (list): A list of dictionaries containing job details.
        filename (str): The name of the CSV file to save.
    """
    output_dir = os.path.join(os.getcwd(), "outputFiles")
    os.makedirs(output_dir, exist_ok=True)
    keys = jobs[0].keys()
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(jobs)
    except IOError as e:
        print("Error saving as CSV:", e)

def save_as_txt(jobs, filename):
    """
    Save job details as text file.

    Args:
        jobs (list): A list of dictionaries containing job details.
        filename (str): The name of the text file to save.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as output_file:
            for job in jobs:
                output_file.write(f"Title: {job['title']}\n")
                output_file.write(f"Company: {job['company']}\n")
                output_file.write(f"Company URL: {job['company_url']}\n")
                output_file.write(f"Tags: {', '.join(job['tags'])}\n")
                output_file.write(f"Date Posted: {job['date_posted']}\n")
                output_file.write(f"Salary: {job['salary']}\n")
                output_file.write(f"Job URL: {job['job_url']}\n")
                output_file.write("-" * 40 + "\n")
    except IOError as e:
        print("Error saving as TXT:", e)

if __name__ == '__main__':
    job, remote, save_option, sort_by = get_user_input()
    url = construct_url(job, remote, sort_by)
    print(f"Scraping URL: {url}")
    jobs = scrape_jobs(url)
    if jobs:
        display_jobs(jobs)
        fileName = f"./outputFiles/{job}_jobs_remote_{str(remote).lower()}_sorted_by_{sort_by}"
        if save_option == 'csv':
            save_as_csv(jobs, f"{fileName}.csv")
        elif save_option == 'txt':
            save_as_txt(jobs, f"{fileName}.txt")
        elif save_option == 'both':
            save_as_csv(jobs, f"{fileName}.csv")
            save_as_txt(jobs, f"{fileName}.txt")
        print(f"Jobs saved as {save_option.upper()} file(s).")
    else:
        print("No jobs found. Exiting.")
