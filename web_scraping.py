import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the web page
url = "https://example.com"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract data
title = soup.title.string
print("Page Title:", title)