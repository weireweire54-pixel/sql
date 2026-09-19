from fastapi import FastAPI

# Создаем объект приложения FastAPI
app = FastAPI()

# Говорим серверу: если пользователь зашел на главную страницу сайта (просто "/")
@app.get("/")
def home():
    # Возвращаем данные в формате JSON (как в базах данных)
    return {"message": "Салам! Это мой первый бэкенд-сайт на FastAPI!"}

# Вторая страница нашего сайта (например, "/job")
@app.get("/job")
def get_job_info():
    return {
        "position": "Python Junior Developer",
        "salary": "450 000 KZT",
        "status": "Ready for offer"
    }

# Новая страница сайта: "/hello"
@app.get("/hello")
def say_hello(name: str):
    # str означает, что мы ожидаем текст (строку)
    return {"message": f"Салам, {name}! Добро пожаловать на наш сервер!"}


import sqlite3

# Создаем страницу "/users"
@app.get("/users")
def get_all_users():
    # 1. Подключаемся к файлу базы данных, который лежит в нашей папке
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    
    # 2. Достаем всех пользователей
    cursor.execute("SELECT id, name, city FROM users")
    rows = cursor.fetchall()
    connection.close()
    
    # 3. Упаковываем данные из базы в красивый список словарей для сайта
    users_list = []
    for row in rows:
        users_list.append({
            "user_id": row[0],
            "name": row[1],
            "city": row[2]
        })
        
    return {"total_users": len(users_list), "users": users_list}

from pydantic import BaseModel

# 1. Описываем схему: какие данные мы требуем для нового пользователя
class UserCreate(BaseModel):
    id: int      # Уникальный ID должен быть числом
    name: str    # Имя — текст
    city: str    # Город — текст

# 2. Создаем эндпоинт с методом POST
@app.post("/users/add")
def create_new_user(user: UserCreate):
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    
    try:
        # Записываем данные в базу SQL из пришедшего объекта user
        cursor.execute("""
        INSERT INTO users (id, name, city) 
        VALUES (?, ?, ?)
        """, (user.id, user.name, user.city))
        
        connection.commit()
        reply = {"status": "success", "message": f"Пользователь {user.name} успешно добавлен!"}
    except sqlite3.IntegrityError:
        reply = {"status": "error", "message": "Пользователь с таким ID уже существует!"}
        
    connection.close()
    return reply
