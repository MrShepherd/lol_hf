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
    player_team_full_name = db.Column(db.String(50), primary_key=True)
    player_team_short_name = db.Column(db.String(50))
    player_team_country = db.Column(db.String(20))
    player_team_league = db.Column(db.String(20))
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
    rank = db.Column(db.Integer)
    tier = db.Column(db.String(30))
    lp = db.Column(db.Integer)
    total_win = db.Column(db.Integer)
    total_lose = db.Column(db.Integer)
    total_win_ratio = db.Column(db.Integer)
    mmr = db.Column(db.Integer)
    twentywin = db.Column(db.Integer)
    twentylose = db.Column(db.Integer)
    twentywinratio = db.Column(db.Integer)
    twentyavgkill = db.Column(db.Float)
    twentyavgdeath = db.Column(db.Float)
    twentyavgassist = db.Column(db.Float)
    twentyavgkda = db.Column(db.Float)
    twentyavgck = db.Column(db.Float)

    def __repr__(self):
        return '<GameIDInfo %r>' % self.game_id


class Summary(db.Model):
    __tablename__ = 'summary'
    player_name = db.Column(db.String(100))
    player_country = db.Column(db.String(20))
    player_team_short_name = db.Column(db.String(50))
    player_team_league = db.Column(db.String(20))
    player_place = db.Column(db.String(20))
    game_id = db.Column(db.String(100), primary_key=True)
    link = db.Column(db.String(500))
    rank = db.Column(db.Integer)
    tier = db.Column(db.String(30))
    lp = db.Column(db.Integer)
    total_win = db.Column(db.Integer)
    total_lose = db.Column(db.Integer)
    total_win_ratio = db.Column(db.Integer)
    mmr = db.Column(db.Integer)
    twentywin = db.Column(db.Integer)
    twentylose = db.Column(db.Integer)
    twentywinratio = db.Column(db.Integer)
    twentyavgkill = db.Column(db.Float)
    twentyavgdeath = db.Column(db.Float)
    twentyavgassist = db.Column(db.Float)
    twentyavgkda = db.Column(db.Float)
    twentyavgck = db.Column(db.Float)

    def __repr__(self):
        return '<Summary %r>' % self.game_id
