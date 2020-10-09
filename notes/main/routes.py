from flask import render_template

from notes.main import bp

from notes.markdown import render_markdown


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")


@bp.route("/postgresql")
def postgresql():
    return render_markdown("static/markdown/psql.md")
