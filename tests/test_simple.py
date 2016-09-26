import helpers
import os
import pytest
import tempfile


def test_compare():
    path = '/home/'
    assert helpers.tree_correct(path) == helpers.pytree(path)