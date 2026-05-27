как запустить сайт

cd project2 - заходим в проект
virt/Scripts/activate - запускаем виртуальную машину

если выйдет ошибка прав доступа пишите вот эту команду и повторяете команду с верху
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process - давем прова доступа рут (админ прова)


cd russia_peoples - заходим в основную папку

python manage.py runserver - запускаем сервер

http://127.0.0.1:8000 - заходим на сайт в браузере
http://127.0.0.1:8000/admin - админ панель сайта