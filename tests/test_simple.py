import helpers
import pytest


@pytest.mark.score(5)
def test_num_directories():
    path = 'examples'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "3 directories" in output


@pytest.mark.score(5)
def test_num_files():
    path = 'examples'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "4 files" in output


@pytest.mark.score(40)
def test_with_path():
    path = 'examples'
    expected = helpers.run_and_capture(['tree', path])
    actual = helpers.run_and_capture(['./pytree.py', path])
    assert expected == actual


@pytest.mark.score(40)
def test_without_path():
    expected = helpers.run_and_capture(['tree'])
    actual = helpers.run_and_capture(['./pytree.py'])
    assert expected == actual
