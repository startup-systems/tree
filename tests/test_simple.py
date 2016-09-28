import helpers


def test_compare():
    path = 'examples'
    expected = helpers.run_and_capture('tree', path)
    actual = helpers.run_and_capture('./pytree.py', path)
    assert expected == actual
