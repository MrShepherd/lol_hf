from sqlalchemy.sql.elements import or_

from app.models import Summary, SponsorManual
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


def get_full_ladder(listpage=None):
    if listpage is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (listpage - 1) * 20
        endindex = startindex + 20
    result = db.session.query(Summary.player_name, Summary.player_country, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).order_by(
        Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_pro_ladder(listpage=None):
    if listpage is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (listpage - 1) * 20
        endindex = startindex + 20
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_team_short_name != '').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_lpl_ladder(listpage=None):
    if listpage is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (listpage - 1) * 20
        endindex = startindex + 20
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_team_league == 'LPL').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_cn_ladder(listpage=None):
    if listpage is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (listpage - 1) * 20
        endindex = startindex + 20
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp, Summary.mmr,
                              Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        or_(Summary.player_country == 'CN', Summary.player_country == 'TW')).order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_nonpro_ladder(listpage=None):
    if listpage is None:
        startindex = 0
        endindex = 100
    else:
        startindex = 100 + (listpage - 1) * 20
        endindex = startindex + 20
    result = db.session.query(Summary.player_name, Summary.rank, Summary.player_country, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier, Summary.lp,
                              Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
        Summary.player_place == '路人').order_by(Summary.rank).all()[startindex:endindex]
    data = to_dict(result)
    return data


def get_query_data(**kw):
    league_list = ['LPL', 'LCK', 'LMS', 'LCS-EU', 'LCS-NA']
    country_list = ['CN', 'KR', 'TW', 'VN', 'US']
    team_list = ['EDG', 'RNG', 'IM', 'SKT', 'ROX', 'SSG', 'LGD', 'SS', 'IG', 'WE', 'OMG']
    if kw is not None and len(kw) > 0:
        # league
        if '全部' in kw.get('league'):
            column_league_exp = "1==1"
        elif '其他' in kw.get('league'):
            column_league_exp = "~Summary.player_team_league.in_(league_list)"
        elif 'LCS' in kw.get('league'):
            column_league_exp = "Summary.player_team_league.in_(['LCS-EU','LCS-NA'])"
        else:
            column_league_exp = "Summary.player_team_league.in_(kw.get('league'))"
        # country
        if '全部' in kw.get('country'):
            column_country_exp = "1==1"
        elif '其他' in kw.get('country'):
            column_country_exp = "~Summary.player_country.in_(country_list)"
        elif '中国' in kw.get('country'):
            column_country_exp = "Summary.player_country.in_(['CN','TW'])"
        elif '韩国' in kw.get('country'):
            column_country_exp = "Summary.player_country.in_(['KR'])"
        elif '台湾' in kw.get('country'):
            column_country_exp = "Summary.player_country.in_(['TW'])"
        elif '美国' in kw.get('country'):
            column_country_exp = "Summary.player_country.in_(['US'])"
        elif '越南' in kw.get('country'):
            column_country_exp = "Summary.player_country.in_(['VN'])"
        else:
            column_country_exp = "1==1"
        # team
        if '全部' in kw.get('team'):
            column_team_exp = "1==1"
        elif '其他' in kw.get('team'):
            column_team_exp = "~Summary.player_team_short_name.in_(team_list)"
        else:
            column_team_exp = "Summary.player_team_short_name.in_(kw.get('team'))"
        # place
        if '全部' in kw.get('place'):
            column_place_exp = "1==1"
        else:
            column_place_exp = "Summary.player_place.in_(kw.get('place'))"
    else:
        column_league_exp = "1==1"
        column_country_exp = "1==1"
        column_team_exp = "1==1"
        column_place_exp = "1==1"
    if 'list' in kw.get('region'):
        listpage = int(kw.get('listpage')[0])
        liststartindex = listpage * 18
        listendindex = liststartindex + 18
        result = db.session.query(Summary.player_name, Summary.player_country, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier,
                                  Summary.lp, Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
            eval(column_country_exp)).filter(eval(column_league_exp)).filter(eval(column_team_exp)).filter(eval(column_place_exp)).order_by(Summary.rank).all()[liststartindex:listendindex]
    elif 'img' in kw.get('region'):
        imgpage = int(kw.get('imgpage')[0])
        imgstartindex = imgpage * 18
        imgendindex = imgstartindex + 18
        result = db.session.query(Summary.player_name, Summary.player_country, Summary.rank, Summary.player_team_short_name, Summary.player_place, Summary.link, Summary.game_id, Summary.tier,
                                  Summary.lp, Summary.mmr, Summary.total_win, Summary.total_lose, Summary.total_win_ratio, Summary.twentyavgck, Summary.twentyavgkda, Summary.twentywinratio).filter(
            eval(column_country_exp)).filter(eval(column_league_exp)).filter(eval(column_team_exp)).filter(eval(column_place_exp)).filter(Summary.player_name != '路人').order_by(Summary.rank).all()[
                 imgstartindex:imgendindex]
    data = to_dict(result)
    return data


def get_sponsor_data():
    result = db.session.query(SponsorManual.sponsorname, SponsorManual.sponsoramount, SponsorManual.sponsordate, SponsorManual.sponsorfrom, SponsorManual.sponsorgameid, SponsorManual.sponsormedia,
                              SponsorManual.sponsorserver).order_by(SponsorManual.sponsoramount).all()
    data = to_dict(result)
    return data
