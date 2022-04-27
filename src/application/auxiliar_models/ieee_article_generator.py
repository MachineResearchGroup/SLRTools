from src.application.interfaces.base_article_generator import BaseArticleGenerator
from src.domain.enumerations.article_bases import ArticleBase
from src.application.parser.bib_parser import IEEEBibParser
from dataclasses import dataclass


@dataclass
class IEEEArticleGenerator(BaseArticleGenerator):

    def __init__(self, topic: str):
        self.topic = topic
        self.article_base = ArticleBase.IEEE
        self.parser = IEEEBibParser()
