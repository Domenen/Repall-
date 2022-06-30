import album

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request




@route("/albums", method="POST")
def create_album():
    year = request.forms.get("year")
    artist = request.forms.get("artist")
    genre = request.forms.get("genre")
    album_name = request.forms.get("album")

    try:
        year = int(year)
    except ValueError:
        return HTTPError(400, "Указан некорректный год альбома")

    try:
        new_album = album.request_data(year, artist, genre, album_name)
    except AssertionError as err:
        result = HTTPError(400, str(err))
    except album.AlreadyExists as err:
        result = HTTPError(409, str(err))
    else:    
        print("Новый #{} сохранен".format(new_album.id))
        result = "Альбом #{} успешно сохранен".format(new_album.id)
    return result


@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
        return result
    else:
        album_names = [album.album for album in albums_list]
        result = " альбомов {}: ".format(artist)
        result += ", ".join(album_names)
        result_number = str(len(album_names))
        return result_number, result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)