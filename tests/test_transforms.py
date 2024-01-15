# -*- coding: utf-8 -*-
"""
Created on Mon Jan  15 10:35:30 2024

@author: SamHill
Unit tests to make sure transforms give expected response.
"""
from __future__ import annotations
import pytest
import numpy as np
import numpy.typing as npt

import ClarkePark


# Create alias for 4 floating point arrays return

try:
    four_arrays = tuple[npt.NDArray[np.float64], npt.NDArray[np.float64],
                        npt.NDArray[np.float64], npt.NDArray[np.float64]]
except TypeError:
    from typing import Tuple
    four_arrays = Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64],
                        npt.NDArray[np.float64], npt.NDArray[np.float64]]


# Global amplitude
ampl = np.sqrt(2) * 127


# Create example dataset
@pytest.fixture
def create_threephase() -> four_arrays:
    ''' Creates three-phase signals as dataset for tests.

    Just like the README file, it creates simple three-phase signals
    (A, B, C) to be used as an example dataset. Each signal, with a 60 Hz
    frequency will be spaced by 120 degrees apart, and have an peak amplitude
    of √2 * 127 V.

    Inputs:
        None

    Returns:
        signals : Three 1d arrays representing signals from each phase.
    '''
    # Create time array (10 cycles @ 60 Hz)
    freq = 60.
    end_time = 10 / freq
    n_points = 1000
    t = np.linspace(0, end_time, n_points)
    wt = 2*np.pi*freq*t
    amp = np.sqrt(2) * 127

    A = amp * np.sin(wt + 0*np.pi/180)
    B = amp * np.sin(wt + 240*np.pi/180)
    C = amp * np.sin(wt + 120*np.pi/180)

    signals = (wt, A, B, C)
    return signals


@pytest.mark.parametrize("phase,expected_result",
                         [(0, (ampl, 0, 0)),
                          (90, (0, -ampl, 0)),
                          (180, (-ampl, 0, 0)),
                          (270, (0, ampl, 0))])
def test_dqz(create_threephase: four_arrays, phase: float,
             expected_result: tuple[float, float, float]) -> None:
    ''' Tests that the DQZ transform gives correct response.

    Will test the dqz transform for different phase angles to ensure
    expected result is obtained.

    Inputs:
        creatre_threephase : three-phase signals from fixture
        phase (float): Constant phase offset applied to rotating axes.
        expected_result (3-tuple): Expected results

    Returns:
        None
    '''
    # Unpack signals
    wt, A, B, C = create_threephase

    # Calculate transform
    d, q, zero = ClarkePark.abc_to_dq0(A, B, C, wt, phase*np.pi/180)

    # Compare results (up to fp precision)
    assert (d.mean(), q.mean(), zero.mean()) == pytest.approx(expected_result)


def test_dqz_roundtrip(create_threephase: four_arrays) -> None:
    ''' Tests that dqz and then inverse dqz transform bring you
    back to where you sorted.

    A test to make sure that the DQZ transform followed by applying
    the inverse returns the same result.

    Inputs:
        creatre_threephase : three-phase signals from fixture

    Returns:
        None
    '''
    # Unpack signals
    wt, A, B, C = create_threephase

    # Calculate transform
    d, q, zero = ClarkePark.abc_to_dq0(A, B, C, wt, delta=0)

    # Calculate inverse transform
    A_prime, B_prime, C_prime = ClarkePark.dq0_to_abc(d, q, zero, wt, delta=0)

    # Test that A == A', B == B', C == C'
    A_test = np.allclose(A, A_prime)
    B_test = np.allclose(B, B_prime)
    C_test = np.allclose(C, C_prime)

    # Check that all results are true
    assert all((A_test, B_test, C_test))
