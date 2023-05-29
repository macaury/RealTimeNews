import scrapy
import json
from celery import Celery
from flask import Flask, jsonify
from redis import Redis


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def scrape_news(domains, urls):
    class G1GloboSpider(scrapy.Spider):
        name = "g1globo_spider"

        def start_requests(self):
            for domain, url in zip(domains, urls):
                yield scrapy.Request(url=url, callback=self.parse, meta={'domain': domain})

        def parse(self, response):
            domain = response.meta['domain']
            path_json_journal = "./journals/journal.json"

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

                noticia_dict = {'titulo': titulo,
                                'imagem': imagem, 'link': link}
                noticias.append(noticia_dict)
                count += 1
                if count >= 10:
                    break

            new_domain = domain.replace(".", "_")
            dados = {new_domain: noticias}

            # Retorna o conteúdo JSON
            return json.dumps(dados, ensure_ascii=False, indent=4)

    process = scrapy.crawler.CrawlerProcess()
    process.crawl(G1GloboSpider)
    process.start()


@app.route("/news", methods=['GET'])
def main():
    with app.app_context():
        json_file_path = "/journals/journal.json"
        with open(json_file_path) as file:
            data = json.load(file)
            domains = []
            urls = []
            for key in data:
                domain = data[key][0]["domain_rep"]
                url = data[key][0]["url_rep"]
                domains.append(domain)
                urls.append(url)

        # Inicia a tarefa de scraping usando o Celery
        task = scrape_news.delay(domains, urls)

        return jsonify({'task_id': task.id}), 202


main()

if __name__ == '__main__':
    app.run(debug=True)
