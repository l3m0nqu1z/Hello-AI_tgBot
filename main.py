import os, logging, openai
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def handle_message(update, context):
    user_input = update.message.text
    logging.info(user_input)
    response = generate_response(user_input)
    update.message.reply_text(response)

openai.api_key = os.environ['GPT_KEY']

def generate_response(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": user_input
            }
        ]
    )

    chat_response = completion.choices[0].message.content
    logging.info(chat_response)
    return chat_response

updater = Updater(os.environ['TGBOT_KEY'])

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling()
updater.idle()
