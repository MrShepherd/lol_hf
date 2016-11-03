from . import api
from flask import jsonify
from .. import queries


@api.route('/api/top15/')
def get_top15():
    data = queries.get_ladder_top15()
    return jsonify(data)


@api.route('/api/lpltop15/')
def get_top15_lpl():
    data = queries.get_ladder_top15_lpl()
    return jsonify(data)


@api.route('/api/cntop15/')
def get_top15_cn():
    data = queries.get_ladder_top15_cn()
    return jsonify(data)


@api.route('/api/adctop15/')
def get_top15_adc():
    data = queries.get_ladder_top15_adc()
    return jsonify(data)


@api.route('/api/suporttop15/')
def get_top15_support():
    data = queries.get_ladder_top15_support()
    return jsonify(data)


@api.route('/api/middletop15/')
def get_top15_middle():
    data = queries.get_ladder_top15_middle()
    return jsonify(data)


@api.route('/api/toptop15/')
def get_top15_top():
    data = queries.get_ladder_top15_top()
    return jsonify(data)


@api.route('/api/jungletop15/')
def get_top15_jungle():
    data = queries.get_ladder_top15_jungle()
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


# test
@api.route('/api/shangdandata/')
def get_shangdan_data():
    data = queries.get_place_data()
    return jsonify({'data': data})
