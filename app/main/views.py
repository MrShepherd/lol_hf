from . import main
from flask import render_template


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/ladder', methods=['GET'])
def ladder():
    return render_template('ladder.html')


@main.route('/query', methods=['GET'])
def query():
    return render_template('query.html')


@main.route('/sponsor', methods=['GET'])
def sponsor():
    return render_template('sponsor.html')
