import requests
from bs4 import BeautifulSoup

from .models import Ad


class AdParser:
    BASE_URL = "https://www.farpost.ru"
    SEARCH_URL = f"{BASE_URL}/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"

    def fetch_page(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def get_author_from_ad_page(self, ad_url):
        soup = self.fetch_page(ad_url)
        author = soup.select_one(
            '.seller-summary-user .userNick a')
        return author.get_text(strip=True) if author else 'Unknown'

    def parse_ads(self):
        soup = self.fetch_page(self.SEARCH_URL)
        ads = []

        for idx, item in enumerate(soup.select('tr.bull-list-item-js')[:10]):
            title = item.select_one('.bull-item__self-link').get_text(
                strip=True)
            ad_id = int(item['data-doc-id'])
            ad_link = self.BASE_URL + item.select_one('.bull-item__self-link')[
                'href']
            views = int(item.select_one('.views').get_text(
                strip=True)) if item.select_one('.views') else 0
            position = idx + 1

            author = self.get_author_from_ad_page(ad_link)

            ad, created = Ad.objects.get_or_create(
                ad_id=ad_id,
                defaults={'title': title, 'author': author, 'views': views,
                          'position': position}
            )
            if not created:
                ad.position = position
                ad.save()

            ads.append(ad)

        return ads
