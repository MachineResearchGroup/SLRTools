from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class Dataset:
    name: str
    type: str
    dataframe: DataFrame
    extension: str
