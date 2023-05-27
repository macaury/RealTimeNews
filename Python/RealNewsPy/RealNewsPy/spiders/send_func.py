from jour import main
import json
import sys
sys.path.append('./jour.py')


json_file_path = "data_json/journals/journal.json"
with open(json_file_path) as file:
    data = json.load(file)
    domains = []
    urls = []
    for key in data:
        domain = data[key][0]["domain_rep"]
        url = data[key][0]["url_rep"]
        domains.append(domain)
        urls.append(url)

main(domains, urls)