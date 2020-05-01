from telegram.ext import Updater, CommandHandler

def welcome(updater, context):
    message= 'Oi meu mestre,\n o que deseja'
    print(message)
    context.bot.send_message(chat_id=updater.effective_chat.id, text= message)
    
def main():
    token = '1165215955:AAES292Q4BwqUEcbddy5aC2uAXjCZFr6vQM'
    updater = Updater(token=token,use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == '__main__':
    main()