from bs4 import BeautifulSoup
import requests

# URL of the webpage you want to scrape
url = 'https://rozetka.com.ua'

# Sending a GET request to the URL
response = requests.get(url)

# Parsing the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Finding specific elements on the webpage
# For example, let's find all the <a> tags (links) on the webpage
links = soup.find_all('a')

# Printing out the text content of each link
for link in links:
    print(link.text)
