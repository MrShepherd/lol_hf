import os
from app import create_app, db
from app.models import Team, Player, IDMapping, GameIDInfo, Summary, IDMappingManual, Sponsor, SponsorManual
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Team=Team, Player=Player, IDMapping=IDMapping, GameIDInfo=GameIDInfo, Summary=Summary, IDMappingManual=IDMappingManual, SponsorManual=SponsorManual, Sponsor=Sponsor)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
