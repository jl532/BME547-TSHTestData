# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:20:16 2019

@author: Mars
"""

import pytest


@pytest.mark.parametrize("inputPatients, expected", [
        ({"TSHData" : [3, 4, 5, 6]}, 
        {"TSHData" : [3, 4, 5, 6], "TSH Diagnosis":"hypothyroidism"}),
        
        
        ])
def test_diagnoseTSH(inputPatients, expected):
    from tsh import diagnoseTSH
    
    diagResults = diagnoseTSH(inputPatients)
    assert diagResults == expected