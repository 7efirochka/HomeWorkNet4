import telebot

token = "6582094526:AAHHpRMEIsMHKqIlyWvQzs2LnqqmdaZiTg8"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):

    if "Lada" in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)
    # bot.send_message(message.chat.id, ssa)

bot.polling(none_stop=True)





