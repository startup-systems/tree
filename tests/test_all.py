import helpers
import pytest


@pytest.mark.score(5)
def test_without_path(monkeypatch):
    monkeypatch.chdir('examples')
    expected = helpers.run_and_capture(['tree'])
    actual = helpers.run_and_capture(['../pytree.py'])
    assert expected == actual
