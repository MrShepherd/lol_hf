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
    if request.args.get('type') is not None:
        ladder_type = request.args.get('type')
    else:
        ladder_type = None
    if request.form.get('page') is not None:
        page = int(request.form.get('page'))
    else:
        page = None
    if ladder_type is None:
        ladder_data = queries.get_full_ladder(page)['data']
        return render_template('ladder.html', data=ladder_data, ladder_type=ladder_type)
    if ladder_type == 'full':
        ladder_data = queries.get_full_ladder(page)['data']
        return render_template('tablerow.html', data=ladder_data)
    if ladder_type == 'pro':
        ladder_data = queries.get_pro_ladder(page)['data']
        return render_template('tablerow.html', data=ladder_data)
    if ladder_type == 'lpl':
        ladder_data = queries.get_lpl_ladder(page)['data']
        return render_template('tablerow.html', data=ladder_data)
    if ladder_type == 'cn':
        ladder_data = queries.get_cn_ladder(page)['data']
        return render_template('tablerow.html', data=ladder_data)
    if ladder_type == 'nonpro':
        ladder_data = queries.get_nonpro_ladder(page)['data']
        return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)


@main.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'GET':
        args = {}
        list_query_data = queries.get_query_data(**args)['data']
        args = {'page': '999', 'league': '全部', 'team': '全部', 'country': '全部', 'place': '全部'}
        img_query_data = queries.get_query_data(**args)['data']
        return render_template('query.html', list_query_data=list_query_data, img_query_data=img_query_data)
    if request.method == 'POST':
        args = request.form
        if 'list' in args.get('region'):
            query_data = queries.get_query_data(**args)['data']
            return render_template('tablerow.html', data=query_data, ladder_type='query')
        if 'img' in args.get('region'):
            query_data = queries.get_query_data(**args)['data']
            return render_template('playerlistimg.html', data=query_data)


@main.route('/help', methods=['GET'])
def sponsor():
    flash('test')
    return render_template('help.html')
