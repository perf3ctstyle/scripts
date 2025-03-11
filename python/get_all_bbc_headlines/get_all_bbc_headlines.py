import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.bbc.com/news'
# Send a GET request to fetch the webpage content
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract all H2 headlines from the page
    headlines = soup.find_all(attrs={"data-testid": "card-headline"})
    # Print each headline
    for headline in headlines:
        print(headline.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
