import requests
from bs4 import BeautifulSoup

number = input("Enter the phone number: ")
url = f'https://mobilenumbertracker.com/mobilenumberlocation/{number[:4]}'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    for i, paragraph in enumerate(paragraphs[:3]):
        print(f"{paragraph.get_text()}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
