import web

urls = (
    '/', 'application.controllers.index.Index',
    '/insert', 'application.controllers.insert.Insert',
    '/update/(.*)','application.controllers.update.Update',
    '/delete/(.*)','application.controllers.delete.Delete',
    '/view/(.*)','application.controllers.view.View',
)

render = web.template.render('application/views/',base='master')
if __name__ == "__main__": # equivalente a metodo main de java. '__' = private
    app = web.application(urls, globals()) # Configuracion/variable  que habla a la url de la variable anterior
    web.config.debug = False
    def NotFound():
        return web.notfound(render.notfound())
    def Internal():
        return web.internalerror(render.internal())
    app.notfound = NotFound
    app.internalerror = Internal
    app.run()#inicia
