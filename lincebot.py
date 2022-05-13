from telegram.ext import (Updater, CommandHandler)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
    

	context.bot.send_message(update.message.chat_id, '''!Hola lince \U0001F44B \U0001F44B!, soy un ChatBot(Lincebot) \U0001F916 \n\n
		Seré tu guía virtual de las instalaciones del Tecnológico Nacional de México en Celaya Campus 2. \U0001F431 \U0001F431 \n\n
		Para ayudarte a encontrar el edificio que gustes puedes preguntarme/escribirme de la siguiente manera: \"¿Edificio -Tu destino-?\". \U0001F6B6 \U0001F6B6 \n\n
		Ejemplos: ¿Edificio Sistemas?, ¿Edificio Cafetería?, ¿Edificio Asociaciones?\U0001F3EB  \n\n
		Espero pueda ayudarte a encontrar tu destino, Orgullosamente Linces! \U0001F9BE \U0001F431''')
print("Mensaje Enviado con exito!")

def main():
	TOKEN="5355902687:AAFfQtANKiNyGc7bd8QIy98Qz8dURToJ-mw"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	dp.add_handler(CommandHandler('start',	start))

	# Comienza el bot
	updater.start_polling()
	# Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	main()
