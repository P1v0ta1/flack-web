from flask import Flask, render_template
from config import Config, db

from page.index import index_page

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(index_page, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)