"""
Unit and regression test for the molssi_best_practices package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import molssi_best_practices


def test_molssi_best_practices_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molssi_best_practices" in sys.modules
