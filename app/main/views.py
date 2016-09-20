from . import main


@main.route('/', methods=['GET'])
def index():
    return '<h1>hello,world</h1>'
