import pandas as pd

from src.application.auxiliar_models.base_file import BaseFile
from src.application.auxiliar_models.dataset import Dataset
from os.path import exists


def get_file(file: BaseFile):
    with open(f"../archives/{file.__getattribute__('directory')}/{file.__getattribute__('article_base')}/"
              f"{str(file.__getattribute__('number'))}.{file.__getattribute__('extension')}", encoding="utf8") as file:
        return file


def file_exists(file: BaseFile):
    return exists(f"../archives/{file.__getattribute__('directory')}/{file.__getattribute__('article_base')}/"
                  f"{str(file.__getattribute__('number'))}.{file.__getattribute__('extension')}")


def path_topic_exists(topic: str):
    return exists(f"../archives/{topic}/")


def save_dataframe(dataset: Dataset):
    dataset.__getattribute__('dataframe').to_csv(f"../archives/dataset/{dataset.__getattribute__('type')}"
                                                 f"/{dataset.__getattribute__('name')}."
                                                 f"{dataset.__getattribute__('extension')}", index=False)


def get_dataframe(topic: str):
    return pd.read_csv(f"../archives/dataset/master/{topic}.csv")
