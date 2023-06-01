from celery import Celery

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='amqp://admin:admin@localhost:6379//',
    CELERY_RESULT_BACKEND='rpc://',
    CELERYD_CONCURRENCY=10,
    CELERYD_PREFETCH_MULTIPLIER=10
)

celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


import os
from celery import Celery

os.environ.setdefault('FLASK_APP', '__init__.py')  # Defina o nome do arquivo principal do Flask
os.environ.setdefault('FLASK_ENV', 'development')  # Defina o ambiente do Flask (development, production, etc.)

app = Celery('__init__')  # Substitua 'nome_do_app_atual' pelo nome do seu aplicativo Flask
app.config_from_object('flask.config')  # Importa as configurações do Flask
