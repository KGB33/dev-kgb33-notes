import os
from pathlib import Path

from flask import render_template

from notes import BASE_DIR

import markdown
from pygments.formatters import HtmlFormatter


def prepare_markdown(file_name: str):
    """
    Uses pypandoc to convert a markdown document to
    HTML, then fixes the img tags
    """
    path = str(BASE_DIR / file_name)

    with open(path) as md_file:
        content = markdown.markdown(
            md_file.read(),
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.codehilite",
            ],
        )

    formatter = HtmlFormatter(full=True, style="solarized-dark")
    css_string = f"<style>{formatter.get_style_defs()}</style>"
    content = content.replace('src="./', 'src="static/img/')
    return css_string + content


def render_markdown(file_name: str, template: str = "markdown_template.html"):
    """
    Converts a '.md' file to html, then
    renders it within a template using flask's
    render_template method.
    """
    content = prepare_markdown(file_name)
    return render_template(template, content=content)


def find_markdown_files(path=Path(f"{BASE_DIR}/static/markdown/")):
    """
    Find markdown files to create dynamic links
    """
    md_files = {path: []}
    for entry in os.scandir(path):
        if entry.name.endswith(".md"):
            md_files[path] += [
                entry.name,
            ]
        if entry.is_dir():
            md_files |= find_markdown_files(path / entry.name)
    return {key: value for key, value in md_files.items() if value}
