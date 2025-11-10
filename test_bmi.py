import bmiLab3

def test_underweight():
    result_bmi = bmiLab3.calculate_bmi(weight=50, height=1.7)
    assert (result_bmi <= 18.5)

def test_normalweight():
    result_bmi = bmiLab3.calculate_bmi(weight=65, height=1.7)
    assert (18.5 < result_bmi <= 25.0)

def test_overweight():
    result_bmi = bmiLab3.calculate_bmi(weight=80, height=1.7)
    assert (result_bmi > 25.0)