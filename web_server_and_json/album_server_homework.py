import os
import album

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

# RESOURCES_PATH = "users/"

# def save_user(artist_data):
#     artist = artist_data["artist"]
#     last_name = artist_data["last_name"]
#     filename = "{}-{}.json".format(artist, last_name)
#     if not os.path.exists(RESOURCES_PATH):
#         os.makedirs(RESOURCES_PATH)

#     with open(filename, "w") as fd:
#         json.dump(artist_data, fd)
#     return filename


@route("/albums", method="POST")
def new_artist():
    artist_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
        "id": request.forms.get("id")
    }
    new_artist_data = album.request_data(artist_data)
    # resource_path = save_user(artist_data)
    # print("User saved at: ", resource_path)

    return new_artist_data


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