from telegram.ext import (Updater, CommandHandler)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
    print("enviado")
	context.bot.send_message(update.message.chat_id, "Bienvenido")

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