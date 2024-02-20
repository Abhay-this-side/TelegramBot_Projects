import telebot
import mysql.connector
import os
import requests

# Function to download a file from a URL and save it to a local path
def download_file(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

# Telegram bot token (obtain from BotFather)
TOKEN = '6604980552:AAFEBOLWJAjeDmDvKcaqTiS1cC_Im9SlmKQ'

# MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'parker@5'
DB_NAME = 'telegram_bot'

# Supported languages (modify as needed)
SUPPORTED_LANGUAGES = ['python', 'c++', 'javascript', 'html', 'css']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm your language PDF helper. To get started, enter '/language' followed by the programming language you're interested in (e.g., /language python).")

@bot.message_handler(commands=['language'])
def handle_language(message):
    chat_id = message.chat.id
    text = message.text.lower()

    # Check for valid language request
    if len(text.split()) != 2 or text.split()[1] not in SUPPORTED_LANGUAGES:
        bot.send_message(chat_id, "Sorry, I only have PDFs for these languages: " + ', '.join(SUPPORTED_LANGUAGES))
        return

    language = text.split()[1]

    # Connect to MySQL database
    try:
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            auth_plugin='mysql_native_password'
        )
        mycursor = mydb.cursor()

        # Fetch PDF file URL from database (replace 'language' with your table and column names)
        sql = f"SELECT pdf_path FROM language_pdf WHERE language = '{language}'"
        mycursor.execute(sql)
        pdf_url = mycursor.fetchone()

        if pdf_url is not None:
            # Download the PDF file
            local_path = 'temp.pdf'
            if download_file(pdf_url[0], local_path):
                # Send the downloaded PDF file
                with open(local_path, 'rb') as pdf:
                    bot.send_document(chat_id, pdf)
                # Remove the temporary file
                os.remove(local_path)
            else:
                bot.send_message(chat_id, "Sorry, I couldn't download the PDF file.")
        else:
            bot.send_message(chat_id, f"Sorry, I couldn't find a PDF for {language}.")

    except mysql.connector.Error as err:
        bot.send_message(chat_id, f"Error connecting to database: {err}")
    finally:
        if mydb.is_connected():
            mydb.close()

bot.infinity_polling()
