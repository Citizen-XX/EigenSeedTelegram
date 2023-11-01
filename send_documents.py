from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler, CallbackQueryHandler, ConversationHandler
from telegram.constants import ParseMode
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, Update

# Reemplaza 'TOKEN' con el token de tu bot de Telegram
TOKEN = '6718203881:AAHglMpdnxv382DmXMwt1L8i4-gG6ere9ao'

# Manejador para el comando /enviarexcel
def send_excel(update, context):
    user_id = update.effective_user.id
    doc_file = open('C:/Users/Fernando/OneDrive/Documentos/PythonProjects/Python/eigenseed_telegrambots/EigenSeedTelegram/BabaBooey.xlsx', 'rb')

    # Reemplaza con la ruta de tu archivo Excel
    # excel_file_path = 'C:/Users/Fernando/OneDrive/Documentos/PythonProjects/Python/eigenseed_telegrambots/EigenSeedTelegram/BabaBooey.xlsx'

    # Envía el archivo de Excel al usuario
    # update.message.send_document(chat_id=user_id, document = excel_file_path)
    # update.message.reply_document(document=open(excel_file_path))
    return context.bot.send_document(user_id, doc_file)

def main():
    # Crea una aplicación usando Application.builder()
    app = Application.builder().token(TOKEN).build()

    # Agrega el manejador para el comando /enviarexcel
    app.add_handler(CommandHandler('enviarexcel', send_excel))

    # Inicia la aplicación
    app.run_polling()

if __name__ == '__main__':
    main()