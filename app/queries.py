from sqlalchemy.sql.elements import or_

from app.models import Summary
from . import db


def to_dict(data_tuple_list):
    data_dict_list = []
    for item in data_tuple_list:
        data_dict_list.append(item._asdict())
    data = {'data': data_dict_list}
    return data


def get_ladder_top10():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.tier, Summary.lp).order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_lpl():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.tier, Summary.lp).filter(Summary.player_team_league == 'LPL').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_cn():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.game_id, Summary.tier, Summary.lp).filter(or_(Summary.player_country == 'CN', Summary.player_country == 'TW')).order_by(
        Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_adc():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == 'ADC').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_support():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '辅助').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_top():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '上单').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_middle():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '中单').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_ladder_top10_jungle():
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win,
                              Summary.total_win_ratio).filter(Summary.player_place == '打野').order_by(Summary.rank).all()[:10]
    data = to_dict(result)
    return data


def get_place_data():
    place_list = ['ADC', '辅助', '中单', '打野', '上单']
    item = []
    for place in place_list:
        result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win, Summary.total_win_ratio,
                                  Summary.twentyavgkda, Summary.twentywinratio, Summary.twentyavgck).filter(Summary.player_place == place).order_by(Summary.rank).all()[:10]
        item.append({'%s-data' % place: to_dict(result)['data']})
    data = {'data': item}
    return data


def get_hot_team():
    hot_team_list = ['EDG', 'RNG', 'IM', 'SKT', 'ROX', 'SSG', 'LGD', 'SS', 'IG', 'WE', 'OMG']
    item = []
    for team in hot_team_list:
        result = db.session.query(Summary.player_name, Summary.rank, Summary.player_place, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr, Summary.total_win, Summary.total_win_ratio,
                                  Summary.twentyavgkda, Summary.twentywinratio, Summary.twentyavgck).filter(Summary.player_team_short_name == team).order_by(Summary.rank).all()[:15]
        item.append({'%s-data' % team: to_dict(result)['data']})
    data = {'data': item}
    return data


def get_full_ladder(page=None):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    result = db.session.query(Summary.player_name, Summary.player_country, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).order_by(
        Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_pro_ladder(page=None):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_team_short_name != '').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_lpl_ladder(page=None):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_team_league == 'LPL').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_cn_ladder(page=None):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr,
                              Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        or_(Summary.player_country == 'CN', Summary.player_country == 'TW')).order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_nonpro_ladder(page=None):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_place == '路人').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_query_data(page=None, **kw):
    if page is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (page - 1) * 20 + 1
        endindex = startindex + 19
    print(kw)
    result = db.session.query(Summary.player_name, Summary.player_country, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_country == 'CN').filter(Summary.player_team_league == 'LPL').filter(Summary.player_team_short_name == 'EDG').filter(Summary.player_place == '打野').order_by(Summary.rank).all()[
             startindex:endindex]
    data = to_dict(result)
    return data
