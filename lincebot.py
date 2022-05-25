from telegram.ext import (Updater, CommandHandler)


def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, '''!Hola lince \U0001F44B \U0001F44B!, soy un ChatBot(Lincebot) \U0001F916 \n\n
		Seré tu guía virtual de las instalaciones del Tecnológico Nacional de México en Celaya Campus 2. \U0001F431 \U0001F431 \n\n
		Para ayudarte a encontrar el edificio que gustes puedes preguntarme/escribirme de la siguiente manera: \"¿Edificio -Tu destino-?\". \U0001F6B6 \U0001F6B6 \n\n
		Ejemplos: /Sistemas, /Cafetería, /Asociaciones\U0001F3EB  \n\n
		Si nececitas ayuda puedes usar /hepl para recibir todos los comandos diponibles \n\n
		Espero pueda ayudarte a encontrar tu destino, Orgullosamente Linces! \U0001F9BE \U0001F431''')


def helpMe(update, context):
    context.bot.send_message(update.message.chat_id, '''!Hola lince! estos son los edificios que se puden consultar \n
	--> /sistemas \n
	--> /Centro_de_Idiomas \n
	--> /Departamento_de_ingeniería_Industrial \n
	--> /vinculación \n
	--> /Aulas_Ingeniería_Industrial_B \n
	--> /Edificio_Ingeniería_Industrial \n
	--> /Cafetería \n
	--> /UTICS \n
	--> /Centro_para_las_Artes \n
	--> /Innova_TecNM
	''')


def sistemas(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')
    

def Centro_de_Idiomas(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def Departamento_de_ingeniería_Industrial(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def vinculacion(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'vinculacion.jpg', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')

def Aulas_Ingeniería_Industrial_B(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def Edificio_Ingeniería_Industrial(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def Cafetería(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def UTICS(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def Centro_para_las_Artes(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def Innova_TecNM(update, context):
    context.bot.sendVideo(chat_id=update.message['chat']['id'], video=open(
        'prueba.png', 'rb'), filename='about.png', caption='Hola, te envio este video, miralo!')


def main():
    updater = Updater('5355902687:AAFfQtANKiNyGc7bd8QIy98Qz8dURToJ-mw', use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start',	start))
    dp.add_handler(CommandHandler('helpMe',	helpMe))
    dp.add_handler(CommandHandler('Edificio_sistemas', sistemas))
    dp.add_handler(CommandHandler('Centro_de_Idiomas', Centro_de_Idiomas))
    dp.add_handler(CommandHandler('vinculacion', vinculacion))
    # dp.add_handler(CommandHandler(
    # 'Edificio_de_Gestión_y_Vinculación', Edificio_de_Gestión_y_Vinculación))
    # dp.add_handler(CommandHandler(
    # 'Aulas_Ingeniería_Industrial_B', Aulas_Ingeniería_Industrial_B))
    # dp.add_handler(CommandHandler(
    # 'Edificio_Ingeniería_Industrial', Edificio_Ingeniería_Industrial))
    # dp.add_handler(CommandHandler('Cafetería', Cafetería))
    # dp.add_handler(CommandHandler('UTICS', UTICS))
    # dp.add_handler(CommandHandler(
    # 'Centro_para_las_Artes', Centro_para_las_Artes))
    # dp.add_handler(CommandHandler('Innova_TecNM', Innova_TecNM))
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()


if __name__ == '__main__':
    main()
