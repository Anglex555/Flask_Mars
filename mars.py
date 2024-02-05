from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def mission_title():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def mission_slogan():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promotion():
    promotion_text = (
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    )
    return render_template('promotion.html', promotion_text=promotion_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
