from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
