import requests
from bs4 import BeautifulSoup 

page = requests.get('file:///home/mehrab/Music/43rd%20BCS%20Preli%20Question%20Bank%20.html')
# soup = BeautifulSoup(page.content, 'html.parser')
n = page.status_code
print(n)

# questions = []

# # Find all odd td elements with colspan=4
# odd_td_elements = soup.select('td[colspan="4"]:nth-of-type(odd)')

# # Select the span elements within the odd td elements
# span_elements = [td.select_one('span') for td in odd_td_elements]

# # Extract the text data from the span elements
# span_text_data = [span.text for span in span_elements if span]


