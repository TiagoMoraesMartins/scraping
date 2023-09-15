import pandas as pd
import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://fbref.com/pt/jogadores/72d0e1b6/gabriel-barbosa'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract specific elements from the webpage
title = soup.title.text
dtfs = pd.read_html(response.text)
df = pd.DataFrame(dtfs[0])
#pd.set_option("display.max_rows", df.shape[0] + 1)
print(df)