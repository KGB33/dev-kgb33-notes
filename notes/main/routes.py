from flask import render_template, request

from notes.main import bp

from notes.markdown import render_markdown, find_markdown_files


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html", files=find_markdown_files())


@bp.route("/doc")
def document():
    return render_markdown(f"{request.args['dir']}/{request.args['file']}")
