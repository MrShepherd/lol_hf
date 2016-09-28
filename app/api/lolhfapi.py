from . import api
from flask import jsonify


@api.route('/api/top15/')
def get_top15():
    data = [
        {
            'rank': 1,
            'name': 'xiaohu',
            'lp': 1300
        },
        {
            'rank': 2,
            'name': 'faker',
            'lp': 1250
        }
    ]
    return jsonify({'data': data})
