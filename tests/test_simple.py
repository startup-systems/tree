import helpers
import pytest
import re


@pytest.mark.score(5)
def test_num_directories():
    path = 'examples/simple'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "2 directories" in output


@pytest.mark.score(5)
def test_num_files():
    path = 'examples/simple'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "4 files" in output


@pytest.mark.score(10)
def test_file_dir_names():
    path = 'examples/simple'
    output = helpers.run_and_capture(['./pytree.py', path])
    names = re.findall('[a-z]+(?:\.[a-z]+)?', output)
    names.sort()
    assert names == [
        'another',
        'bites',
        'directories',
        'dot.jpg',
        'dust',
        'examples',
        'files',
        'one.txt',
        'simple',
        'the'
    ]


@pytest.mark.score(15)
def test_full_output():
    path = 'examples/simple'
    expected = helpers.run_and_capture(['tree', path])
    actual = helpers.run_and_capture(['./pytree.py', path])
    assert expected == actual
