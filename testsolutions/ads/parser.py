from typing import Any
import requests
from bs4 import BeautifulSoup

from ads.models import Ad


class AdParser:
    BASE_URL = "https://www.farpost.ru"
    SEARCH_URL = f"{BASE_URL}/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"

    def fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetches the HTML content of a given URL and returns a BeautifulSoup object.

        Args:
            url (str): The URL of the page to fetch.

        Returns:
            BeautifulSoup: Parsed HTML content of the page.
        """
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def get_author_from_ad_page(self, ad_url: str) -> str:
        """
        Extracts the author's name from the ad page.

        Args:
            ad_url (str): The URL of the ad page.

        Returns:
            str: The author's name, or 'Unknown' if the author is not found.
        """
        soup = self.fetch_page(ad_url)
        author = soup.select_one('.seller-summary-user .userNick a')
        return author.get_text(strip=True) if author else 'Unknown'

    def parse_ads(self) -> list[Any]:
        """
        Parses ads from the search page and updates the database.

        Returns:
            list: A list of Ad objects.
        """
        soup = self.fetch_page(self.SEARCH_URL)
        ads = []

        for idx, item in enumerate(soup.select('tr.bull-list-item-js')[:10]):
            title = item.select_one('.bull-item__self-link').get_text(strip=True)
            ad_id = int(item['data-doc-id'])
            ad_link = self.BASE_URL + item.select_one('.bull-item__self-link')['href']
            views = int(item.select_one('.views').get_text(strip=True)) if item.select_one('.views') else 0
            position = idx + 1

            author = self.get_author_from_ad_page(ad_link)

            ad, created = Ad.objects.get_or_create(
                ad_id=ad_id,
                defaults={'title': title, 'author': author, 'views': views, 'position': position}
            )
            if not created:
                ad.position = position
                ad.save()

            ads.append(ad)

        return ads
