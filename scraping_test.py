import requests
from bs4 import BeautifulSoup

url = "https://www.airbnb.com/rooms/606801579780717669?adults=1&category_tag=Tag%3A8678&children=0&enable_m3_private_room=true&infants=0&pets=0&photo_id=1383695469&check_in=2023-12-15&check_out=2023-12-17&source_impression_id=p3_1699214088_G2GdZZnedyLQ9Mqk&previous_page_section_name=1000&federated_search_id=7d1bd017-0f35-4cba-8745-5ce1abd2a7e1"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing the ratings
ratings_section = soup.find('span', {'class': 'a8jt5op'})
if ratings_section:
    ratings_text = ratings_section.get_text(strip=True)
    print("Ratings:", ratings_text)
else:
    print("Ratings not found on the page.")
