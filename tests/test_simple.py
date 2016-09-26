import helpers
import os
import pytest
import tempfile


def test_no_errors():
    path = '../'
    assert helpers.tree_correct(path) == helpers.pytree(path)