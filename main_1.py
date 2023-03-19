from flask import Flask, redirect, render_template
from data import db_session
from data.users import User
from flask_login import LoginManager, login_user
from loginform import LoginForm
from workform import WorkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = WorkForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        return redirect("/")
    return render_template('work.html', title='Adding a job', form=form)


def main():
    db_session.global_init("db/blogs.db")
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = "surname1"
    # user.name = "name1"
    # user.age = 22
    # user.position = "colonist"
    # user.speciality = "research engineer"
    # user.address = "module_2"
    # user.email = "surname1_chief@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()

    # user = User()
    # user.surname = "surname2"
    # user.name = "name2"
    # user.age = 23
    # user.position = "colonist"
    # user.speciality = "research engineer"
    # user.address = "module_3"
    # user.email = "surname2_chief@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = "surname3"
    # user.name = "name3"
    # user.age = 24
    # user.position = "colonist"
    # user.speciality = "research engineer"
    # user.address = "module_4"
    # user.email = "surname3_chief@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()

    db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.address == 'module_1')
    # print(user)
    # for user in db_sess.query(User).filter((User.address == 'module_1')):
    #     print(user)
    # app.run()


if __name__ == '__main__':
    # main()
    app.run(port=8080, debug=True)
