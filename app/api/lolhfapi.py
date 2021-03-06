from . import api
from flask import jsonify
from .. import queries


@api.route('/api/top10/')
def get_top10():
    data = queries.get_ladder_top10()
    return jsonify(data)


@api.route('/api/lpltop10/')
def get_top10_lpl():
    data = queries.get_ladder_top10_lpl()
    return jsonify(data)


@api.route('/api/cntop10/')
def get_top10_cn():
    data = queries.get_ladder_top10_cn()
    return jsonify(data)


@api.route('/api/adctop10/')
def get_top10_adc():
    data = queries.get_ladder_top10_adc()
    return jsonify(data)


@api.route('/api/suporttop10/')
def get_top10_support():
    data = queries.get_ladder_top10_support()
    return jsonify(data)


@api.route('/api/middletop10/')
def get_top10_middle():
    data = queries.get_ladder_top10_middle()
    return jsonify(data)


@api.route('/api/toptop10/')
def get_top10_top():
    data = queries.get_ladder_top10_top()
    return jsonify(data)


@api.route('/api/jungletop10/')
def get_top10_jungle():
    data = queries.get_ladder_top10_jungle()
    return jsonify(data)


@api.route('/api/placedata/')
def get_place_data():
    data = queries.get_place_data()
    return jsonify(data)


@api.route('/api/hotteam/')
def get_team_data():
    data = queries.get_hot_team()
    return jsonify(data)


@api.route('/api/ladder/')
def get_ladder_ranking():
    data = queries.get_full_ladder()
    return jsonify(data)


@api.route('/api/proladder/')
def get_pro_ladder_ranking():
    data = queries.get_pro_ladder()
    return jsonify(data)


@api.route('/api/lplladder/')
def get_lpl_ladder_ranking():
    data = queries.get_lpl_ladder()
    return jsonify(data)


@api.route('/api/cnladder/')
def get_cn_ladder_ranking():
    data = queries.get_cn_ladder()
    return jsonify(data)


@api.route('/api/nonproladder/')
def get_nonpro_ladder_ranking():
    data = queries.get_nonpro_ladder()
    return jsonify(data)


@api.route('/api/query/')
def get_query_data():
    kw = {'place': ['全部'], 'team': ['全部'], 'league': ['全部'], 'country': ['全部'], 'region': 'list', 'listpage': '2'}
    data = queries.get_query_data(**kw)
    return jsonify(data)


@api.route('/api/sponsor/')
def get_sponsor_data():
    data = queries.get_sponsor_data()
    return jsonify(data)
