from src.application.service.set_articles_generator_app import DataFrameArticlesGenerator
from src.service.auxiliar_models.config_set_generation import ConfigSetGeneration


def generate_set_articles(config: ConfigSetGeneration):

    DataFrameArticlesGenerator(config.__getattribute__('topic'), 
                               config.__getattribute__('article_base_list'))\
        .generate_dataframe_from_article_bases()
        
        


