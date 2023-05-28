import scrapy
from scrapy.crawler import CrawlerProcess
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def main(domains, urls):

    def get_scraped_data(domains, urls):
        class G1GloboSpider(scrapy.Spider):
            name = "g1globo_spider"

            def start_requests(self):
                for domain, url in zip(domains, urls):
                    yield scrapy.Request(url=url, callback=self.parse, meta={'domain': domain})

            def parse(self, response):
                domain = response.meta['domain']
                path_json_journal = "data_json/journals/journal.json"

                with open(path_json_journal, encoding='utf-8') as arquivo_json:
                    dats = json.load(arquivo_json)
                    data = dats[domain][0]
                    noticia_rep = data["noticia_rep"]
                    titulo_rep = data["titulo_rep"]
                    img_rep = data["img_rep"]
                    link_rep = data["link_rep"]

                count = 0
                noticias = []

                for noticia in response.css(noticia_rep):
                    titulo = noticia.css(titulo_rep).get()
                    imagem = noticia.css(img_rep).get()
                    link = noticia.css(link_rep).get()

                    noticia_dict = {'titulo': titulo, 'imagem': imagem, 'link': link}
                    noticias.append(noticia_dict)
                    count += 1
                    if count >= 10:
                        break

                new_domain = domain.replace(".", "_")
                dados = {new_domain: noticias}

                # Retorna o conteúdo JSON
                return json.dumps(dados, ensure_ascii=False, indent=4)

        process = CrawlerProcess()
        scraped_data = process.crawl(G1GloboSpider)
        process.start()

        return scraped_data

    with app.app_context():
        scraped_data = get_scraped_data(domains, urls)

        print(scraped_data)

    return 

if __name__ == '__main__':


    app.run()
