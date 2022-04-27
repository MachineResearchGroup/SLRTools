from src.application.auxiliar_models.base_file import BaseFile
from src.domain.enumerations.article_bases import ArticleBase
from src.application.interfaces.parser import Parser
from src.domain.models.article import Article
from abc import ABC
from dataclasses import dataclass
from typing import List

from src.infra.data import data_handler


@dataclass
class BaseArticleGenerator(ABC):

    topic: str
    article_base: ArticleBase
    parser: Parser

    def generate_set_articles(self) -> List[Article]:
        file_number = 1
        next_file = BaseFile(directory=self.topic,
                             article_base=self.article_base.value,
                             number=file_number,
                             extension=self.parser.__getattribute__('extension'))
        articles = []

        while data_handler.file_exists(next_file):
            articles.extend(self.parser.transform_unique_file_in_articles(next_file,
                                                                          self.article_base.value))
            file_number += 1
            next_file.__setattr__('number', file_number)

        articles = self.__remove_duplicate_articles(articles)
        return articles

    def __remove_duplicate_articles(self, articles: List[Article]) -> List[Article]:
        unique_articles = []

        for article in articles:
            if article not in unique_articles:
                unique_articles.append(article)

        return unique_articles

