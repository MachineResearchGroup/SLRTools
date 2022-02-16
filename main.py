from service.datasetgenerator import DatasetGenerator
from domain.config import Config


if __name__ == '__main__':
    filtro_covid = {'nome': 'covid',
                    'wordlist': ['covid', 'coronavirus', 'srs-cov-2', 'covid19', 'covid-19', 'virus', 'pandemic',
                                 'quarantine', '2019-nCoV']
                    }

    filtro_smart = {'nome': 'smart_city',
                    'wordlist': ['smart house', 'smart grid', 'smart cities', 'smart city', 'smart home',
                                 'smart farming', 'smart parking', 'smart maintenance', 'smart lighting']
                    }

    config = Config(query='bi_dy',
                    geracao_inicial=False,
                    dataset='principal',
                    info=False,
                    base_ano=False,
                    periodico=False,
                    keywords=False,
                    filtros=False,
                    filtros_valores=[filtro_covid]
                    )

    generator = DatasetGenerator(config)
    generator.run(['ACM', 'ScienceDirect', 'MDPI'])
