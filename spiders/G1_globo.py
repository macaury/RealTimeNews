import scrapy
import json


class G1GloboSpider(scrapy.Spider):
    name = "G1.globo"
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com"]


    def parse(self, response):
        noticias = []
        for noticia in response.css('.feed-post-body'):
            titulo = noticia.css('.gui-color-hover a::text').get()
            hora = noticia.css('.feed-post-datetime ::text').get()
            imagem = noticia.css('.bstn-fd-picture-image ::attr(srcset)').get()
            link = noticia.css('.feed-post-figure-link ::attr(href)').get()
            categoria = noticia.css('.feed-post-metadata-section ::text').get() 

            noticia_dict = {'titulo': titulo, 'imagem': imagem , 'link': link, 'H_postado' : hora , 'categoria' : categoria}
            
            noticias.append(noticia_dict)

        dados = {'noticias': noticias}
        
        path_data = "News/News/data_json/g1.json"

        with open(path_data, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(G1GloboSpider)
process.start()
