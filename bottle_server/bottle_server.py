# импортируем необходимые сущности библиотеки bottle
from bottle import route
from bottle import run

# регистрируем обработчик пути /hello/ с помощью декоратора route
@route("/hello/")
def hello_world():
    return "Hello World!"  # Возвращаем приветственное сообщение

@route("/upper/<param>")
def upper(param):
    return param.upper()

# --------------------------------------------------------------------------

from bottle import HTTPError  # Импортируем класс HTTPError

@route("/modify/<param>/<method>")
def modify(param, method):
    # проверяем переданный модификатор и готовим соответствующий результат
    if method == "upper":
        result = param.upper()
    elif method == "lower":
        result = param.lower()
    elif method == "title":
        result = param.title()
    else:
       	# если нам передан неизвестный модификатор, готовим ответ для пользователя 
        result = HTTPError(400, "incorrect `method` value")
    return result

# -------------------------------------------------------------------------------

from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError

@route("/add")
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, "Некорректные параметры")
    else:
        s = x + y
        result = "Сумма {} и {} равна {}".format(x, y, s)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)









if __name__ == "__main__":
    # Запускаем веб-сервер с помощью функции run: указываем адрес узла и порт
    run(host="localhost", port=8080, debug=True)
    # Булев флаг debug=True запускает сервер в режиме отладки

