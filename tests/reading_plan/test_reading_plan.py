from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest


news_list = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 4,
        "summary": "Algo muito bacana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-longa-demais",
        "title": "Notícia longa demais",
        "timestamp": "03/03/2023",
        "writer": "Eles",
        "reading_time": 11,
        "summary": "Algo muito chato e maçante aconteceu",
        "category": "Chatices",
    }
]

mock_response = {
    "readable": [
        {
            "unfilled_time": 1,
            "chosen_news": [
                (
                    "Notícia bacana",
                    4,
                ),
            ],
        },
    ],
    "unreadable": [
        (
            "Notícia longa demais",
            11,
        )
    ],
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(False)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=news_list)

    response = ReadingPlanService.group_news_for_available_time(10)

    assert len(response["readable"]) == 1
    assert response["readable"][0]["unfilled_time"] == 6

    assert len(response["unreadable"]) == 1
