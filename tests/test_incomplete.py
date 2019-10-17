from reporter.header import create_header


def test_create_header_incomplete():
    auth_list = [
        {"first": "Jojo",},
        {"last": "Dodo",},
    ]

    res = create_header(auth_list, "NY")

    assert "Dudu" in res
    assert "Jojo" in res
