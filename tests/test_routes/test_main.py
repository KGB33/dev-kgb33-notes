def test_index(test_client):
    """
    When the the index page is called
    check that the correct template is rendered
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<!-- index.html -->" in response.data


def test_postgresql(test_client):
    """
    When the postgresql page is called
    Check that the postgresql notes is displayed
    in the markdown template
    """
    response = test_client.get("/postgresql")
    assert response.status_code == 200
    assert b"<!-- markdown_template.html -->" in response.data
    assert (
        b'The youtube video can be found <a href="https://www.youtube.com/watch?v=qw--VYLpxG4">here</a>.</p>'
        in response.data
    )
