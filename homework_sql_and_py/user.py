# import imp
import uuid
# import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()


class User(Base):
    """Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primory_key=True)
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

def request_data():
    """Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("Введе свое имя: ")
    last_name = input("Введи свою фамилию: ")
    gender = input("Введите пожалуйста ваш пол: ")
    hieght = input("Ващ рост: ")
    birthday = input("Когда вы родились(пожалуйста в формате 'dd.mm.yy'): ")
    email = input("Введи свою почту: ")
    user_id = str(uuid.uuid4())
    # Создаем нового пользователя
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        hieght=hieght,
        birthday=birthday
    )
    # возвращаем созданного пользователя
    return user

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    # просим пользователя выбрать режим
    mode = input("Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    # проверяем режим
    if mode == "1":
        # выбран режим поиска, запускаем его
        name = input("Введи имя пользователя для поиска: ")
        # вызываем функцию поиска по имени
        users_cnt, user_ids, log = find(name, session)
        # вызываем функцию печати на экран результатов поиска
        print_users_list(users_cnt, user_ids, log)
    elif mode == "2":
        # запрашиваем данные пользоватлея
        user = request_data()
        # добавляем нового пользователя в сессию
        session.add(user)
        # обновляем время последнего визита для этого пользователя
        # log_entry = update_timestamp(user.id, session)
        # добавляем объект log_entry в сессию
        # session.add(log_entry)
        # сохраняем все изменения, накопленные в сессии
        session.commit()
        print("Спасибо, данные сохранены!")
    else:
        print("Некорректный режим:(")

if __name__ == "__main__":
    main()