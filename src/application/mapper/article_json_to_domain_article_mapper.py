from src.domain.models.article import Article
import json


class ArticleJsonToDomainArticleMapping:

    def json_to_domain_article(self, value: json, article_base: str):
        article = Article(
            base=article_base,
            doi=value['doi'] if 'doi' in value else '',
            url=value['url'] if 'url' in value else '',
            author=value['author'] if 'author' in value else '',
            title=value['title'] if 'title' in value else '',
            year=value['year'] if 'year' in value else '',
            articleType=value['ENTRYTYPE'] if 'ENTRYTYPE' in value else '',
            sourceTitle=value['journal'] if 'journal' in value else value['booktitle'] if 'booktitle' in value else '',
            keywords=value['keywords'].replace(',', ';') if 'keywords' in value else '',
            abstract=value['abstract'].replace('\n', ' ') if 'abstract' in value else ''
        )

        return article
