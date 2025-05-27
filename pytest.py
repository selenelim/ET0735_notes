pip install pytest

#MAIN FUNCTIONS
myfunctions.py
def get_total(marks):
    return sum(marks)

def get_average(marks):
    return sum(marks) / len(marks)


#TEST MAIN FUNCTIONS
from my_functions import get_total, get_average

def test_get_total():
    assert get_total([10, 20, 30]) == 60

def test_get_average():
    assert get_average([10, 20, 30]) == 20


pytest
