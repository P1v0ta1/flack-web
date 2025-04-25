from flask import Flask, render_template
from config import Config,db

from models import House

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#测试代码
@app.route('/')
def hello():
    first_house =House.query.first()
    print(first_house)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)