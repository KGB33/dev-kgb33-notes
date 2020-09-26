import pypandoc

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
