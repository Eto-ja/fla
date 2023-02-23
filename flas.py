from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def inde():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='static/img/image_mars.jpeg')}"
                     alt="здесь должна была быть картинка, но не нашлась">                          
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
                     rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='/img/image_mars.jpeg')}"
                     alt="здесь должна была быть картинка, но не нашлась"></br>                         
                    <q2><font size = "5">Человечество вырастает из детства</font></q2></br>
                    <q1><font size = "5">Человечеству мала одна планета</font></q1></br>
                    <q3><font size = "5" class=q1>Мы сделаем обитаемыми безжизненные пока планеты.</font></q3></br>
                    <q4><font size = "5">И начнем с Марса!</font></q4></br>
                    <q5><font size = "5">Присоединяйся!</font></q5>
                  </body>
                </html>"""


# <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />


if __name__ == '__main__':
    app.run(port=8080, debug=False)
