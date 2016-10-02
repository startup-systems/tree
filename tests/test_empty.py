import helpers
import pytest
import tempfile


@pytest.fixture
def emptydir():
    with tempfile.TemporaryDirectory(suffix='-tree') as emptydir:
        yield emptydir


@pytest.mark.score(5)
def test_num_directories(emptydir):
    output = helpers.run_and_capture(['./pytree.py', emptydir])
    assert "0 directories" in output


@pytest.mark.score(5)
def test_num_files(emptydir):
    output = helpers.run_and_capture(['./pytree.py', emptydir])
    assert "0 files" in output


@pytest.mark.score(5)
def test_full_output(emptydir):
    expected = helpers.run_and_capture(['tree', emptydir])
    actual = helpers.run_and_capture(['./pytree.py', emptydir])
    assert expected == actual
