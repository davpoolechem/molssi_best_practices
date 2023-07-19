"""
Unit tests for the measure.py module 
"""

import numpy as np
import pytest

import molssi_best_practices as mbp


@pytest.mark.slow
def test_calculate_distance():
    """Test computing distance between two points"""
    rA = np.array([0, 0, 0])
    rB = np.array([0, 0, 1])

    expected_distance = 1.0

    calculated_distance = mbp.calculate_distance(rA, rB)

    assert expected_distance == calculated_distance
