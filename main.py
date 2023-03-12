from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # app.run()

    user = User()

    user.name = "Ridley"
    user.surname = "Scott"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "surname1"
    user.name = "name1"
    user.age = 22
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "surname1_chief@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "surname2"
    user.name = "name2"
    user.age = 23
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_3"
    user.email = "surname2_chief@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "surname3"
    user.name = "name3"
    user.age = 24
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_4"
    user.email = "surname3_chief@mars.org"
    db_sess.add(user)
    db_sess.commit()


def query_1():
    db_path = "db/blogs.db"
    db_session.global_init(db_path)
    db_sess = db_session.create_session()

    query = db_sess.query(User).filter(User.address == 'module_1')
    for i in query:
        print(i.id)


def query_2():
    db_path = "db/blogs.db"
    db_session.global_init(db_path)
    db_sess = db_session.create_session()

    query = db_sess.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%'))
    for i in query:
        print(i)


def main_2():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    job = Jobs(team_leader=1, job="deployment of residential modules 1 and 2", work_size=15, collaborators="2, 3",
               is_finished=False)
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main_2()
