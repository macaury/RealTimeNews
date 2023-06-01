from spiders.app import scrape_news 
from .celery import app


import time
import json
from celery import Celery
import tqdm
import requests






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
        
        print("selector e responser :" , progress_bar)

        while not task.ready():
            # Atualiza a barra de progresso
            progress_bar.update(10)
            # Aguarda um curto período de tempo antes de verificar novamente
            time.sleep(0.5)

        # Finaliza a barra de progresso
        progress_bar.close()

        # Aguarda a conclusão da tarefa e obtém o resultado
        return jsonify(task.get())


if __name__ == '__main__':
    app.run(debug=True)
