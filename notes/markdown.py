import os
from pathlib import Path

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
