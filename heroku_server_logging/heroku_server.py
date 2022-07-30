# SERVER_URL = "https://my-solution.herokuapp.com"
"""
/success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
/fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500
"""

from bottle import run
from bottle import route
from bottle import HTTPError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@route("/success")
def success():
    return f'{logger.info(HTTPError)}'


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)