# Introduction

This Python program is a web scraper that extracts data about graphics cards from a specific website. It uses the BeautifulSoup library to parse the HTML content of the website and requests library to fetch the web page.

## Requirements

- Python 3.x
- BeautifulSoup library (`beautifulsoup4`)
- Requests library (`requests`)
- Openpyxl library (`openpyxl`)

You can install the required libraries using pip:

```
pip install beautifulsoup4 requests openpyxl
```

## How to Use

1. Clone this repository or download the files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the Python script `app.py`:

```
app.py
```

4. The program will start scraping data from the website and display the brand, name, and price of each graphics card on the console.

5. Once the scraping is complete, the program will save the data to an Excel file named `Graphics Card.xlsx`.

## Configuration

You can modify the URL in the `scrape_graphics_cards_data()` function inside the `app.py` file to scrape data from a different website or adjust the parameters as needed.

## Output

The program will generate an Excel file `Graphics Card.xlsx` containing the scraped data. Each row in the Excel file represents a graphics card and includes the columns `Brand`, `Name`, and `Price`.

## Disclaimer

This web scraper is provided for educational and informational purposes only. Please be respectful of the website's terms of service and scraping policies. Always obtain proper authorization before scraping any website, and use the scraper responsibly and ethically.
