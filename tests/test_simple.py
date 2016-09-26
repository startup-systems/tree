import helpers
import os
import pytest
import tempfile


def test_compare():
    path = '../'
    assert helpers.tree_correct(path) == helpers.pytree(path)