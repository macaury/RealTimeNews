import string
import scrapy
import json

def main(domains, urls):
    class G1GloboSpider(scrapy.Spider):
        name = "g1globo_spider"

        def start_requests(self):
            for domain, url in zip(domains, urls):
                yield scrapy.Request(url=url, callback=self.parse, meta={'domain': domain})

        def parse(self, response):
            domain = response.meta['domain']
            path_json_journal = "data_json/journals.json/journal.json"

            with open(path_json_journal, encoding='utf-8') as arquivo_json:
                dats = json.load(arquivo_json)
                data = dats[domain][0]
                noticia_rep = data["noticia_rep"]
                titulo_rep = data["titulo_rep"]
                img_rep = data["img_rep"]
                link_rep = data["link_rep"]

            noticias = []
            for noticia in response.css(noticia_rep):
                titulo = noticia.css(titulo_rep).get()
                imagem = noticia.css(img_rep).get()
                link = noticia.css(link_rep).get()

                noticia_dict = {'titulo': titulo, 'imagem': imagem, 'link': link}
                noticias.append(noticia_dict)

            dados = {domain: noticias}

            new_domain = domain.replace(".", "_")
            path_data = f"data_json/{new_domain}.json"

            with open(path_data, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(G1GloboSpider)
    process.start() 