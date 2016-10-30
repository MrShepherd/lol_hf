from . import db


class Team(db.Model):
    __tablename__ = 'team'
    team_name = db.Column(db.String(100), primary_key=True)
    team_nation = db.Column(db.String(10))
    team_league = db.Column(db.String(10))

    # players = db.relationship('Player', backref='team_name', lazy='dynamic')

    def __repr__(self):
        return '<Team %r>' % self.team_name


class Player(db.Model):
    __tablename__ = 'player'
    # id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')
    player_name = db.Column(db.String(100), primary_key=True)
    player_country = db.Column(db.String(20))
    # player_team = db.Column(db.String(32), db.ForeignKey('team.team_name'))
    player_team = db.Column(db.String(50), primary_key=True)
    player_place = db.Column(db.String(20))

    # idmappings = db.relationship('IDMapping', backref='player', lazy='dynamic')

    def __repr__(self):
        return '<Player %r>' % self.player_name


class IDMapping(db.Model):
    __tablename__ = 'idmapping'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # playername = db.Column(db.String(64), db.ForeignKey('player.player_name'))
    player_name = db.Column(db.String(100))
    player_team = db.Column(db.String(50))
    game_id = db.Column(db.String(100))

    def __repr__(self):
        return '<IDMapping %r>' % self.game_id


class GameIDInfo(db.Model):
    __tablename__ = 'gameidinfo'
    game_id = db.Column(db.String(100), primary_key=True)
    link = db.Column(db.String(500))
    rank = db.Column(db.String(10))
    tier = db.Column(db.String(30))
    lp = db.Column(db.String(30))
    total_win = db.Column(db.String(30))
    total_lose = db.Column(db.String(30))
    total_win_ratio = db.Column(db.String(30))
    mmr = db.Column(db.String(30))
    twentywin = db.Column(db.String(30))
    twentylose = db.Column(db.String(30))
    twentywinratio = db.Column(db.String(30))
    twentyavgkill = db.Column(db.String(30))
    twentyavgdeath = db.Column(db.String(30))
    twentyavgassist = db.Column(db.String(30))
    twentyavgkda = db.Column(db.String(30))
    twentyavgck = db.Column(db.String(30))

    def __repr__(self):
        return '<GameIDInfo %r>' % self.game_id
