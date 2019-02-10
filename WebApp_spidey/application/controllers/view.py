import web
import config as config

class View:
    def __init__(self):
        pass

    def GET(self, id_spidey):
        spidey = config.model_spider.select_spider(id_spidey)
        return config.render.view(spidey)
