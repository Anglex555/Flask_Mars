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

@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')

@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')

@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
