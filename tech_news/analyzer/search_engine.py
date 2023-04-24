from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]


# Requisito 8
def search_by_date(date):
    try:
        formated = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        return [
            (new["title"], new["url"])
            for new in search_news({"timestamp": {"$eq": formated}})
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]
