import string
import scrapy
import json


def main(domain, url):
    class G1GloboSpider(scrapy.Spider):

        name = "G1.globo"
        allowed_domains = [domain]
        start_urls = [url]

        def parse(self, response):

            path_json_journal = "data_json/journals.json/journal.json"

            with open(path_json_journal, encoding='utf-8') as arquivo_json:
                dats = json.load(arquivo_json)

                #domain_rep = dats["g1.globo.com"][0]["domain_rep"]
                noticia_rep = dats[domain][0]["noticia_rep"]
                titulo_rep = dats[domain][0]["titulo_rep"]
                hora_rep = dats[domain][0]["hora_rep"]
                img_rep = dats[domain][0]["img_rep"]
                link_rep = dats[domain][0]["link_rep"]
                categoria_rep = dats[domain][0]["categoria_rep"]

            print(dats)

            noticias = []
            for noticia in response.css(noticia_rep):
                titulo = noticia.css(titulo_rep).get()
                hora = noticia.css(hora_rep).get()
                imagem = noticia.css(img_rep).get()
                link = noticia.css(link_rep).get()
                categoria = noticia.css(categoria_rep).get()

                noticia_dict = {'titulo': titulo, 'imagem': imagem,
                                'link': link, 'H_postado': hora, 'categoria': categoria}

                noticias.append(noticia_dict)

            dados = {'noticias': noticias}

            new_domain = domain.replace(".", "_")

            path_data = f"data_json/{new_domain}.json"

            with open(path_data, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(G1GloboSpider)
    process.start()
