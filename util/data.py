from pandas import DataFrame
import bibtexparser
import pandas as pd
import rispy


def get_bib(file_name: str, base: str):
    with open(f"archives/bibtex/{base}_{file_name}.bib", encoding="utf8") as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database.entries_dict


def get_ris(file_name: str, base: str):
    with open(f"archives/ris/{base}_{file_name}.ris", 'r', encoding="utf8") as bibliography_file:
        entries = rispy.load(bibliography_file)

    return entries


def export_csv(dataset: DataFrame, path: str, name: str, query: str, index=False):
    dataset.to_csv(f"archives/results/{path}/dataset_{name}_{query}.csv", index=index)


def get_csv(path: str, name: str, query: str):
    return pd.read_csv(f"archives/results/{path}/dataset_{name}_{query}.csv")

