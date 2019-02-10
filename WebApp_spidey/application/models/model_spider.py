import config as config
db = config.db

'''
Seleccion de registros aracnidos
'''
def select_spiders():
    try:
        return db.select('spiders')
    except Exception as e:
        print "Model select_spiders Error {}".format(e.args)
        print "Model select_spiders Message {}".format(e.message)
        return None

'''
Seleccion de un registro aracnido con coincidencia
'''
def select_spider(id_spidey):
    try:
        return db.select('spiders',where='id_spidey=$id_spidey', vars=locals())[0]
    except Exception as e:
        print "Model select_spider Error {}".format(e.args)
        print "Model select_spider Message {}".format(e.message)
        return None

'''
Ingreso de un nuevo hombre arania
'''
def insert_spider(nombre,identidad,genero,universo,aparicion,colores):
    try:
        return db.insert('spiders', nombre=nombre,identidad=identidad,genero=genero,universo=universo,aparicion=aparicion,colores=colores)
    except Exception as e:
        print "Model insert_spider Error {}".format(e.args)
        print "Model insert_spider Message {}".format(e.message)
        return None

'''
Eliminar aracnido
'''
def delete_spider(id_spidey):
    try:
        return db.delete('spiders', where='id_spidey=$id_spidey',vars=locals())
    except Exception as e:
        print "Model delete_spidey Error {}".format(e.args)
        print "Model delete_spidey Message {}".format(e.message)
        return None

'''
Actualizar datos de aracnido
'''
def update_spider(id_spidey, nombre, identidad, genero, universo, aparicion, colores):
    try:
        return db.update('spiders',
                         nombre=nombre,
                         identidad=identidad,
                         genero=genero,
                         universo=universo,
                         aparicion=aparicion,
                         colores=colores,
                         where='id_spidey=$id_spidey', vars=locals())
    except Exception as e:
        print "Model update_spider Error {}".format(e.args)
        print "Model update_spider Error {}".format(e.args)
        return None
