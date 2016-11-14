from flask import render_template, request

from . import main
from .. import queries, db
from ..models import Sponsor


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
    if request.method == 'GET':
        listpage = None
        if ladder_type is None:
            ladder_data = queries.get_full_ladder(listpage)['data']
            return render_template('ladder.html', data=ladder_data, ladder_type=ladder_type)
        if ladder_type == 'full':
            ladder_data = queries.get_full_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)
        if ladder_type is None or ladder_type == 'pro':
            ladder_data = queries.get_pro_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)
        if ladder_type is None or ladder_type == 'lpl':
            ladder_data = queries.get_lpl_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)
        if ladder_type is None or ladder_type == 'cn':
            ladder_data = queries.get_cn_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)
        if ladder_type is None or ladder_type == 'nonpro':
            ladder_data = queries.get_nonpro_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)
    if request.method == 'POST':
        listpage = int(request.form.get('listpage'))
        if ladder_type == 'full':
            ladder_data = queries.get_full_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data)
        if ladder_type == 'pro':
            ladder_data = queries.get_pro_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data)
        if ladder_type == 'lpl':
            ladder_data = queries.get_lpl_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data)
        if ladder_type == 'cn':
            ladder_data = queries.get_cn_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data)
        if ladder_type == 'nonpro':
            ladder_data = queries.get_nonpro_ladder(listpage)['data']
            return render_template('tablerow.html', data=ladder_data, ladder_type=ladder_type)


@main.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'GET':
        args = {'listpage': '0', 'league': '全部', 'team': '全部', 'country': '全部', 'place': '全部', 'region': 'list'}
        list_query_data = queries.get_query_data(**args)['data']
        args = {'imgpage': '0', 'league': '全部', 'team': '全部', 'country': '全部', 'place': '全部', 'region': 'img'}
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


@main.route('/help', methods=['GET', 'POST'])
def sponsor():
    if request.method == 'GET':
        sponsordata = queries.get_sponsor_data()['data']
        return render_template('help.html', sponsordata=sponsordata)
    if request.method == 'POST':
        data = request.form
        newsponsor = Sponsor(sponsorfrom=data.get('from'), sponsorname=data.get('name'), sponsorserver=data.get('server'), sponsorgameid=data.get('gameid'), sponsoramount=data.get('amount'),
                             sponsordate=data.get('date'), sponsormedia=data.get('media'))
        db.session.add(newsponsor)
        db.session.commit()
        db.session.close()
        return 'ok,done'
