from flask import render_template

from notes.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return(render_template("index.html"))


@bp.route('/postgresql')
def postgresql():
    return(render_template("postgresql/psql.html"))

