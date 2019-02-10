from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'spider_bot',
    user = 'spidey',
    pw = 'spidey.2019',
    port = 3307
    )

#Spidey_bot
token = '786763058:AAG7mXO5x8oGawaLrEMxTkPEgB7Bb9p21Oc'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Saludos {} , para conocer mas usa estos comandos:\n/info llave #busca_informacion\n/spider #busca_descripcion_de_nombre_o_identidad_similar\n/aparicion llave #muestra_la_primer_aparicion_en_comics'.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion\n/spider llave #busca_descripcion_de_nombre_o_identidad_similar\n/aparicion llave #muestra_la_primer_aparicion_en_comics'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        id_spidey = int(text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(id_spidey)
        result = db.select('spiders', where='id_spidey=$id_spidey',vars=locals())[0]
        print result
        respuesta =  "| Nombre: "+ str(result.nombre) + "|\n| Identidad: " + str(result.identidad) + "|\n|Tipo: " + str(result.genero) + "|\n| Tierra: " +str(result.universo) + "|\n| Primer aparicion: " + str(result.aparicion) + "|\n|Vestimenta: " + str(result.colores) +"|"
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Saludos {}\nEsto es la informacion que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_spidey))

def search2(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        valor = text[1]
        sql = "Select nombre, universo, identidad from spiders where nombre like '%"+valor+"%' or identidad like '%"+valor+"%';"
        print "Send info to {}".format(username)
        print "Key search {}".format(valor)
        result = db.query(sql, vars=locals())[0]
        print result
        respuesta = "| Nombre: "+ str(result.nombre) + " | Tierra: " + str(result.universo) + " | Identidad: " +str(result.identidad) + " |\n"
        update.message.reply_text('{}Aqui esta lo que buscas: \n {}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('No se encontro resultado'.format(spider))
def search3(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        valor = text[1]
        sql = "Select nombre, identidad, aparicion from spiders where nombre like '%"+valor+"%' or identidad like '%"+valor+"%';"
        print "Send info to {}".format(username)
        print "Key search {}".format(valor)
        result = db.query(sql, vars=locals())[0]
        print result
        respuesta = "| Nombre: "+ str(result.nombre) + " | Identidad: " + str(result.identidad) + " | Primer aparicion: " +str(result.aparicion) + " |\n"
        update.message.reply_text('{}Aqui esta lo que buscas: \n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('No se encontro resultado'.format(spider))
def spider(bot, update):
    search2(update)

def info(bot, update):
    search(update)

def aparicion(bot, update):
    search3(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    try:
        print 'Spidey_bot init token'

        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'Spidey_bot init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))
        dp.add_handler(CommandHandler("spider", spider))
        dp.add_handler(CommandHandler("aparicion", aparicion))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'Spidey_bot ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
