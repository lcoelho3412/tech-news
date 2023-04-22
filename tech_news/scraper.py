import requests
from parsel import Selector
from tech_news.database import create_news
from time import sleep


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


def scrape_updates(html_content):
    html_selector = Selector(text=html_content)
    update_links = html_selector.css("h2.entry-title a::attr(href)").getall()
    return update_links


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next::attr(href)").get()
    return next_page_link


def scrape_news(html_content):
    selector = Selector(text=html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css("div.meta-category span.label::text").get(),
    }


def get_tech_news(amount):
    next_page = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        content = fetch(next_page)
        urls = scrape_updates(content)

        for url in urls:
            if len(news) < amount:
                new_content = fetch(url)
                piece = scrape_news(new_content)
                news.append(piece)

        next_page = scrape_next_page_link(content)
        if not next_page:
            break

    create_news(news)
    return news
