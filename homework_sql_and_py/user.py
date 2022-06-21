import uuid
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()


class User(Base):
    """Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = "user"

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)

def connect_db():
    """Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к БД
    engine = sa.create_engine(DB_PATH)
    # Создаем описанные таблицы
    Base.metadata.create_all(engine)
    # Создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def valid_date(date):
    D, M, Y = date.split(".")
    if len(D) == 2 and len(M) == 2 and len(Y) == 4:
        return True
    else:
        return False


def request_data():
    """Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("Введе свое имя: ")
    last_name = input("Введи свою фамилию: ")
    gender = input("Введите пожалуйста ваш пол: ")
    height = input("Ваш рост: ")
    birthdate = input("Когда вы родились(пожалуйста в формате 'dd.mm.yyyy'): ")
    email = input("Введи свою почту: ")
    user_id = str(uuid.uuid4())
    # Создаем нового пользователя
    user = User(
        id = user_id,
        first_name = first_name,
        last_name = last_name,
        email = email,
        gender = gender,
        height = height,
        birthdate = birthdate
    )
    # возвращаем созданного пользователя
    return user

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    obj = request_data()
    session.add(obj)
    session.commit()
    print("Дфнные успещшно записаны")


if __name__ == "__main__":
    main()