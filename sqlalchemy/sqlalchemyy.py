

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Обычно доступ к базе данных выглядит -
# dialect+driver://username:password@host:port/database


# При подключении к sqlite - 
#  sqlite:///filename

DB_PATH = "sqlite:///b4_7.sqlite3"

Base = declarative_base()

class Album(Base):
    # указываем имя таблицы
    __tablename__ = "album"
    # Задаем колонки в формате
    # название_колонки = sa.Column(ТИП_КОЛОНКИ)
    # идентификатор строки
    id = sa.Column(sa.INTEGER, primary_key=True)
    # год записи альбома
    year = sa.Column(sa.INTEGER)
    # артист или группа, записавшие альбом
    artist = sa.Column(sa.TEXT)
    # жанр альбома
    genre = sa.Column(sa.TEXT)
    # Название альбома
    album = sa.Column(sa.TEXT)


# Создаем соединение к базе данных
engine = sa.create_engine(DB_PATH)
# создаем фабрику сессию
Sessions = sessionmaker(engine)
# создаем сессию
session = Sessions()


# передаем в модель Albun в метод session.query и вызываем метод all
albums = session.query(Album).all()


# выводит все записи из БД в опеределенном виде
for album in albums:
    print("Группа {} записала альбом {} в жанре {} в {} году".format(album.artist, album.album, album.genre, album.year))


# -----------------------------------------------------------------------
#                      Парсер строки соединения с БД
# ----------------------------------------------------------------------

connection_string = "postgresql+psycopg2://admin:1234@localhost:fsadghws/b4_7"

def parse_connection_string(x):
    """парсит строку соединения с БД"""

    d = { "dialect" :"", "driver":"", "username":"", "password":"", "host":"", "port":"", "database":""}

    if ":///" in x:
        d["dialect"] = x.split(":///")[0]
        d["database"] = x.split(":///")[1]
        print(d)
    else:
        base = x.split("://")
        if "+" in base[0]:
            d["dialect"] = base[0].split("+")[0]
            d["driver"] = base[0].split("+")[1]
        else:
            d["dialect"] = base[0]
        if "@" in base[1]:
            d["username"] = base[1].split("@")[0].split(":")[0]
            d["password"] = base[1].split("@")[0].split(":")[1]
            d["database"] = base[1].split("/")[1]
            if ":" in base[1].split("@")[1]:
                d["host"] = base[1].split("@")[1].split(":")[0]
                d["port"] = base[1].split("@")[1].split(":")[1].split("/")[0]
            else:
                d["host"] = base[1].split("@")[1].split("/")[0]
        else:
            d["username"] = base[1].split(":")[0]
            d["password"] = base[1].split(":")[1].split("/")[0]
            d["database"] = base[1].split(":")[1].split("/")[1]

    return d


parse_connection_string(connection_string)

# ---------------------------------------------------------------------------


# # два новых экземпляра класса
# bionic = Album(year=2010, artist="Christina Aguilera", genre="Rhythm and blues", album="Bionic")
# heaven_and_earth = Album(year=2010, artist="Kamasi Washington", genre="Jazz", album="Heaven and Earth")

# # # добавим их в объект сессии
# # session.add(bionic)
# # session.add(heaven_and_earth)

# # # теперь сохраним изменения и запишем их в БД
# # session.commit()
# # если в сессии накопились изменения которые мы хотим изменить, можно их откатить - session.rollback()


# # теперь исправим данные которые уже есть в БД
# heaven_and_earth = session.query(Album).filter(Album.album == "Heaven and Earth").first()
# heaven_and_earth.year = 2018
# # session.add(heaven_and_earth)

# last_ship = Album(year=2013, artist="Sting", genre="Rock", album="The Last Ship")
# magic = Album(year=2016, artist="Bruno Mars", genre="Rhythm and blues", album="24K Magic")

# # а теперь добавим все накопившиеся изменения
# session.add_all([last_ship, magic])

# session.commit()