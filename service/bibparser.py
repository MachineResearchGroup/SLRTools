import json
import pandas as pd
from util import data
from dataclasses import dataclass
from domain.article import Article
import service.risadjust as risadjust


@dataclass
class BibTexDataBaseParser:
    bases: list
    query: str

    def contains(self, article, articles):
        for a in articles:
            if a.doi == article.doi:
                return True
        return False

    def parse_keywords_to_str(self, keys: []):
        keyword_str = ''

        for k in keys:
            if keys[0] == k:
                keyword_str = k
            else:
                keyword_str = keyword_str + '; ' + k

        return keyword_str

    def insert_article(self, base, articles, r, r_aux):
        if base != 'IEEE' or (base == 'IEEE' and 'ENTRYTYPE' in r and r['ENTRYTYPE'] != 'inbook'):
            article = Article(
                doi=r['doi'] if 'doi' in r else '',
                url=r['url'] if 'url' in r else '',
                author=r['author'] if 'author' in r else '',
                base=base,
                title=r['title'] if 'title' in r else '',
                year=r['year'] if 'year' in r else '',
                articleType=r['ENTRYTYPE'] if 'ENTRYTYPE' in r else '',
                sourceTitle=r['journal'] if 'journal' in r else r[
                    'booktitle'] if 'booktitle' in r else '',
                keywords=r['keywords'].replace(',', ';') if 'keywords' in r else '',
                abstract=r['abstract'].replace('\n', ' ') if 'abstract' in r else ''
            )
            if base == 'MDPI':
                article.__setattr__('keywords', self.parse_keywords_to_str(r_aux['keywords'])
                                    .replace(',', ';') if 'keywords' in r_aux else '')

                if not self.contains(article, articles):
                    articles.append(article)

            else:
                articles.append(article)

    def bib_to_database(self):
        articles = []

        for base in self.bases:

            print(f'Coletando arquivos BibTeX de {base}')

            for count in range(70):

                filename = self.query + '_' + str(count)
                try:
                    results = json.loads(json.dumps(data.get_bib(filename, base), indent=False))

                    print(f'Coletando arquivos BibTeX de {base}: {str(count + 1)}')

                    if base == 'MDPI':
                        risadjust.ris_adjust(filename, base)
                        results_aux = data.get_ris(filename, base)

                        for r, r_aux in zip(results, results_aux):
                            r = results[r]
                            self.insert_article(base, articles, r, r_aux)

                    else:
                        for r in results:
                            r = results[r]
                            self.insert_article(base, articles, r, None)

                except:
                    break

        df = pd.DataFrame.from_records([a.to_dict() for a in articles])
        return df
