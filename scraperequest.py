
import requests
from bs4 import BeautifulSoup

# Function to scrape with plain requests library and BeautifulSoup
def scrapeWithRequests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

url = 'https://housevia.com/search-result-page/?status%5B%5D=&states%5B%5D=&location%5B%5D=&type%5B%5D=for-rent&bedrooms=&bathrooms=&min-price=&max-price='

soup = scrapeWithRequests(url)


# Modify as per your target element
houses = soup.find_all('div', class_='item-wrap')


houses = []

for title in houses:
    price = title.find('li', class_="item-price").text.strip()
    if price:
        print(price)
    title = title.find('h2', class_='item-title').text.strip()
    if title:
        print(title)
    houses.append({
        'title': title,
        'price': price
    })

print(houses)