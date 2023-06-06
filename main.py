import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container for the postings
postings_container = soup.find('table', id='table_id')

if postings_container:
    # Find all the individual postings
    postings = postings_container.find_all('tr')

    # Iterate over the first 5 postings
    for posting in postings[:5]:
        txt = posting.text
        print(txt)
        # Extract the required fields
        est_value_notes = posting.find('td', class_='sorting_asc').text.strip()
        description = posting.find('div', class_='sorting_desc').text.strip()
        closing_date = posting.find('div', class_='sorting').text.strip()

        # Print the extracted information
        print('Est. Value Notes:', est_value_notes)
        print('Description:', description)
        print('Closing Date:', closing_date)
        print('---')
else:
    print('Postings container not found.')
