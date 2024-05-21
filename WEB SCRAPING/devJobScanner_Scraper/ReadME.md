# devJobScanner Job Scraper

## Description
This repository contains two scripts designed to scrape job listings from a specified website. Users can input their desired job title, remote work preference, sorting preference, and choose how to save the output (CSV, TXT, or both).

## Scripts

### Script 1: `job_scraper_static.py`
- Scrapes job listings using the `requests` library and `BeautifulSoup`.
- Displays job details in the console.
- Saves job details in CSV and/or TXT format.
- Suitable for static page scraping.

### Script 2: `job_scraper_dynamic.py`
- Enhanced to use `SeleniumBase` for dynamic page interaction.
- Supports infinite scrolling to load more job listings.
- Users can specify the number of job listings to scrape.
- More robust handling of dynamically loaded content.

## Requirements

### Common Requirements
- Python 3.x
- `beautifulsoup4` library
- `requests` library

### Dynamic Script Additional Requirements
- `seleniumbase` library
- WebDriver for your browser (e.g., ChromeDriver for Chrome)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/asibhossen897/devJobsScanner-job-scraper.git
    cd devJobsScanner-job-scraper
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. For `job_scraper_dynamic.py`, ensure you have the appropriate WebDriver installed and available in your PATH.

## Usage

### Static Scraper (`job_scraper_static.py`)
1. Run the script:
    ```bash
    python job_scraper_static.py
    ```
    (**If ```python``` does not work, use ```python3```**)

2. Follow the prompts to input your job search criteria and preferences.

### Dynamic Scraper (`job_scraper_dynamic.py`)
1. Run the script:
    ```bash
    python job_scraper_dynamic.py
    ```
    (**If ```python``` does not work, use ```python3```**)

2. Follow the prompts to input your job search criteria, number of jobs to scrape, and preferences.

## File Structure
- `job_scraper_static.py`: Script for static job scraping.
- `job_scraper_dynamic.py`: Script for dynamic job scraping with SeleniumBase.
- `requirements.txt`: List of required Python libraries.
- `outputFiles/`: Directory where output files (CSV, TXT) are saved.

## Disclaimer
These scripts are for educational and personal use only. Scraping websites can be against the terms of service of the website being scraped. Always check the website’s terms and conditions before scraping any content. The author is not responsible for any misuse of these scripts. Use at your own risk.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Asib Hossen

## Date
May 21, 2024
