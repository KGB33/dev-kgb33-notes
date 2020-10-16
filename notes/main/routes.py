from flask import render_template

from notes.main import bp

from notes.markdown import render_markdown, find_markdown_files


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")


@bp.route("/postgresql")
def postgresql():
    return render_markdown("static/markdown/psql.md")


@bp.route("/go/channels")
def go_channels():
    return render_markdown("static/markdown/Go/NoSuchThingAsGenerators.md")


@bp.route("/toc")
def table_of_contents():
    print("In TOC route")
    return "<br>".join(find_markdown_files())
