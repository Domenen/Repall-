from bottle import run
from bottle import route
from bottle import HTTPError
starting = open("index.html" ,encoding='UTF-8')
page_2 = open("page_2.html" ,encoding='UTF-8')
stile = open("style/style.css" ,encoding='UTF-8')
starti = starting.readlines()
page_23 = page_2.readlines()
stilee = stile.readlines()

inde = starti + stilee

@route("/stat")
def stat():
    return inde


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)