import helpers
import hashlib
import os
import pytest
import tempfile


def test_compare():
    path = 'examples'
    correct = helpers.tree_correct(path)
    output = helpers.pytree(path)
    assert len(correct) == len(output)
