from flask import render_template, Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    return render_template('no_base.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['list'] = list
    return render_template('list_prof.html', **param)


# @app.route('/odd_even')
# def odd_even():
#     return render_template('odd_even.html', number=2)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
