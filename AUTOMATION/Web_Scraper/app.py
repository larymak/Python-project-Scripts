from bs4 import BeautifulSoup
import requests
import openpyxl

def extract_brand_name_and_title(name):
    brand, title = name.split(' ', 1)
    return brand, title

def get_page_content(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', class_='main-products product-grid').find_all(
        'div', class_='product-layout has-extra-button')

def write_to_excel(cards, file_path):
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "price"
    sheet.append(['Brand', 'Name', 'Price'])

    for card in cards:
        name = card.find('div', class_='name').a.text
        brand, title = extract_brand_name_and_title(name)
        price = card.find('div', class_='price').span.text
        sheet.append([brand, title, price])

    with open(file_path, 'wb') as f:
        excel.save(f)

def scrape_graphics_cards_data(file_path='Graphics Card.xlsx'):
    try:
        url = 'https://www.techlandbd.com/pc-components/graphics-card?sort=p.price&order=ASC&fq=1&limit=100'
        html = get_page_content(url)
        cards = parse_html(html)
        write_to_excel(cards, file_path)

    except requests.RequestException as e:
        print("Network error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    scrape_graphics_cards_data()

