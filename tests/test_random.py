import helpers
from pathlib import Path
import os
import pytest
import random
import tempfile


@pytest.mark.score(5)
def test_output():
    with tempfile.TemporaryDirectory(suffix='-tree') as tmpdirname:
        num_files = random.randint(1, 10)
        file_numbers = random.sample(range(0, 100), num_files)
        file_numbers.sort()

        for file_num in file_numbers:
            path = os.path.join(tmpdirname, 'file{}.txt'.format(file_num))
            Path(path).touch()

        expected = helpers.run_and_capture(['tree', tmpdirname])
        actual = helpers.run_and_capture(['./pytree.py', tmpdirname])
        assert expected == actual
