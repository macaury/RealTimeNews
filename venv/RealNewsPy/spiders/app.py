import time
import scrapy
import json
from celery import Celery
from flask import Flask, jsonify
import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERYD_CONCURRENCY=4,
    CELERYD_PREFETCH_MULTIPLIER=4
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
                if count >= 2:
                    break

            new_domain = domain.replace(".", "_")
            dados = {new_domain: noticias}

            # Retorna o conteúdo JSON
            return json.dumps(dados, ensure_ascii=False, indent=4)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service('path/to/chromedriver')  # Substitua pelo caminho correto para o executável do ChromeDriver

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    process = scrapy.crawler.CrawlerProcess(settings={
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'REACTOR_THREADPOOL_MAXSIZE': 20,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.1,
        'AUTOTHROTTLE_MAX_DELAY': 5.0,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_selenium.SeleniumMiddleware': 800,
        },
        'SELENIUM_DRIVER_NAME': 'chrome',
        'SELENIUM_DRIVER_EXECUTABLE_PATH': 'path/to/chromedriver',  # Substitua pelo caminho correto para o executável do ChromeDriver
        'SELENIUM_DRIVER_ARGUMENTS': [],
    })
    
    process.crawl(G1GloboSpider, driver=driver)
    process.start()

    driver.quit()


@app.route("/news", methods=['GET'])
def main():
    with app.app_context():
        json_file_path = "./journals/journal.json"
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

        progress_bar = tqdm.tqdm(total=len(domains), desc="Scraping Progress")

        while not task.ready():
            # Atualiza a barra de progresso
            progress_bar.update(1)
            # Aguarda um curto período de tempo antes de verificar novamente
            time.sleep(0.1)

        # Finaliza a barra de progresso
        progress_bar.close()

        # Aguarda a conclusão da tarefa e obtém o resultado
        return jsonify(task.get())


if __name__ == '__main__':
    app.run(debug=True)
