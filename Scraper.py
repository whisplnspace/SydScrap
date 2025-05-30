import requests
from bs4 import BeautifulSoup
import json

def scrape_eventbrite():
    url = "https://www.eventbrite.com.au/d/australia--sydney/events/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    for card in soup.select("div.eds-event-card-content__content")[:10]:
        title_tag = card.select_one("div.eds-event-card-content__primary-content > div > div > a > div")
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            continue

        link_tag = card.find("a", href=True)
        link = link_tag["href"] if link_tag else "#"

        date_time = card.select_one("div.eds-text-bs--fixed").get_text(strip=True) if card.select_one("div.eds-text-bs--fixed") else "N/A"
        location = "Sydney, Australia"
        description = "Exciting event in Sydney. Check it out!"

        events.append({
            "title": title,
            "date_time": date_time,
            "location": location,
            "description": description,
            "link": link
        })

    with open("event_data.json", "w") as f:
        json.dump(events, f, indent=4)

if __name__ == "__main__":
    scrape_eventbrite()
