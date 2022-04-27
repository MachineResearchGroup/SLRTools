from src.application.auxiliar_models.dataset import Dataset
from src.domain.models.set_articles import SetArticles
from src.infra.data import data_handler
import pandas as pd


class SetArticlesToDataFrameMapping:
    
    def set_articles_to_dataframe(self, set_articles: SetArticles):

        dataframe = pd.DataFrame.from_records([a.to_dict() for a in set_articles.__getattribute__('articles')])
        name = set_articles.__getattribute__('name') + '_' + str(set_articles.__getattribute__('date'))
        
        data_handler.save_dataframe(Dataset(name=name, 
                                            type='master', 
                                            dataframe=dataframe, 
                                            extension='csv'))
