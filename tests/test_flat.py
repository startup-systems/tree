import helpers
import pytest
import re


@pytest.mark.score(5)
def test_num_directories():
    path = 'examples/flat'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "0 directories" in output


@pytest.mark.score(5)
def test_num_files():
    path = 'examples/flat'
    output = helpers.run_and_capture(['./pytree.py', path])
    assert "3 files" in output


@pytest.mark.score(5)
def test_file_dir_names():
    path = 'examples/flat'
    output = helpers.run_and_capture(['./pytree.py', path])
    names = re.findall('[a-z]+\d?(?:\.[a-z]+)?', output)
    names.sort()
    assert names == [
        'directories',
        'examples',
        'file1.txt',
        'file2.txt',
        'file3.txt',
        'files',
        'flat'
    ]


@pytest.mark.score(15)
def test_full_output():
    path = 'examples/flat'
    expected = helpers.run_and_capture(['tree', path])
    actual = helpers.run_and_capture(['./pytree.py', path])
    assert expected == actual
