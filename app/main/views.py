from . import main
from flask import render_template, flash
from .. import queries


@main.route('/', methods=['GET'])
def index():
    top15data = queries.get_top15()
    placedata = queries.get_place_data()
    teamdata = queries.get_team_data()
    return render_template('index.html', top15data=top15data,
                           placedata=placedata, teamdata=teamdata)


@main.route('/ladder', methods=['GET'])
def ladder():
    return render_template('ladder.html')


@main.route('/query', methods=['GET'])
def query():
    return render_template('query.html')


@main.route('/sponsor', methods=['GET'])
def sponsor():
    flash('test')
    return render_template('sponsor.html')
