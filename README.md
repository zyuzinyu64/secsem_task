#### secsem_task

Приложение написано на Django 3.2.7
1) Для учтановки данного фреймворка нужно установить Python3.7 и выше. Команда для установки Django:
- pip install Django
2) Подключиться к серверу mysql. 
3) Создать базу данных и таблицы, используя скрипт db-init.mysql
4) В командной строке пишем команду:
- django-admin startproject test_project
5) В папке проекта прописываем команду:
- python manage.py startapp firstapp
6) Проводим настройку файла test_project:
- создаем папку templates, кладём туда файлы из директории данного гита github.com/zyuzinyu64/secsem_task/blob/main/test_project/test_project/templates/
- в файле settings.py проводим настройку переменной TEMPLATES, указываем в переменную DIRS путь до папки templates, в переменной DATABASES делаем изменения в соотвествии с https://github.com/zyuzinyu64/secsem_task/blob/main/test_project/test_project/settings.py, а так же меняем переменную LANGUAGE_CODE на 'ru'
- файл urls.py заменить на https://github.com/zyuzinyu64/secsem_task/blob/main/test_project/test_project/urls.py
7) Переходим в директорию приложения и вносим изменения:
- Заменяем файл views.py на https://github.com/zyuzinyu64/secsem_task/blob/main/test_project/firstapp/views.py
- Если нет файлы models.py, то добавляем https://github.com/zyuzinyu64/secsem_task/blob/main/test_project/firstapp/models.py
8) Находясь в папке проекта, прописываем следующие команды:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

Терминал выдаст ссылку на главную страницу вида: "http://127.0.0.1:8000/", что является основной страницей веб-приложения, переходим по ней и тестируем
