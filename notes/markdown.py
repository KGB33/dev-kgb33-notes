import pypandoc
from flask import render_template

from notes import BASE_DIR


def prepare_markdown(file_name: str):
    """
    Uses pypandoc to convert a markdown document to
    HTML, then fixes the img tags
    """
    path = str(BASE_DIR / file_name)
    content = pypandoc.convert_file(path, "html")
    content = content.replace('<img src="./', '<img src="static/img/')

    return content


def render_markdown(file_name: str, template: str = "markdown_template.html"):
    """
    Converts a '.md' file to html, then
    renders it within a template using flask's
    render_template method.
    """
    content = prepare_markdown(file_name)
    return render_template(template, content=content)
