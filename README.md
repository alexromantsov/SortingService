# SortingService

**SortingService** - это приложение на Python, 

## Установка


1. Установите Python версии 3.8 или выше на вашем компьютере.
2. Клонируйте репозиторий SortingService
3. Перейдите в папку проекта:
```bash
cd SortingService
```

4. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

## Запуск сервера
```bash
python manage.py runserver
```

## Запуск автотестов
```bash
python manage.py test
```


### Создание requirements.txt

```bash
pip freeze > requirements.txt
```

### Выполнения миграций 
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


### Собрать все статические файлы
```bash
python manage.py collectstatic
```


### Создаем пользователей
```bash
python manage.py initialize_users
```

### Заполняем Базу данных данными
```bash
python manage.py filldata
```