from src.application.interfaces.base_article_generator import BaseArticleGenerator
from src.application.parser.pub_med_parser import PubMedRisParser
from src.domain.enumerations.article_bases import ArticleBase
from dataclasses import dataclass


@dataclass
class PubMedArticleGenerator(BaseArticleGenerator):

    def __init__(self, topic: str):
        self.topic = topic
        self.article_base = ArticleBase.PUBMED
        self.parser = PubMedRisParser()
