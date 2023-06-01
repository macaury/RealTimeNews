import time
import json
from celery import Celery
from flask import Flask, jsonify
import tqdm
import requests
from scrapy import Selector


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERYD_CONCURRENCY=10,
    CELERYD_PREFETCH_MULTIPLIER=10
)

celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def scrape_news(domains, urls):

    for domain, url in zip(domains, urls):
        response = requests.get(url)
        selector = Selector(text=response.text)
        
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

        for noticia in selector.css(noticia_rep):
            titulo = noticia.css(titulo_rep).get().strip()
            imagem = noticia.css(img_rep).get()
            link = noticia.css(link_rep).get()

            noticia_dict = {'titulo': titulo, 'imagem': imagem, 'link': link}
            noticias.append(noticia_dict)
            count += 1
            if count >= 2:
                break

    new_data = {}
    for domain, noticias in zip(domains, noticias):
        new_domain = domain.replace(".", "_")
        new_data[new_domain] = noticias

    # Retorna o conteúdo JSON
    conteudo = json.dumps(new_data, ensure_ascii=False, indent=4)
    return conteudo
