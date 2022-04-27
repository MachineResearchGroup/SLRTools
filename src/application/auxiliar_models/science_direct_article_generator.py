from src.application.interfaces.base_article_generator import BaseArticleGenerator
from src.domain.enumerations.article_bases import ArticleBase
from src.application.parser.bib_parser import BibParser
from dataclasses import dataclass


@dataclass
class ScienceDirectArticleGenerator(BaseArticleGenerator):

    def __init__(self, topic: str):
        self.topic = topic
        self.article_base = ArticleBase.SCIENCE_DIRECT
        self.parser = BibParser()