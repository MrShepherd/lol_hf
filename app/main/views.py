from . import main
from flask import render_template, flash
from .. import queries


@main.route('/', methods=['GET'])
def index():
    top10data = queries.get_ladder_top10()['data']
    lpltop10data = queries.get_ladder_top10_lpl()['data']
    cntop10data = queries.get_ladder_top10_cn()['data']
    placedata = queries.get_place_data()['data']
    teamdata = queries.get_hot_team()['data']
    return render_template('index.html', top10data=top10data, lpltop10data=lpltop10data, cntop10data=cntop10data, placedata=placedata, teamdata=teamdata)


@main.route('/ladder', methods=['GET'])
def ladder():
    ladder_data = queries.get_full_ladder()
    return render_template('ladder.html', ladder_data=ladder_data)


@main.route('/query', methods=['GET'])
def query():
    ladder_data = queries.get_query_data()
    return render_template('query.html', ladder_data=ladder_data)


@main.route('/sponsor', methods=['GET'])
def sponsor():
    flash('test')
    return render_template('sponsor.html')
