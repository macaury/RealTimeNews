import string
import scrapy
import json



def test (domain, url , noticia_rep, titulo_rep , hora_rep,img_rep ,link_rep , categoria_rep) :
    class G1GloboSpider(scrapy.Spider):

        name = "G1.globo"
        allowed_domains = [domain]
        start_urls = [url]

        def parse(self, response):

            noticias = []
            for noticia in response.css(noticia_rep):
                titulo = noticia.css(titulo_rep).get()
                hora = noticia.css(hora_rep).get()
                imagem = noticia.css(img_rep).get()
                link = noticia.css(link_rep).get()
                categoria = noticia.css(categoria_rep).get() 

                noticia_dict = {'titulo': titulo, 'imagem': imagem , 'link': link, 'H_postado' : hora , 'categoria' : categoria}

                noticias.append(noticia_dict)

            dados = {'noticias': noticias}

            new_domain =  domain.replace(".", "_")
            
            path_data =  f"data_json/{new_domain}.json"

            with open(path_data, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)


    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(G1GloboSpider)
    process.start()



noticia_rep = '.feed-post-body'

titulo_rep = '.gui-color-hover a::text'

hora_rep = '.feed-post-datetime ::text'

img_rep = '.bstn-fd-picture-image ::attr(srcset)'

link_rep = '.feed-post-figure-link ::attr(href)'

categoria_rep = '.feed-post-metadata-section ::text'


domain = "g1.globo.com"

url= "https://g1.globo.com"

test ( domain ,url, noticia_rep, titulo_rep , hora_rep,img_rep ,link_rep , categoria_rep) 