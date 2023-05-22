import string
import scrapy
import json


def main(domain, url):
    class G1GloboSpider(scrapy.Spider):

        name = "G1.globo"
        allowed_domains = [domain]
        start_urls = [url]

        def parse(self, response):

            path_json_journal = "../journal.json"

            with open(path_json_journal) as arquivo_json:
                dats = json.load(arquivo_json)

                domain_rep = dats['domain_rep']
                url_rep = dats['url_rep']
                noticia_rep = dats['noticia_rep']
                titulo_rep = dats['titulo_rep']
                hora_rep = dats['hora_rep']
                img_rep = dats['img_rep']
                link_rep = dats['link_rep']
                categoria_rep = dats['categoria_rep']

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
