from . import db


class Team(db.Model):
    __tablename__ = 'team'
    name = db.Column(db.String(32), primary_key=True)
    region = db.Column(db.String(32), nullable=False)
    players = db.relationship('Player', backref='team', lazy='dynamic')

    def __repr__(self):
        return '<Team %r>' % self.name


class Player(db.Model):
    __tablename__ = 'player'
    # id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')
    name = db.Column(db.String(64), primary_key=True)
    country = db.Column(db.String(32), nullable=False)
    team = db.Column(db.String(32), db.ForeignKey('team.name'), nullable=False)
    place = db.Column(db.String(16), nullable=False)
    idmappings = db.relationship('IDMapping', backref='player', lazy='dynamic')

    def __repr__(self):
        return '<Player %r>' % self.name


class IDMapping(db.Model):
    __tablename__ = 'idmapping'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playername = db.Column(db.String(64), db.ForeignKey('player.name'),
                           nullable=False)
    gameid = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<IDMapping %r>' % self.name


class GameIDInfo(db.Model):
    __tablename__ = 'gameidinfo'
    gameid = db.Column(db.String(64), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    tier = db.Column(db.String(32), nullable=False)
    lp = db.Column(db.Integer, nullable=False)
    win = db.Column(db.Integer, nullable=False)
    lose = db.Column(db.Integer, nullable=False)
    winratio = db.Column(db.Float, nullable=False)
    mmr = db.Column(db.Integer, nullable=False)
    twentywin = db.Column(db.Integer, nullable=False)
    twentylose = db.Column(db.Integer, nullable=False)
    twentywinratio = db.Column(db.Float, nullable=False)
    twentyavgkill = db.Column(db.Float, nullable=False)
    twentyavgdeath = db.Column(db.Float, nullable=False)
    twentyavgassist = db.Column(db.Float, nullable=False)
    twentyavgkda = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<GameIDInfo %r>' % self.name
