from aiogram import Bot, Dispatcher, executor, types
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import openpyxl
pp = pprint.PrettyPrinter(indent=4)

# Установка необходимые данные для авторизации
CLIENT_SECRET_FILE = 'botss-391914-f2d939634069.json'  # Путь к файлу с клиентскими данными
API_NAME = 'drive'
API_VERSION = 'v3'

bot = Bot('6320096781:AAF6hrJovqSkabJB1M9WpQm0X-IaAdfixOM')
dp = Dispatcher(bot)

# Функция для загрузки фото с Google Диска
def download_from_drive(file_id, file_name):
    # Авторизация и создание экземпляра сервиса Google Диска
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=['https://www.googleapis.com/auth/drive'])
    service = build(API_NAME, API_VERSION, credentials=credentials)

    file_id = '1HGS-VUCGd0XPsbvXMSXJTMu7NmNsKQpux-E_LDyNNNU'
    request = service.files().export_media(fileId=file_id,
                                                mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = 'eventsMMF.xlsx'
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))

# Команда для начала диалога и вывода основных кнопок с мероприятиями
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('02.05 Футбол 10:00-14:00')
    btn2 = types.KeyboardButton('02.05 Волейбол 10:00-14:00')
    btn3 = types.KeyboardButton('02.05 Научный вечер 18:00-20:20')
    keyboard.row(btn1, btn2, btn3)
    btn4 = (types.KeyboardButton('03.05 Мафия 15:00-17:20'))
    btn5 = (types.KeyboardButton('03.05 Мелотрек 18:00-20:20'))
    keyboard.row(btn4, btn5)

    # Ввод ID файлов и имен файлов для загрузки

    file_id = '1HGS-VUCGd0XPsbvXMSXJTMu7NmNsKQpux-E_LDyNNNU'

    file_name = 'eventsMMF.xlsx'

    # Загрузка файлов с Google Диска
    download_from_drive(file_id, file_name)

    await message.answer('Привет, организатор мероприятий ММФ. Информацию по какому мероприятию хочешь просмотреть?', reply_markup=keyboard)

# Команда для обработки нажатия inline-кнопок
@dp.message_handler(content_types=['text'])
async def text(message: types.Message):

    if message.text == '02.05 Футбол 10:00-14:00':
        book = openpyxl.open('eventsMMF.xlsx', read_only=True) # связь с гугл таблицей на гугл диске
        sheet= book.worksheets[1]

        spis = ''
        try:
            for i in range(2, 1000): # парсинг таблицы
                spis += sheet[i][1].value + '\n'
        except:
            spis += "Всего {} участников".format(i-2)
            await message.answer(spis)

    elif message.text == '02.05 Волейбол 18:00-20:20':
        book = openpyxl.open('eventsMMF.xlsx', read_only=True) # связь с гугл таблицей на гугл диске
        sheet= book.worksheets[2]

        spis = ''
        try:
            for i in range(2, 1000): # парсинг таблицы
                spis += sheet[i][1].value + '\n'
        except:
            spis += "Всего {} участников".format(i-2)
            await message.answer(spis)

    if message.text == '02.05 Научный вечер 18:00-20:20':
        book = openpyxl.open('eventsMMF.xlsx', read_only=True) # связь с гугл таблицей на гугл диске
        sheet = book.worksheets[3]

        spis = ''
        try:
            for i in range(2, 1000): # парсинг таблицы
                spis += sheet[i][1].value + '\n'
        except:
            spis += "Всего {} участников".format(i-2)
            await message.answer(spis)

    elif message.text == '03.05 Мафия 15:00-17:20':
        book = openpyxl.open('eventsMMF.xlsx', read_only=True) # связь с гугл таблицей на гугл диске
        sheet = book.worksheets[4]

        spis = ''
        try:
            for i in range(2, 1000): # парсинг таблицы
                spis += sheet[i][1].value + '\n'
        except:
            spis += "Всего {} участников".format(i-2)
            await message.answer(spis)

    elif message.text == '03.05 Мелотрек 18:00-20:20':
        book = openpyxl.open('eventsMMF.xlsx', read_only=True) # связь с гугл таблицей на гугл диске
        sheet = book.worksheets[5]

        spis = ''
        try:
            for i in range(2, 1000): # парсинг таблицы
                spis += sheet[i][1].value + '\n'
        except:
            spis += "Всего {} участников".format(i-2) # условная обработка исключения
            await message.answer(spis)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
