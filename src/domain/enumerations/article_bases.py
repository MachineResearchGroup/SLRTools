from enum import Enum


class ArticleBase(Enum):
    SCIENCE_DIRECT = 'science_direct'
    ACM = 'acm'
    IEEE = 'ieee'
    MDPI = 'mdpi'
    PUBMED = 'pub_med'
