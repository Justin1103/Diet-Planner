from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import diet_maker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diet.db'
app.secret_key = '123456'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    amounts, instructions = diet_maker.create_recipe(600)
    res = []
    for name, values in amounts.items():
        res.append("{} - {}g - {} kcal".format(name, values[1], values[0]))
    res.append("Sposób przyrządzenia:")
    for i, step in enumerate(instructions):
        res.append("{}. {}".format(i + 1, step))

    return '<br>'.join(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
