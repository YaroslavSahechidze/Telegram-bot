from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
import pprint
import io


pp = pprint.PrettyPrinter(indent=4)

# Установка необходимых данных для авторизации
CLIENT_SECRET_FILE = 'botss-391914-f2d939634069.json'  # Путь к файлу с клиентскими данными
API_NAME = 'drive'
API_VERSION = 'v3'

bot = Bot('5861903747:AAFIL302XS4rSeHKkHb_fqTz_27eH1Eh_s0')
dp = Dispatcher(bot)

# Функция для загрузки фото с Google Диска
def download_from_drive(file_id, file_name):
    # Авторизация и создание экземпляра сервиса Google Диска
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=['https://www.googleapis.com/auth/drive'])
    service = build(API_NAME, API_VERSION, credentials=credentials)

    # Загрузка фото
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()

# Команда для начала диалога и вывода основных кнопок с мероприятиями
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('02.05 Спортивный день 10:00-14:00')
    btn2 = types.KeyboardButton('02.05 Научный вечер 18:00-20:20')
    keyboard.row(btn1, btn2)
    btn3 = (types.KeyboardButton('03.05 Мафия 15:00-17:20'))
    btn4 = (types.KeyboardButton('03.05 Мелотрек 18:00-20:20'))
    keyboard.row(btn3, btn4)

    # Ввод ID файлов и имен файлов для загрузки
    file_id = ['1grRUmv80hT5fMA3vFeSKRDUM3DBr9Qcj',
               '1dIlphX9wvqhOgRPtSMECzfQQbzcxUfiL',
               '1nDyl5ppPrKJVnR2h2cHRRhyFp0ca6yXi',
               '1GETv1zeMJsuemCZH2aYOg035M7GzN6Gl']  # ID файла на Google Диске

    file_name = ['sportday.jpg',
                 'science.jpg',
                 'mafia.jpg',
                 'melotrack.jpg']  # Имя файла для сохранения

    # Загрузка файлов с Google Диска
    [download_from_drive(file_id[i], file_name[i]) for i in range(4)]
    text_id = ['1fTbVh6bTa_Hyqj-QSoMax0M5N9VtQbgt',
               '1MAVXCfeOglFyM6xxzTABGbPgXvB3WfqZ',
               '1qMS-4ckl4US566UzU1sPpZ4T8MhUh6vs',
               '1eFUrdQZC2c6aG-_osu9zo6h9eobrAJQh']

    text_name = ['sportday.txt',
                 'science.txt',
                 'mafia.txt',
                 'melotrack.txt']

    [download_from_drive(text_id[i], text_name[i]) for i in range(4)]

    await message.answer('Привет! Это Студсоюз Мехмата, рады тебя видеть! На какое мероприятие ты бы хотел зарегистрироваться?', reply_markup=keyboard)

# Команда для обработки нажатия reply-кнопок
@dp.message_handler(content_types=['text'])
async def text(message: types.Message):

    if message.text == '02.05 Спортивный день 10:00-14:00':
        keyboard = InlineKeyboardMarkup() # создание inline-клавиатуры
        btn1 = InlineKeyboardButton('Регистрация на футбол', url='https://forms.gle/G9DMNYZ2WGwnKqHp8')
        btn2 = InlineKeyboardButton('Регистрация на волейбол', url='https://forms.gle/oWuiWKtNT8ESmfQh9')
        keyboard.row(btn1, btn2)
        file = open('sportday.jpg', 'rb')
        with open('sportday.txt', 'r', encoding='utf-8') as f: # парсинг текстового документа
            text = f.readlines()
            for i in range(len(text)):
                if str('\n') in text[i]:
                    text[i] = text[i][:-1]
            text = str("\n").join(text)
        await bot.send_photo(message.chat.id, file, caption=text, reply_markup=keyboard)

    elif message.text == '02.05 Научный вечер 18:00-20:20':
        keyboard = InlineKeyboardMarkup() # создание inline-клавиатуры
        keyboard.add(InlineKeyboardButton('Регистрация на научный вечер', url='https://forms.gle/cQuXs698fuKxJ88s7'))
        file = open('science.jpg', 'rb')
        with open('science.txt', 'r', encoding='utf-8') as f: # парсинг текстового документа
            text = f.readlines()
            for i in range(len(text)):
                if str('\n') in text[i]:
                    text[i] = text[i][:-1]
            text = str("\n").join(text)
        await bot.send_photo(message.chat.id, file, caption=text, reply_markup=keyboard)

    elif message.text == '03.05 Мафия 15:00-17:20':
        keyboard = InlineKeyboardMarkup() # создание inline-клавиатуры
        keyboard.add(InlineKeyboardButton('Регистрация на мафию', url='https://forms.gle/vA8TBDP9xtsA9rw3A'))
        file = open('mafia.jpg', 'rb')
        with open('mafia.txt', 'r', encoding='utf-8') as f: # парсинг текстового документа
            text = f.readlines()
            for i in range(len(text)):
                if str('\n') in text[i]:
                    text[i] = text[i][:-1]
            text = str("\n").join(text)
        await bot.send_photo(message.chat.id, file, caption=text, reply_markup=keyboard)

    elif message.text == '03.05 Мелотрек 18:00-20:20':
        keyboard = InlineKeyboardMarkup() # создание inline-клавиатуры
        keyboard.add(InlineKeyboardButton('Регистрация на мелотрек', url= 'https://forms.gle/sj5EsduEyZ1xp9nM6'))
        file = open('melotrack.jpg', 'rb')
        with open('melotrack.txt', 'r', encoding='utf-8') as f: # парсинг текстового документа
            text = f.readlines()
            for i in range(len(text)):
                if str('\n') in text[i]:
                    text[i] = text[i][:-1]
            text = str("\n").join(text)
        await bot.send_photo(message.chat.id, file, caption=text, reply_markup=keyboard)

    else:
        await message.answer('Выберите мероприятие из предложенных ниже.') # условная обработка исключения

@dp.callback_query_handler() # обработка нажатия на inline-кнопку
async def callback(call):
    await call.message.answer(call.data)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
