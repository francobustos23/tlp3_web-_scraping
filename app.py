import requests
from bs4 import BeautifulSoup
import json

# URL of the website
url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

# Get the HTML of the website
response = requests.get(url)

# Create a BeautifulSoup object with the HTML of the website
soup = BeautifulSoup(response.text, 'html.parser')

# Find all relevant links
results = soup.find_all('a', class_='splinter-link main-slider-item')

# Dictionary to store the data
data = {}

# Iterate over each link
for result in results:
    # Get the URL of the link
    a_url = result['href']

    # Get the HTML of the link
    response2 = requests.get(a_url)

    # Create a BeautifulSoup object with the HTML of the link
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    
    # Find all h1 and p elements
    results2 = soup2.find_all(['h1', 'p'])
    
    # Extract text content from the results2 
    # and convert it to a string to keep the element labels 
    extracted_text = [str(element) for element in results2]
    
    # Store the URL and the extracted text in the dictionary
    data[a_url] = extracted_text

# Save the data to a JSON file
with open('results.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data has been saved to results.json")
