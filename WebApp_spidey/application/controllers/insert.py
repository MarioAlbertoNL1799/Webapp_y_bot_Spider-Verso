import web
import config as config

class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert()

    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        identidad = formulario['identidad']
        genero = formulario['genero']
        universo = formulario['universo']
        aparicion = formulario['aparicion']
        colores = formulario['colores']
        config.model_spider.insert_spider(nombre, identidad, genero, universo, aparicion, colores)
        raise web.seeother('/')
