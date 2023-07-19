"""
Unit and regression test for the molssi_best_practices package.
"""

# Import package, test suite, and other packages as needed
import numpy as np
import pytest
import sys

import molssi_best_practices as mbp


def test_molssi_best_practices_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molssi_best_practices" in sys.modules


def test_build_bond_list_exception():
    """Make sure the code throws correctly on nonsensical user inputs."""
    coordinates = np.array([[0, 0, 0], [0, 1, 0]])

    with pytest.raises(ValueError) as e_info:
        mbp.build_bond_list(coordinates, max_bond=1.5, min_bond=2)
