from flask import Flask
from weather import weather_by_city
from flask import render_template
from news_finder import get_python_news
app = Flask(__name__)


# @app.route("/")
# def hello():
#   return "Привет!"


@app.route("/")
def index():
    weather = weather_by_city("Moscow,Russia")
    news_list = get_python_news()
    return render_template('index.html', weather=weather, news_list=news_list)


if __name__ == "__main__":
    app.run()
