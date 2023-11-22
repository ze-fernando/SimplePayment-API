from flask import Flask, request
from .domain.enums import Type

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)