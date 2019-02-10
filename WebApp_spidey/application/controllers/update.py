import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, id_spidey):
        spidey = config.model_spider.select_spider(id_spidey)
        return config.render.update(spidey)

    def POST(self, id_spidey):
        formulario = web.input()
        nombre = formulario['nombre']
        identidad = formulario['identidad']
        genero = formulario['genero']
        universo = formulario['universo']
        aparicion = formulario['aparicion']
        colores = formulario['colores']
        config.model_spider.update_spider(id_spidey, nombre, identidad, genero, universo, aparicion, colores)
        raise web.seeother('/')
