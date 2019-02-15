# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:20:16 2019

@author: Mars
"""

import pytest


@pytest.mark.parametrize("inputPatients, expected", [
        ([{"TSHData": [3, 4, 5, 6]}], "hypothyroidism"),
        ([{"TSHData": [9, 9, 9]}], "hypothyroidism"),
        ([{"TSHData": [0.1, 2, 3]}], "hyperthyroidism"),
        ([{"TSHData": [0.1, 0.1, 0.2, 0.5]}], "hyperthyroidism"),
        ([{"TSHData": [2, 3]}], "normal thyroid function"),
        ])
def test_diagnoseTSH(inputPatients, expected):
    from tsh import diagnoseTSH

    diagResults = diagnoseTSH(inputPatients)[0]
    assert diagResults["TSH Diagnosis"] == expected
