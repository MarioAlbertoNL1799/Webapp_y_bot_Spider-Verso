import web
import config as config

class Delete:
    def __init__(self):
        pass

    def GET(self,id_spidey):
        spider = config.model_spider.select_spider(id_spidey) # Selecciona todos los registros aracnidos
        return config.render.delete(spider) # Envia todos los registro y envia a delete.html

    def POST(self, id_spidey):
        formulario = web.input()
        id_spidey = formulario['id_spidey']
        config.model_spider.delete_spider(id_spidey)
        raise web.seeother('/')
