"""
Unit and regression test for the montecarlo2 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo2


def test_montecarlo2_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo2" in sys.modules
