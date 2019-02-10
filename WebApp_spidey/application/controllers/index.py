import web
import config as config

class Index:
    def __init__(self):
        pass

    def GET(self):
        spiders = config.model_spider.select_spiders().list() # Selecciona todos los registros aracnidos
        return config.render.index(spiders) # Envia todos los registros y renderiza index.html
