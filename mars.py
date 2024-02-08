from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_pyfile('config.py')

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

@app.route('/choice/<planet_name>')
def choice(planet_name):
    planet_info = get_planet_info(planet_name)
    return render_template('choice.html', planet_name=planet_name, planet_info=planet_info)

def get_planet_info(planet_name):
    if planet_name.lower() == 'Mars' or planet_name.lower() == 'марс':
        return {
            'name': 'Марс',
            'description': 'Марс - четвёртая планета от Солнца. Он близок по размерам к Земле, имеет водяной лед на поверхности и полярных капах, и давно вызывает интерес ученых и исследователей.',
            'advantages': ['Близкое расстояние к Земле', 'Потенциально обитаемые условия', 'Возможность терраформирования']
        }
    elif planet_name.lower() == 'Venus' or planet_name.lower() == 'венера':
        return {
            'name': 'Венера',
            'description': 'Венера - вторая планета от Солнца, самая близкая к Земле по размерам, массе и минимальному расстоянию. На Венере давление в 92 раза превышает земное, и её атмосфера состоит в основном из углекислого газа.',
            'advantages': ['Близкое расстояние к Земле', 'Возможность изучения атмосферы и парникового эффекта']
        }
    else:
        return {
            'name': planet_name,
            'description': 'Информация о данной планете отсутствует',
            'advantages': ["Неизвестны"]
        }

@app.route('/results/<string:nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)