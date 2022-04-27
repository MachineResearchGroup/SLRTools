from src.application.mapper.article_json_to_domain_article_mapper import ArticleJsonToDomainArticleMapping
from src.application.auxiliar_models.base_file import BaseFile
from src.domain.models.article import Article
from abc import ABC, abstractmethod
from typing import List


class Parser(ABC):

    def __init__(self, extension):
        self.article_mapper = ArticleJsonToDomainArticleMapping()
        self.extension = extension

    @abstractmethod
    def transform_unique_file_in_articles(self, file: BaseFile, article_base: str) -> List[Article]:
        pass
