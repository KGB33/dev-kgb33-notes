from pathlib import Path

from flask import render_template, request, abort

from notes import BASE_DIR

from notes.main import bp

from notes.markdown import render_markdown, find_markdown_files


@bp.route("/")
@bp.route("/index")
def index():
    files = {p.name: f for p, f in find_markdown_files().items()}
    return render_template("index.html", files=files)


@bp.route("/doc")
def document():
    path = Path(f"{BASE_DIR}/static/markdown/")
    if request.args["dir"] != "markdown":
        path = path / request.args["dir"]
    path = path / request.args["file"]

    if not path.exists():
        abort(404)

    return render_markdown(path)
