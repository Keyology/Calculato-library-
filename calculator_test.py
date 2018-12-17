import pytest
import calculator
import sys



def test_addition():
    assert 10 == calculator.add(5, 5)
        

def test_subtraction():
    assert 10 == calculator.subtract(20, 10)

def test_division():
    assert 2 == calculator.divide(4, 2)
    

def test_multiply():
    assert 25 == calculator.multiply(5, 5)
        
    
    
