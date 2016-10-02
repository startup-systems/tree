import helpers
import pytest


@pytest.mark.score(10)
def test_without_path():
    expected = helpers.run_and_capture(['tree'])
    actual = helpers.run_and_capture(['./pytree.py'])
    assert expected == actual
