import helpers
import pytest
import re


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


@pytest.mark.score(20)
def test_file_dir_names():
    path = 'examples'
    output = helpers.run_and_capture(['./pytree.py', path])
    names = re.findall('[a-z]+(?:\.[a-z]+)?', output)
    assert names == ['examples', 'simple', 'another', 'bites', 'dust', 'dot.jpg', 'the', 'one.txt', 'directories', 'files']


@pytest.mark.score(30)
def test_with_path():
    path = 'examples'
    expected = helpers.run_and_capture(['tree', path])
    actual = helpers.run_and_capture(['./pytree.py', path])
    assert expected == actual
