from telegram.ext import CommandHandler
from telegram.ext import Application

# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot de Telegram
BOT_TOKEN = '6718203881:AAHglMpdnxv382DmXMwt1L8i4-gG6ere9ao'

# Manejador para el comando /sendexcel
def send_excel(update, context):
    user_id = update.effective_user.id

    # Reemplaza con la ruta de tu archivo Excel
    excel_file_path = 'C:/Users/Fernando/OneDrive/Documentos/PythonProjects/Python/eigenseed_telegrambots/EigenSeedTelegram/BabaBooey.xlsx'

    # Envía el archivo de Excel al usuario
    update.message.reply_document(document=open(excel_file_path))

def main():
    # Crea una aplicación usando Application.builder()
    app = Application.builder().token(BOT_TOKEN).build()

    # Agrega el manejador para el comando /sendexcel
    app.add_handler(CommandHandler('enviarexcel', send_excel))

    # Inicia la aplicación
    app.run_polling()

if __name__ == '__main__':
    main()