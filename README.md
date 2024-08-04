# todolist

<!-- ABOUT THE PROJECT -->
## О проекте
*FastAPI-приложение для отслеживания списка дел*
Приложение предоставляет возможности добавлять, обновлять и удалять задачи в списке дел.


**Стек**
- fastapi
- starlette
- sqlalchemy


<!-- GETTING STARTED -->
## Подготовка к работе

Для запуска локальной копии выполните следующие шаги:

### Установка

1. Клонируйте проект
   ```sh
   git@github.com:aukhadieva/todolist.git
   ```
2. Убедитесь, что вы получили из удаленного репозитория все ветки и переключились на ветку разработки develop
   ```sh
   git checkout develop
   ```
3. Установите зависимости проекта (в случае, если не установились при клонировании)
   ```sh
   poetry install
   ```
4. Создайте в корне проекта файл .env и заполните переменные среды в соответствии с желаемой конфигурацией, используя файл .env_sample


### Запуск приложения
1. Для запуска проекта выполните команду
   ```sh
   uvicorn app:app --reload
   ```
2. Пройдите по адресу
   ```sh
   http://127.0.0.1:8000/
   ```
