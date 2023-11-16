from bs4 import BeautifulSoup
import requests
import openpyxl


def extract_brand_name_and_title(name):
    # Split the name and return the first word as the brand name and the rest as title
    brand, title = name.split(' ', 1)
    return brand, title


def scrape_graphics_cards_data():
    try:
        # Create a new Excel workbook and set up the worksheet
        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = "price"
        sheet.append(['Brand', 'Name', 'Price'])

        url = 'https://www.techlandbd.com/pc-components/graphics-card?sort=p.price&order=ASC&fq=1&limit=100'
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all product cards on the webpage
        cards = soup.find('div', class_='main-products product-grid').find_all(
            'div', class_='product-layout has-extra-button')

        for card in cards:
            # Extract the product name
            name = card.find('div', class_='name').a.text

            # Split the name to get the brand and title
            brand, title = extract_brand_name_and_title(name)

            # Extract the product price
            price = card.find('div', class_='price').span.text

            # Print the product details and add them to the Excel sheet
            print(brand, title, price)
            sheet.append([brand, title, price])

        # Save the Excel file
        excel.save('Graphics Card.xlsx')

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    # Call the main scraping function
    scrape_graphics_cards_data()
