import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# API Token من BotFather
telegram_token = 'TELEGRAM_BOT_TOKEN'
openai_api_key = 'OPENAI_API_KEY'

openai.api_key = openai_api_key

# إرسال الرسالة إلى ChatGPT واستلام الرد
def ask_chatgpt(question):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=question,
      max_tokens=150
    )
    return response.choices[0].text.strip()

# الاستجابة للرسائل الواردة من المستخدم
def handle_message(update, context):
    user_message = update.message.text
    response = ask_chatgpt(user_message)
    update.message.reply_text(response)

# بدء البوت
def main():
    updater = Updater(telegram_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
