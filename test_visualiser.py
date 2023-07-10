from visualiser import app


def test_000_header_presence(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales"


def test_001_visualiser_presence(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=5)


def test_002_radio_presence(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio", timeout=5)
