import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the New York Times website
url = 'https://www.nytimes.com/'
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Identify the HTML elements that contain the article titles and descriptions
articles = soup.find_all('article', class_='css-8atqhb')

# Create an empty list to store the data
data = []

# Extract the title and description of each article using BeautifulSoup
for article in articles[:10]:
    try:
        title = article.find('h2', class_='css-1j9dxys e1voiwgp0').text.strip()
        description = article.find('p', class_='css-1echdzn e1wijjg60').text.strip()
        data.append({'Title': title, 'Description': description})
    except AttributeError:
        pass

# Write the data to a CSV file
with open('nytimes.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Description'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print('Data has been scraped and saved to nytimes.csv')
