from flask import render_template

from notes.main import bp

from notes.main.documents import prepare_markdown


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")


@bp.route("/postgresql")
def postgresql():
    content = prepare_markdown("static/markdown/psql.md")
    return render_template("markdown_template.html", content=content)
