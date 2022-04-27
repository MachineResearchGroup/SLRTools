from src.domain.models.article import Article
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class SetArticles:

    def __init__(self, name: str, articles: List[Article]):
        self.name = name
        self.date = date.today()
        self.articles = articles
