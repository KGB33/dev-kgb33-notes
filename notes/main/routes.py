from notes.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return("This is the index")

