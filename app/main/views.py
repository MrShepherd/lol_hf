from flask import render_template, flash, request

from . import main
from .. import queries


@main.route('/', methods=['GET'])
def index():
    top10data = queries.get_ladder_top10()['data']
    lpltop10data = queries.get_ladder_top10_lpl()['data']
    cntop10data = queries.get_ladder_top10_cn()['data']
    placedata = queries.get_place_data()['data']
    teamdata = queries.get_hot_team()['data']
    return render_template('index.html', top10data=top10data, lpltop10data=lpltop10data, cntop10data=cntop10data, placedata=placedata, teamdata=teamdata)


@main.route('/ladder', methods=['GET', 'POST'])
def ladder():
    if request.method == 'GET':
        ladder_type = request.args.get('type')
    elif request.method == 'POST':
        ladder_type = request.form['type']
    if ladder_type is None:
        ladder_data = queries.get_full_ladder()['data']
        return render_template('full-ladder.html', ladder_data=ladder_data)
    if ladder_type == 'full':
        ladder_data = queries.get_full_ladder()['data']
        return render_template('ladder.html', ladder_data=ladder_data)
    if ladder_type == 'pro':
        ladder_data = queries.get_pro_ladder()['data']
        return render_template('ladder.html', ladder_data=ladder_data)
    if ladder_type == 'lpl':
        ladder_data = queries.get_lpl_ladder()['data']
        return render_template('ladder.html', ladder_data=ladder_data)
    if ladder_type == 'cn':
        ladder_data = queries.get_cn_ladder()['data']
        return render_template('ladder.html', ladder_data=ladder_data)
    if ladder_type == 'nonpro':
        ladder_data = queries.get_nonpro_ladder()['data']
        return render_template('ladder.html', ladder_data=ladder_data)


@main.route('/query', methods=['GET'])
def query():
    ladder_data = queries.get_query_data()
    return render_template('query.html', ladder_data=ladder_data)


@main.route('/help', methods=['GET'])
def sponsor():
    flash('test')
    return render_template('help.html')
