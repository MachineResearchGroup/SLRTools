from src.application.auxiliar_models.science_direct_article_generator import ScienceDirectArticleGenerator
from src.application.mapper.set_articles_to_dataframe_mapper import SetArticlesToDataFrameMapping
from src.application.auxiliar_models.pubmed_article_generator import PubMedArticleGenerator
from src.application.auxiliar_models.ieee_article_generator import IEEEArticleGenerator
from src.application.auxiliar_models.mdpi_article_generator import MDPIArticleGenerator
from src.application.auxiliar_models.acm_article_generator import ACMArticleGenerator
from src.domain.models.set_articles import SetArticles
from dataclasses import dataclass
from typing import List


@dataclass
class DataFrameArticlesGenerator:
    topic: str
    article_base_list: List[str]

    def generate_dataframe_from_article_bases(self):
        all_articles = []
        for article_base in self.article_base_list:
            base = self.__get_base_generator_from_name(article_base, self.topic)
            all_articles.extend(base.generate_set_articles())

        set_articles = SetArticles(self.topic, all_articles)
        SetArticlesToDataFrameMapping().set_articles_to_dataframe(set_articles)

    def __get_base_generator_from_name(self, article_base: str, topic: str):

        if article_base == ScienceDirectArticleGenerator(topic).__getattribute__('article_base').value:
            return ScienceDirectArticleGenerator(topic)

        elif article_base == ACMArticleGenerator(topic).__getattribute__('article_base').value:
            return ACMArticleGenerator(topic)

        elif article_base == IEEEArticleGenerator(topic).__getattribute__('article_base').value:
            return IEEEArticleGenerator(topic)

        elif article_base == MDPIArticleGenerator(topic).__getattribute__('article_base').value:
            return MDPIArticleGenerator(topic)

        elif article_base == PubMedArticleGenerator(topic).__getattribute__('article_base').value:
            return PubMedArticleGenerator(topic)
