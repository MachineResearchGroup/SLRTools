from service.bibparser import BibTexDataBaseParser
from service.filter import FilterSLR
from dataclasses import dataclass
from domain.config import Config
from collections import Counter
from util import data
import pandas as pd


@dataclass
class DatasetGenerator:

    def __init__(self, config: Config):
        self.df = None
        self.config = config
        self.query = self.config.query

    def generate_dataset_principal(self, name: str, bases: []):
        print('criando dataset principal...')

        bib = BibTexDataBaseParser(bases, self.query)
        dataset = bib.bib_to_database()
        data.export_csv(dataset, 'geral', name, self.query)
        self.df = dataset

        print('dataset criado com sucesso!\n')

    def generate_dataset_info(self, text: str):
        print('criando dataset de informações gerais...')
        info = self.df.isnull().sum()
        data.export_csv(info, 'info', f'{self.config.dataset}_info_{text}', self.query, True)

        print('dataset criado com sucesso!\n')

    def generate_dataset_base_ano(self):
        print('criando dataset de quantidade de publicações por bases e por ano...')

        columns = ["Ano", "Base", "Quantidade"]
        dataset = pd.DataFrame(columns=columns)

        anos = self.df["year"].unique()
        bases = self.df["base"].unique()

        for ano in anos:
            for base in bases:
                qtd_ano = self.df.loc[self.df['year'] == ano]
                qtd_ano = qtd_ano.loc[self.df['base'] == base].count()
                dataset = dataset.append(
                    {
                        "Ano": ano,
                        "Base": base,
                        "Quantidade": qtd_ano['doi'],
                    }
                    , ignore_index=True
                )

        dataset.sort_values(by=['Ano'])
        data.export_csv(dataset, 'bases', f'{self.config.dataset}_base_ano', self.query)

        print('dataset criado com sucesso!\n')

    def generate_dataset_periodico(self):
        print('criando dataset de quantidade de publicações por periódico/evento...')

        columns = ["Periodico", "Quantidade"]

        dataset = pd.DataFrame(columns=columns)

        types = self.df["sourceTitle"].unique()

        for tp in types:
            qtd = self.df.loc[self.df["sourceTitle"] == tp].count()
            dataset = dataset.append(
                {
                    "Periodico": tp,
                    "Quantidade": qtd['doi'],
                }
                , ignore_index=True
            )

        dataset.sort_values(by=['Quantidade'], ascending=False)
        data.export_csv(dataset, 'periodico', f'periodico', self.query)

        print('dataset criado com sucesso!\n')

    def generate_dataset_keywords(self, df):
        print('criando dataset de palavras-chave...')
        list_keys = []

        keys = [key.split(";") for key in df['keywords'] if isinstance(key, str)]
        for k in keys:
            for word in k:
                if word != '':
                    word = word if word[0] != ' ' else word[1:]
                    word = word.lower()
                    list_keys.append(word)

        count = Counter(list_keys)

        dataset = pd.DataFrame.from_dict(count, orient='index').reset_index()
        dataset = dataset.rename(columns={'index': 'word', 0: 'weight'})
        dataset = dataset[['weight', 'word']]
        dataset.sort_values(by=['weight'], ascending=False)
        dataset = dataset.head(30)
        data.export_csv(dataset, 'keywords', f'{self.config.dataset}_palavras_chave', self.query)

        print('dataset criado com sucesso!\n')

    def generate_dataset_filtrado(self, word_list: [], filter_name: str):
        print('criando dataset filtrado...')

        dataset = FilterSLR(self.query).filter(word_list)
        data.export_csv(dataset, 'geral', f'filtrado_{filter_name}', self.query)

        print('dataset criado com sucesso!\n')

    def run(self, bases: []):
        if self.config.geracao_inicial:
            self.generate_dataset_principal('principal', bases)

        if self.config.dataset == 'covid':
            self.df = data.get_csv('geral', 'filtrado_covid', self.query)
        elif self.config.dataset == 'principal':
            self.df = data.get_csv('geral', 'principal', self.query)

        if self.config.info:
            self.generate_dataset_info('depois')

        if self.config.base_ano:
            self.generate_dataset_base_ano()

        if self.config.periodico:
            self.generate_dataset_periodico()

        if self.config.filtros:
            for filtro in self.config.filtros_valores:
                self.generate_dataset_filtrado(word_list=filtro['wordlist'], filter_name=filtro['nome'])

        if self.config.keywords:
            self.generate_dataset_keywords(self.df)

