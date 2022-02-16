from dataclasses import dataclass


@dataclass
class Config:
    query: str
    geracao_inicial: bool
    dataset: str
    info: bool
    base_ano: bool
    periodico: bool
    keywords: bool
    filtros: bool
    filtros_valores: list
