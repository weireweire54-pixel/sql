# # # # # # # # # import sqlite3 # Подключаем встроенную базу данных

# # # # # # # # # # 1. Подключаемся к файлу базы данных (если файла нет, Python его создаст)
# # # # # # # # # connection = sqlite3.connect("bot_users.db")

# # # # # # # # # # 2. Создаем специальный инструмент для выполнения команд — курсор
# # # # # # # # # cursor = connection.cursor()

# # # # # # # # # # 3. Пишем команду на языке SQL, которая создаст таблицу users (если её ещё нет)
# # # # # # # # # cursor.execute("""
# # # # # # # # # CREATE TABLE IF NOT EXISTS users (
# # # # # # # # #     id INTEGER PRIMARY KEY,
# # # # # # # # #     name TEXT,
# # # # # # # # #     city TEXT
# # # # # # # # # )
# # # # # # # # # """)

# # # # # # # # # # 4. Сохраняем изменения и закрываем соединение
# # # # # # # # # connection.commit()
# # # # # # # # # connection.close()
# # # # # # # # import sys; sys.stdout.reconfigure(encoding='utf-8')

# # # # # # # # import sqlite3

# # # # # # # # connection = sqlite3.connect("bot_users.db")
# # # # # # # # cursor = connection.cursor()

# # # # # # # # # Пишем SQL-команду для добавления данных
# # # # # # # # # Нам нужно заполнить колонки name и city конкретными значениями
# # # # # # # # cursor.execute("""
# # # # # # # # INSERT INTO users (name, city) 
# # # # # # # # VALUES ('Daur', 'Almaty')
# # # # # # # # """)

# # # # # # # # # КРИТИЧЕСКИ ВАЖНО: commit сохраняет изменения в самом файле базы данных
# # # # # # # # connection.commit()
# # # # # # # # connection.close()

# # # # # # # # print("Пользователь успешно добавлен в базу!")


# # # # # # import sqlite3
# # # # # # import sys; sys.stdout.reconfigure(encoding='utf-8') # Защита от закорючек!

# # # # # # connection = sqlite3.connect("bot_users.db")
# # # # # # cursor = connection.cursor()

# # # # # # # 1. Пишем команду: ВЫБРАТЬ все колонки ИЗ таблицы users
# # # # # # cursor.execute("SELECT * FROM users")

# # # # # # # 2. Метод fetchall() забирает все найденные строки и превращает их в список Python
# # # # # # all_users = cursor.fetchall()

# # # # # # # 3. Перебираем список через цикл for и выводим на экран
# # # # # # for user in all_users:
# # # # # #     print(f"ID: {user[0]} | Имя: {user[1]} | Город: {user[2]}")

# # # # # # connection.close()

# # # # # # import sqlite3
# # # # # # import sys; sys.stdout.reconfigure(encoding='utf-8') # Защита от закорючек!

# # # # # # connection = sqlite3.connect("bot_users.db")
# # # # # # cursor = connection.cursor()

# # # # # # # Пишем команду: УДАЛИТЬ ИЗ таблицы users ГДЕ id равен 1
# # # # # # cursor.execute("DELETE FROM users WHERE id = 3")

# # # # # # # КРИТИЧЕСКИ ВАЖНО: сохраняем изменения в файле базы данных
# # # # # # connection.commit()
# # # # # # connection.close()

# # # # # # print("Строка успешно удалена!")


# # # # # # import sqlite3

# # # # # # connection = sqlite3.connect("bot_users.db")
# # # # # # cursor = connection.cursor()

# # # # # # # Пишем команду: ОБНОВИТЬ таблицу users, УСТАНОВИТЬ город 'Astana' ГДЕ id равен 2
# # # # # # cursor.execute("""
# # # # # # UPDATE users 
# # # # # # SET city = 'Astana' 
# # # # # # WHERE id = 2
# # # # # # """)

# # # # # # # Сохраняем изменения в базе
# # # # # # connection.commit()
# # # # # # connection.close()

# # # # # # print("Данные успешно изменены!")


# # # # # import asyncio
# # # # # import sys
# # # # # from aiogram import Bot, Dispatcher, types
# # # # # from aiogram.filters import CommandStart

# # # # # # Защита от закорючек в терминале Windows
# # # # # sys.stdout.reconfigure(encoding='utf-8')

# # # # # # Вставляем ваш токен, который выдал BotFather
# # # # # TOKEN = "8925987850:AAGkvHlY8i4t5IUjcHAHRruneBILQT6EWqQ"

# # # # # # Создаем объекты бота и диспетчера (он отвечает за прием сообщений)
# # # # # bot = Bot(token=TOKEN)
# # # # # dp = Dispatcher()

# # # # # # Этот хэндлер (обработчик) срабатывает, когда пользователь пишет /start
# # # # # @dp.message(CommandStart())
# # # # # async def cmd_start(message: types.Message):
# # # # #     # Бот вежливо отвечает пользователю и использует его имя из Telegram
# # # # #     await message.answer(f"Салам, {message.from_user.first_name}! Я твой первый бот на Python. Чем могу помочь?")

# # # # # # Этот хэндлер будет ловить любые текстовые сообщения
# # # # # @dp.message()
# # # # # async def echo_message(message: types.Message):
# # # # #     # message.text — это тот текст, который вам прислал пользователь
# # # # #     user_text = message.text
    
# # # # #     # Отправляем этот же текст обратно пользователю
# # # # #     await message.answer(f"Вы написали мне: {user_text}")


# # # # # # Главная функция, которая запускает постоянный опрос серверов Telegram
# # # # # async def main():
# # # # #     print("Бот успешно запущен и слушает команды...")
# # # # #     await dp.start_polling(bot)

# # # # # # Запуск асинхронного кода
# # # # # if __name__ == "__main__":
# # # # #     asyncio.run(main())

# # # # import asyncio
# # # # import sys
# # # # import sqlite3
# # # # from aiogram import Bot, Dispatcher, types
# # # # from aiogram.filters import CommandStart

# # # # sys.stdout.reconfigure(encoding='utf-8')

# # # # TOKEN = "8925987850:AAGkvHlY8i4t5IUjcHAHRruneBILQT6EWqQ"
# # # # bot = Bot(token=TOKEN)
# # # # dp = Dispatcher()

# # # # # Обработчик команды /start
# # # # @dp.message(CommandStart())
# # # # async def cmd_start(message: types.Message):
# # # #     # 1. Забираем данные пользователя из Telegram
# # # #     user_id = message.from_user.id
# # # #     user_name = message.from_user.first_name
# # # #     default_city = "Не указан" # Город пока поставим по умолчанию
    
# # # #     # 2. Подключаемся к нашей базе данных
# # # #     connection = sqlite3.connect("bot_users.db")
# # # #     cursor = connection.cursor()
    
# # # #     # 3. Записываем пользователя в таблицу (используем безопасный метод с подстановкой ?)
# # # #     try:
# # # #         cursor.execute("""
# # # #         INSERT INTO users (id, name, city) 
# # # #         VALUES (?, ?, ?)
# # # #         """, (user_id, user_name, default_city))
        
# # # #         connection.commit()
# # # #         reply_text = f"Салам, {user_name}! Ты успешно зарегистрирован в базе данных!"
# # # #     except sqlite3.IntegrityError:
# # # #         # Если пользователь с таким ID уже есть в базе, выскочит эта ошибка
# # # #         reply_text = f"Рад видеть тебя снова, {user_name}! Ты уже есть в нашей базе."
        
# # # #     connection.close()
    
# # # #     # 4. Отвечаем пользователю в Telegram
# # # #     await message.answer(reply_text)

# # # # # Хэндлер эхо-бота (оставляем его ниже)
# # # # @dp.message()
# # # # async def echo_message(message: types.Message):
# # # #     await message.answer(f"Вы написали мне: {message.text}")

# # # # async def main():
# # # #     print("Бот со связкой SQL успешно запущен...")
# # # #     await dp.start_polling(bot)

# # # # if __name__ == "__main__":
# # # #     asyncio.run(main())


# # # import asyncio
# # # import sys
# # # import sqlite3
# # # from aiogram import Bot, Dispatcher, types
# # # from aiogram.filters import CommandStart
# # # # Подключаем инструменты для создания кнопок
# # # from aiogram.utils.keyboard import ReplyKeyboardBuilder

# # # sys.stdout.reconfigure(encoding='utf-8')

# # # TOKEN = "8925987850:AAGkvHlY8i4t5IUjcHAHRruneBILQT6EWqQ"
# # # bot = Bot(token=TOKEN)
# # # dp = Dispatcher()

# # # # Обработчик команды /start с кнопками
# # # @dp.message(CommandStart())
# # # async def cmd_start(message: types.Message):
# # #     user_id = message.from_user.id
# # #     user_name = message.from_user.first_name
# # #     default_city = "Не указан"
    
# # #     connection = sqlite3.connect("bot_users.db")
# # #     cursor = connection.cursor()
    
# # #     try:
# # #         cursor.execute("INSERT INTO users (id, name, city) VALUES (?, ?, ?)", (user_id, user_name, default_city))
# # #         connection.commit()
# # #         reply_text = f"Салам, {user_name}! Ты успешно зарегистрирован!"
# # #     except sqlite3.IntegrityError:
# # #         reply_text = f"Рад видеть тебя снова, {user_name}!"
        
# # #     connection.close()
    
# # #     # --- СОЗДАЕМ КНОПКИ ---
# # #     builder = ReplyKeyboardBuilder()
# # #     builder.button(text="👤 Мой профиль")
# # #     builder.button(text="❓ Помощь")
# # #     # adjust(2) говорит боту расположить 2 кнопки в один ряд
# # #     builder.adjust(2)
    
# # #     # Отправляем сообщение вместе с кнопками (генерация через as_markup)
# # #     await message.answer(reply_text, reply_markup=builder.as_markup(resize_keyboard=True))


# # # # Хэндлер эхо-бота (будет ловить нажатия на кнопки как обычный текст)
# # # @dp.message()
# # # async def echo_message(message: types.Message):
# # #     await message.answer(f"Вы нажали кнопку или написали: {message.text}")

# # # async def main():
# # #     print("Бот с кнопками успешно запущен...")
# # #     await dp.start_polling(bot)

# # # if __name__ == "__main__":
# # #     asyncio.run(main())


# # import asyncio
# # import sys
# # import sqlite3
# # from aiogram import Bot, Dispatcher, types, F  # Импортируем F для фильтрации текста
# # from aiogram.filters import CommandStart
# # from aiogram.utils.keyboard import ReplyKeyboardBuilder

# # sys.stdout.reconfigure(encoding='utf-8')

# # TOKEN = "8925987850:AAGkvHlY8i4t5IUjcHAHRruneBILQT6EWqQ"
# # bot = Bot(token=TOKEN)
# # dp = Dispatcher()

# # @dp.message(CommandStart())
# # async def cmd_start(message: types.Message):
# #     user_id = message.from_user.id
# #     user_name = message.from_user.first_name
# #     default_city = "Не указан"
    
# #     connection = sqlite3.connect("bot_users.db")
# #     cursor = connection.cursor()
# #     try:
# #         cursor.execute("INSERT INTO users (id, name, city) VALUES (?, ?, ?)", (user_id, user_name, default_city))
# #         connection.commit()
# #         reply_text = f"Салам, {user_name}! Ты успешно зарегистрирован!"
# #     except sqlite3.IntegrityError:
# #         reply_text = f"Рад видеть тебя снова, {user_name}!"
# #     connection.close()
    
# #     builder = ReplyKeyboardBuilder()
# #     builder.button(text="👤 Мой профиль")
# #     builder.button(text="❓ Помощь")
# #     builder.adjust(2)
    
# #     await message.answer(reply_text, reply_markup=builder.as_markup(resize_keyboard=True))


# # # --- ОБРАБОТЧИК КНОПКИ «МОЙ ПРОФИЛЬ» ---
# # @dp.message(F.text == "👤 Мой профиль")
# # async def show_profile(message: types.Message):
# #     user_id = message.from_user.id
    
# #     # Идем в базу данных за информацией о пользователе
# #     connection = sqlite3.connect("bot_users.db")
# #     cursor = connection.cursor()
    
# #     # Ищем строку именно с этим ID
# #     cursor.execute("SELECT name, city FROM users WHERE id = ?", (user_id,))
# #     user_data = cursor.fetchone() # fetchone() забирает ОДНУ найденную строку
# #     connection.close()
    
# #     if user_data:
# #         name = user_data[0]
# #         city = user_data[1]
# #         await message.answer(f"📋 Ваш профиль:\n\n👤 Имя: {name}\n🏢 Город: {city}\n🆔 Ваш ID: {user_id}")
# #     else:
# #         await message.answer("Ошибка: профиль не найден в базе данных. Нажмите /start заново.")


# # # --- ОБРАБОТЧИК КНОПКИ «ПОМОЩЬ» ---
# # @dp.message(F.text == "❓ Помощь")
# # async def show_help(message: types.Message):
# #     await message.answer("🤖 Это тестовый бот на Python.\n\nОн умеет регистрировать вас в базе данных SQLite и показывать ваш профиль.")


# # async def main():
# #     print("Умный бот со связкой кнопок и SQL запущен...")
# #     await dp.start_polling(bot)

# # if __name__ == "__main__":
# #     asyncio.run(main())


# import asyncio
# import sys
# import sqlite3
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import CommandStart
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
# # Импортируем инструменты для машины состояний (FSM)
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext

# sys.stdout.reconfigure(encoding='utf-8')

# TOKEN = "8925987850:AAGkvHlY8i4t5IUjcHAHRruneBILQT6EWqQ"
# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# # 1. Создаем класс состояний
# class UserForm(StatesGroup):
#     waiting_for_city = State()  # Состояние «Ожидание ввода города»

# @dp.message(CommandStart())
# async def cmd_start(message: types.Message):
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     default_city = "Не указан"
    
#     connection = sqlite3.connect("bot_users.db")
#     cursor = connection.cursor()
#     try:
#         cursor.execute("INSERT INTO users (id, name, city) VALUES (?, ?, ?)", (user_id, user_name, default_city))
#         connection.commit()
#         reply_text = f"Салам, {user_name}! Ты успешно зарегистрирован!"
#     except sqlite3.IntegrityError:
#         reply_text = f"Рад видеть тебя снова, {user_name}!"
#     connection.close()
    
#     # Добавили третью кнопку для изменения города
#     builder = ReplyKeyboardBuilder()
#     builder.button(text="👤 Мой профиль")
#     builder.button(text="✏️ Изменить город")
#     builder.button(text="❓ Помощь")
#     builder.adjust(2, 1) # 2 кнопки в первом ряду, 1 во втором
    
#     await message.answer(reply_text, reply_markup=builder.as_markup(resize_keyboard=True))

# @dp.message(F.text == "👤 Мой профиль")
# async def show_profile(message: types.Message):
#     user_id = message.from_user.id
#     connection = sqlite3.connect("bot_users.db")
#     cursor = connection.cursor()
#     cursor.execute("SELECT name, city FROM users WHERE id = ?", (user_id,))
#     user_data = cursor.fetchone()
#     connection.close()
    
#     if user_data:
#         await message.answer(f"📋 Ваш профиль:\n\n👤 Имя: {user_data[0]}\n🏢 Город: {user_data[1]}\n🆔 Ваш ID: {user_id}")

# # --- 2. ВКЛЮЧАЕМ РЕЖИМ ОЖИДАНИЯ ГОРОДА ---
# @dp.message(F.text == "✏️ Изменить город")
# async def change_city_request(message: types.Message, state: FSMContext):
#     await message.answer("Напишите название вашего города (например: Алматы или Астана):")
#     # Приказываем боту включить состояние ожидания для этого юзера
#     await state.set_state(UserForm.waiting_for_city)

# # --- 3. ЛОВИМ НАЗВАНИЕ ГОРОДА И ОБНОВЛЯЕМ БАЗУ ---
# @dp.message(UserForm.waiting_for_city)
# async def save_city_to_db(message: types.Message, state: FSMContext):
#     user_city = message.text  # Забираем то, что написал юзер
#     user_id = message.from_user.id
    
#     # Обновляем базу данных командой UPDATE
#     connection = sqlite3.connect("bot_users.db")
#     cursor = connection.cursor()
#     cursor.execute("UPDATE users SET city = ? WHERE id = ?", (user_city, user_id))
#     connection.commit()
#     connection.close()
    
#     # Сбрасываем состояние (выключаем режим ожидания)
#     await state.clear()
#     await message.answer(f"Город успешно изменен на: {user_city}! Проверьте профиль.")

# @dp.message(F.text == "❓ Помощь")
# async def show_help(message: types.Message):
#     await message.answer("🤖 Бот умеет сохранять ваш город в базу данных SQLite.")

# async def main():
#     print("Бот со Стейтами (FSM) успешно запущен...")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())



import asyncio
import sys
import sqlite3
import os  # Импортируем стандартную библиотеку для работы с системой
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv  # Подключаем dotenv

sys.stdout.reconfigure(encoding='utf-8')

# Загружаем переменные из файла .env
load_dotenv()

# Вытаскиваем токен из скрытого файла окружения
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен успешно считался (критическое мышление!)
if not TOKEN:
    sys.exit("Ошибка: Токен бота не найден в файле .env!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

class UserForm(StatesGroup):
    waiting_for_city = State()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    default_city = "Не указан"
    
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (id, name, city) VALUES (?, ?, ?)", (user_id, user_name, default_city))
        connection.commit()
        reply_text = f"Салам, {user_name}! Ты успешно зарегистрирован!"
    except sqlite3.IntegrityError:
        reply_text = f"Рад видеть тебя снова, {user_name}!"
    connection.close()
    
    builder = ReplyKeyboardBuilder()
    builder.button(text="👤 Мой профиль")
    builder.button(text="✏️ Изменить город")
    builder.button(text="❓ Помощь")
    builder.adjust(2, 1)
    
    await message.answer(reply_text, reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text == "👤 Мой профиль")
async def show_profile(message: types.Message):
    user_id = message.from_user.id
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name, city FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    connection.close()
    
    if user_data:
        await message.answer(f"📋 Ваш профиль:\n\n👤 Имя: {user_data[0]}\n🏢 Город: {user_data[1]}\n🆔 Ваш ID: {user_id}")

@dp.message(F.text == "✏️ Изменить город")
async def change_city_request(message: types.Message, state: FSMContext):
    await message.answer("Напишите название вашего города (например: Алматы или Астана):")
    await state.set_state(UserForm.waiting_for_city)

@dp.message(UserForm.waiting_for_city)
async def save_city_to_db(message: types.Message, state: FSMContext):
    user_city = message.text
    user_id = message.from_user.id
    
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET city = ? WHERE id = ?", (user_city, user_id))
    connection.commit()
    connection.close()
    
    await state.clear()
    await message.answer(f"Город успешно изменен на: {user_city}! Проверьте профиль.")

@dp.message(F.text == "❓ Помощь")
async def show_help(message: types.Message):
    await message.answer("🤖 Бот умеет сохранять ваш город в базу данных SQLite.")

async def main():
    print("Безопасный бот со скрытым токеном успешно запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
