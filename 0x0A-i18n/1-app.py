#!/usr/bin/env python3
"""starter Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def home() -> str:
    """Route for index page"""
    return render_template('1-index.html')


class Config():
    """Babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
