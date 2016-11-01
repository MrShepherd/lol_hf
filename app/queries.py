from app.models import Summary
from . import db


def to_dict(data_tuple_list):
    data_dict_list = []
    for item in data_tuple_list:
        data_dict_list.append(item._asdict())
    data = {'data': data_dict_list}
    return data


def get_ladder_top15():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.lp).order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_lpl():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.lp).filter(Summary.player_team_league == 'LPL').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_cn():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.lp).filter(Summary.player_country == 'CN').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_adc():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == 'ADC').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_support():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '辅助').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_top():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '上单').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_middle():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '中单').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_ladder_top15_jungle():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '打野').order_by(Summary.rank).all()[:15]
    data = to_dict(result)
    return data


def get_hot_team():
    hot_team_list = ['EDG', 'RNG', 'IM', 'WE', 'SS', 'LGD', 'OMG', 'IG', 'SKT', 'ROX', 'SSG']
    item = []
    for team in hot_team_list:
        result = db.session.query(Summary.player_name, Summary.rank, Summary.player_place, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win, Summary.total_win_ratio).filter(
            Summary.player_team_short_name == team).order_by(Summary.rank).all()[:15]
        item.append({'%s-data' % team: to_dict(result)['data']})
    data = {'data': item}
    return data


# test
def get_top15():
    item = {'rank': 1, 'name': 'xiaohu', 'id': 'leap', 'lp': 1300}
    data = [item for x in range(1, 11)]
    return data


def get_place_data():
    item = {'place': 'shangdan', 'rank': 1, 'name': 'uzi', 'team': 'RNG', 'id': 'kuangxiaogou', 'tier': 'wangzhe', 'lp': 1000, 'winratio': 0.60, 'mmr': 2300, 'twentywinratio': 0.80, 'twentykda': 13}
    data = [item for x in range(1, 10)]
    return data


def get_team_data():
    item = {'place': 'shangdan', 'rank': 1, 'name': 'uzi', 'team': 'RNG', 'id': 'kuangxiaogou', 'tier': 'wangzhe', 'lp': 1000, 'winratio': 0.60, 'mmr': 2300, 'twentywinratio': 0.80, 'twentykda': 13}
    data = [item for x in range(1, 10)]
    return data


def get_ladder_data():
    item = {'rank': 1, 'name': 'uzi', 'team': 'RNG', 'id': 'kuangxiaogou', 'tier': 'wangzhe', 'lp': 1000, 'mmr': 2300, 'winratio': 0.60, }
    data = [item for x in range(1, 30)]
    return data
