# Решатель школьных проблем

Дорогой друг! Если, вдруг, каким-то удивительным образом, в твоей школе электронный дневник ведется с помощью [проекта от Devman](https://github.com/devmanorg/e-diary) и у тебя есть доступ к серверу, то ты можешь очень сильно поправить свою успеваемость с помощью __Решателя школьных проблем__!

Эта программа исправит плохие оценки, удалит замечания учителей и даже добавит похвалы от них.

## Как использовать

1. Скачай этот файл `super_script.py` и положи его на сервер в папку где расположен сайт электронного дневника (в этой папке будет файл `manage.py`).
2. В консоли сервера введи команду (чтобы не ошибиться в командах - копируй их из инструкции)
```
python manage.py shell
```
должна появиться следующая надпись (верхняя строчка может быть другой)
```Python console
Python 3.10.1 (main, Jan 15 2022, 15:06:10) [GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```
3. После значка `'>>>'` введи новую команду
```Python
from super_script import hack_db
```
4. Теперь можно править данные. Вызови функцию `hack_db` и передай в неё ФИО ученика (можно указывать только часть ФИО, например только фамилию или фамилию и имя) и название урока по которому надо добавить похвалу
```Python
hack_db('Фролов Иван', 'Математика')
```
Если программа выдаст сообщение: `"Найдено много учеников, укажите имя точнее!"` или `"Ученик не найден - проверьте имя!"`, или `"Не найден урок - проверьте название предмета!"`, то внимательно проверь введенные данные и повтори пункт 4 этой инструкции.

Когда все пройдет успешно программа сообщит: `"Шалость удалась!"`

## Техническая информация

Для использования этого скрипта необходимо иметь развернутый сайт проекта [e-diary](https://github.com/devmanorg/e-diary) и файл БД.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
