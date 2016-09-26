import helpers
import os
import pytest
import tempfile


def test_no_errors():
    correct = helpers.pytree('../simple')
    pytree = helpers.pytree('../simple')
    assert correct == pytree