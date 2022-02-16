from dataclasses import dataclass


@dataclass
class Article:
    doi: str
    url: str
    author: str
    base: str
    title: str
    year: str
    articleType: str
    sourceTitle: str
    keywords: str
    abstract: str

    def to_dict(self):
        return {
            'doi': self.doi,
            'url': self.url,
            'author': self.author,
            'year': self.year,
            'title': self.title,
            'articleType': self.articleType,
            'sourceTitle': self.sourceTitle,
            'base': self.base,
            'abstract': self.abstract,
            'keywords': self.keywords,
        }
