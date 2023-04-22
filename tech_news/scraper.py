import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    html_selector = Selector(text=html_content)
    update_links = html_selector.css("h2.entry-title a::attr(href)").getall()
    return update_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
