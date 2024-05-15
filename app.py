import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website
url = 'https://es.wikipedia.org/wiki/Kobe_Bryant'

# Get the HTML of the website
response = requests.get(url)

# Create a BeautifulSoup object with the HTML of the website
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('a')

for result in results:
    if 'href' in result.attrs:
        # Verificar si el enlace tiene una URL completa
        if result['href'].startswith('http'):
            full_url = result['href']
        else:
            # Unir la URL base con el href del elemento
            full_url = urljoin(url, result['href'])
            
        # Realizar la solicitud solo si es una URL completa
        response2 = requests.get(full_url)
        
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        
        results2 = soup2.find_all(['h1','p'])
        
        print(results2)
    else:
        print("No 'href' attribute found.")
